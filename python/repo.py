from models import TalhaoBase


class Cultura:
    """Classe "mãe" (genérica) para qualquer cultura agrícola."""
    def __init__(self):
        self.talhoes: list[TalhaoBase] = []

    def adicionar(self, talhao: TalhaoBase):
        self.talhoes.append(talhao)

    def listar(self, nome: str):
        if not self.talhoes:
            print(f"⚠️ Nenhum talhão cadastrado em {nome}.")
            return

        print(f"\n=== Lista de talhões ({nome}) ===")
        for i, talhao in enumerate(self.talhoes):
            print(
                f"[{i}] Talhão={talhao.nome}, "
                f"Área={talhao.calcular_area():.2f} m², ",
                f"Litros={talhao.calcular_litros():.2f} L"
            )

    def atualizar(self, idx: int, campo: str, novo_valor: str):
        try:
            """Utilizando try/except IndexError para verificar se o index buscado existe"""
            talhao = self.talhoes[idx]
        except IndexError:
            print("⚠️ Índice inválido.")
            return

        tipo = type(getattr(talhao, campo))  # pega o tipo do atributo que será alterado
        try:
            """Tenta converter para o mesmo tipo.
            Se o tipo inserido for diferente do tipo do atributo, lança exceção
            - talhao: texto
            - ruas: inteiro
            - demais: float
            """
            valor_convertido = tipo(novo_valor)
        except ValueError:
            print(f"⚠️ Valor inválido para '{campo}'. Deve ser {tipo.__name__}.")
            return

        setattr(talhao, campo, valor_convertido)  # define o novo valor para o atributo
        print("✅ Talhão atualizado com sucesso.")

    def deletar(self, idx: int):
        try:
            self.talhoes.pop(idx)
            print("✅ Talhão deletado com sucesso.")
        except IndexError:
            print("⚠️ Índice inválido.")


class Cafe(Cultura):
    """Class responsável para realizar CRUD da cultura café
    pass adicionado, pois todos os métodos necessários estão na classe pai
    """
    pass


class Soja(Cultura):
    """Class responsável para realizar CRUD da cultura café
    pass adicionado, pois todos os métodos necessários estão na classe pai
    """
    pass


class Repo:
    """"Repositório" que guarda UMA instância de cada cultura para o app inteiro."""
    def __init__(self):
        self.cafe = Cafe()  # Banco de dados em memória para café
        self.soja = Soja()  # Banco de dados em memória para soja

    def get(self, cultura_nome: str) -> Cultura:
        """Facilita pegar a instância correta com base no texto digitado no menu."""
        return self.cafe if cultura_nome == "cafe" else self.soja