import csv

class Cultura:  # Pessoa A: definir atributos comuns; Pessoa B: métodos de cálculo depois
    def __init__(self, nome):
       # renomeado p/ seguir o enunciado
       self.talhao = []             #(não existia)
       self.ruas = []               # ok (já existia como 'ruas')
       self.metros_por_rua = []     # era: self.Mpr
       self.dose_ml_por_m = []      # era: self.mlpM
       # removidos: self.cult, self.area (não são necessárias pelo enunciado)
    #criei listas kk

    """
        PESSOA A:ma
        - Guardar o nome da cultura (ex.: "cafe" ou "soja") em um atributo (ex.: self.nome = nome).
        - Criar as LISTAS (vetores) COMUNS para armazenar dados de cada talhão (mesmo índice = mesmo talhão):
            self.talhao           -> list[str]  (ex.: "T1", "T2"...)
            self.ruas             -> list[int]  (quantidade de linhas/ruas no talhão)
            self.metros_por_rua   -> list[float] (comprimento de cada rua em metros)
            self.dose_ml_por_m    -> list[float] (dose em mL por metro a ser pulverizada/aplicada)
        - NÃO chamar menu aqui (retire/ignore a linha self.menu_principal()):
            * O fluxo de menu (loop) deve estar fora (ex.: função loop()).
        """

    # Pessoa B: implementar depois
    def calcular_area(self, i):       
      pass

    # Pessoa B: implementar depois
    def calcular_litros(self, i):
        # atualizado p/ nomes do enunciado
        return self.ruas[i] * self.metros_por_rua[i] * (self.dose_ml_por_m[i] / 1000)
    #faz o calculo de litros baseado nas informações que vc me deu


class Cafe(Cultura):  # Pessoa A: definir atributos específicos (comprimento, largura)
    def __init__(self):
     super().__init__("cafe")
     self.comprimento = [] 
     self.largura = []      # era: self.larg
    #criei a lista para armazenar o comprimento e fds tlgd da pra ver ai  
    #lembrar de colocar pra ficar em apenas metro

    """
        PESSOA A:
        OBJETIVO:
        - Inicializar a cultura 'cafe' chamando super().__init__("cafe").
        - Criar LISTAS ESPECÍFICAS do café:
            self.comprimento -> list[float]  (m)
            self.largura     -> list[float]  (m)
        - Essas listas devem ter o MESMO TAMANHO das listas comuns (mesmo índice = mesmo talhão).
        """

    # Pessoa B: implementar depois (área retângulo)
    def calcular_area(self, i):
        # atualizado p/ nomes do enunciado
        return self.comprimento[i] * self.largura[i]
        #calcula a area do talhão baseado no comprimento e largura(retangulo)


class Soja(Cultura):  # Pessoa A: definir atributos específicos (raio)
    def __init__(self):
      super().__init__("soja")
      self.raio = []
        #super server para transferir dados de uma classe para a outra
        #mema fita de antes
        #lembrar de colocar pra ficar em apenas metro
    """
        PESSOA A:
        OBJETIVO:
        - Inicializar a cultura 'soja' chamando super().__init__("soja").
        - Criar LISTA ESPECÍFICA da soja:
            self.raio -> list[float]  (m)
        - Garantir alinhamento de índices com as listas comuns.
        """

    # Pessoa B: implementar depois (área círculo)
    def calcular_area(self, i):
        return 3.14 * (self.raio[i] ** 2)
    #calcula a area do talhão baseado no raio(circulo)


class Repo:  # Pessoa A: estruturar referências; Pessoa B: ajustar se necessário
    def __init__(self):
       self.soja = Soja()
       self.cafe = Cafe()
       #mais lista 
       #pra puxar a instance <- ta em ingles aff

    def get(self, cultura_nome):  # Pessoa A
       if cultura_nome == "cafe":
           return self.cafe
       else:
           return self.soja
       #retornar a intancia de cultura a partir do nome 
       #https://chatgpt.com/share/68b741a8-462c-8011-b432-49ba5e3f4701


# ==============================
# FUNÇÕES DO APP (MENU + CRUD + EXPORT + LOOP)
# ==============================

def menu_principal():  # Pessoa A
    while True:
        print(" 1 Inserir\n" \
        "2) Listar\n" \
        "3) Atualizar\n" \
        "4) Deletar\n" \
        "5) Exportar CSV\n" \
        "0) Sair")
        opcao = input("")
        if opcao in ["0", "1","2","3","4","5"]:
            return opcao
        else: 
         print("⚠️ Opção inválida, tente novamente.")


def escolher_cultura():  # Pessoa A
    input("Qual cultura você quer operar? \n" \
    "(1 - café) ou (2 - soja) \n" \
    "")
    """
    PESSOA A:
    OBJETIVO:
    - Perguntar ao usuário qual cultura deseja operar.
    - Retornar "cafe" ou "soja".
    """
    pass


def inserir_registro(cultura_nome):  # Pessoa A
    """
    PESSOA A:
    OBJETIVO:
    - Receber do usuário os dados do talhão e adicioná-los nas LISTAS da cultura escolhida.
    """
    pass


def listar_registros(cultura_nome):  # Pessoa A
    """
    PESSOA A:
    OBJETIVO:
    - Percorrer os índices dos vetores da cultura escolhida e imprimir:
        [i] talhao=...  area_m2=...  litros=...
    """
    pass


def atualizar_registro(cultura_nome):  # Pessoa B
    c = repo.get(cultura_nome)
    if len(c.talhao) == 0:
        print("⚠️ Nenhum talhão cadastrado para atualizar.")
        return
    idx_txt = input("Índice do talhão a alterar: ")
    try: 
        idx = int(idx_txt)
    except ValueError:
        print("⚠️ Índice inválido.")
        return
    campos =  ["talhao", "ruas", "metros_por_rua", "dose_ml_por_m"]
    if cultura_nome == "cafe":
        campos += ["comprimento", "largura"]
    else:
        campos += ["raio"]
    print("Campos disponíveis para alterar: " + ", ".join(campos))
    campo = input("Qual campo alterar? ").strip().lower()
    if campo not in campos:
        print("⚠️ Campo inválido.")
        return
    novo_txt = input(f"Novo valor para '{campo}': ").strip()
    if campo == "talhao":
        novo_val = novo_txt
    elif campo == "ruas":
        try:
            novo_val = int(novo_txt)
        except ValueError:
            print("⚠️ Valor inválido para 'ruas'. Deve ser um número inteiro.")
            return
    # (restante ainda a implementar pela Pessoa B)


def deletar_registro(cultura_nome):  # Pessoa B
    """
    PESSOA B:
    OBJETIVO:
    - Remover o talhão de índice 'idx' de TODAS as listas correspondentes da cultura.
    """
    pass


def exportar_csv():  # Pessoa B
    """
    PESSOA B:
    OBJETIVO:
    - Gerar um arquivo CSV 'data/dados.csv' consolidando registros de CAFÉ e SOJA.
    """
    pass


def loop():  # Pessoa B
    """
    PESSOA B:
    OBJETIVO:
    - Controlar o ciclo do programa (loop de menu) até o usuário escolher sair.
    """
    pass


# ==============================
# MAIN
# ==============================
if __name__ == "__main__":  # Pessoa B
    """
    PESSOA B:
    OBJETIVO:
    - Ponto de entrada do programa.
    """
    pass
