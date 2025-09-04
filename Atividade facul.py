# Por padrão vou usar tudo em Metros.
# (Isso significa que todos os comprimentos e medidas de distância serão considerados em "m".)

import csv  # Módulo da própria linguagem para gravar/ler arquivos CSV.

class Cultura:  # Classe "mãe" (genérica) para qualquer cultura agrícola.
    # Pessoa A: definir atributos comuns; Pessoa B: métodos de cálculo depois
    def __init__(self):
       # Listas (vetores) que guardam os dados de cada talhão.
       # Cada posição i nas listas representa o MESMO talhão.
       self.talhao = []             # Identificador/nome do talhão (texto)
       self.ruas = []               # Quantidade de ruas (linhas de plantio) no talhão (inteiro)
       self.metros_por_rua = []     # Comprimento de cada rua, em metros (float)
       self.dose_ml_por_m = []      # Dose (em mL) aplicada por metro linear (float)
       # Removidos do escopo: cult, area (não exigidos pelo enunciado)

    # Pessoa B: implementar depois
    def calcular_area(self, i):
      # Método "genérico" (na classe-mãe) — cada cultura calcula área de um jeito.
      # Aqui fica como "pass" porque as classes-filhas (Café/Soja) é que implementam.
      pass

    # Pessoa B: implementar depois
    def calcular_litros(self, i):
        # Cálculo da quantidade total de insumo (em L) para o talhão i.
        # Lógica: número_de_ruas * metros_por_rua * (dose_mL_por_m / 1000 para converter mL -> L)
        return self.ruas[i] * self.metros_por_rua[i] * (self.dose_ml_por_m[i] / 1000)
        # Exemplo: 10 ruas * 100 m/rua * 500 mL/m = 500.000 mL -> 500 L


class Cafe(Cultura):  # Cultura "café": área em formato de retângulo (comprimento x largura).
    # Pessoa A: definir atributos específicos (comprimento, largura)
    def __init__(self):
     # Ajuste: a classe-mãe (Cultura.__init__) NÃO recebe argumentos.
     # Portanto, chamamos sem passar "cafe".
     super().__init__()        # (antes: super().__init__("cafe"))
     self.comprimento = []     # Comprimento do talhão, em metros (float)
     self.largura = []         # Largura do talhão, em metros (float)
     # Observação: mantemos tudo em metros para padronizar e evitar conversões depois.

    # Pessoa B: implementar depois (área retângulo)
    def calcular_area(self, i):
        # Área do retângulo = comprimento * largura
        return self.comprimento[i] * self.largura[i]
        # Retorna m²


class Soja(Cultura):  # Cultura "soja": área em formato de círculo (usamos o raio).
    # Pessoa A: definir atributos específicos (raio)
    def __init__(self):
      # Ajuste: a classe-mãe (Cultura.__init__) NÃO recebe argumentos.
      # Portanto, chamamos sem passar "soja".
      super().__init__()   # (antes: super().__init__("soja"))
      self.raio = []       # Raio do talhão circular, em metros (float)
      # Observação: índices de todas as listas precisam ficar alinhados (mesma posição = mesmo talhão)

    """
        PESSOA A:
        OBJETIVO:
        - Inicializar a cultura 'soja' chamando super().__init__().  (sem argumentos)
        - Criar LISTA ESPECÍFICA da soja:
            self.raio -> list[float]  (m)
        - Garantir alinhamento de índices com as listas comuns.
    """

    # Pessoa B: implementar depois (área círculo)
    def calcular_area(self, i):
        # Área do círculo = π * raio² (aqui usamos 3.14 como aproximação de π)
        return 3.14 * (self.raio[i] ** 2)
        # Retorna m²


class Repo:  # "Repositório" que guarda UMA instância de cada cultura para o app inteiro.
    # Pessoa A: estruturar referências; Pessoa B: ajustar se necessário
    def __init__(self):
       self.soja = Soja()  # Banco de dados em memória para soja
       self.cafe = Cafe()  # Banco de dados em memória para café

    def get(self, cultura_nome):  # Pessoa A
       # Facilita pegar a instância correta com base no texto digitado no menu.
       if cultura_nome == "cafe":
           return self.cafe
       else:
           return self.soja

repo = Repo()  # Cria o repositório global usado pelas funções do menu.


# ==============================
# FUNÇÕES DO APP (MENU + CRUD + EXPORT + LOOP)
# ==============================

def menu():
    # Loop que exibe o menu e só retorna quando a opção é válida.
    while True:
        print("\n===== MENU =====")
        print("1) Inserir")
        print("2) Listar")
        print("3) Atualizar")
        print("4) Deletar")
        print("5) Exportar CSV")
        print("0) Sair")
        opcao = input("Escolha uma opção: ")
        if opcao in ["0", "1", "2", "3", "4", "5"]:
            return opcao
        else:
            print("⚠️ Opção inválida, tente novamente.")
        # Obs.: aqui usamos decisão (if/else) e repetição (while) — requisitos do enunciado.

def escolher_cultura():
    # Garante que o usuário digite apenas "cafe" ou "soja".
    while True:
        escolha = input("Qual cultura você quer operar? (cafe/soja): ").strip().lower()
        if escolha in ["cafe", "soja"]:
            return escolha
        else:
            print("⚠️ Digite apenas 'cafe' ou 'soja'.")
        # .strip() remove espaços extras; .lower() deixa tudo minúsculo para evitar erro por capitalização.

def inserir_registro(cultura_nome):  # Pessoa A
    c = repo.get(cultura_nome)  # Pega o "banco" (instância) de café ou soja.

    # Coleta de dados gerais do talhão (iguais para qualquer cultura):
    talhao = input("ID/Nome do talhão: ")
    ruas = int(input("Número de ruas: "))
    metros = float(input("Comprimento de cada rua (m): "))
    dose = float(input("Dose em mL por metro: "))

    # Armazenamos nas listas equivalentes. Todas têm o mesmo comprimento.
    c.talhao.append(talhao)
    c.ruas.append(ruas)
    c.metros_por_rua.append(metros)
    c.dose_ml_por_m.append(dose)

    # Dados específicos por cultura:
    if cultura_nome == "cafe":
        comprimento = float(input("Comprimento do talhão (m): "))
        largura = float(input("Largura do talhão (m): "))
        c.comprimento.append(comprimento)
        c.largura.append(largura)
    else:
        raio = float(input("Raio do talhão (m): "))
        c.raio.append(raio)

    print("✅ Talhão cadastrado com sucesso!")
    # Importante: mantemos a ordem de inserção para que o índice i identifique o mesmo talhão em todas as listas.

def listar_registros(cultura_nome):  # Pessoa A
    c = repo.get(cultura_nome)  # Acessa os dados da cultura escolhida.

    if len(c.talhao) == 0:
        # Se não há registros, avisamos e retornamos.
        print(f"⚠️ Nenhum talhão cadastrado em {cultura_nome}.")
        return

    print(f"\n=== Lista de talhãos ({cultura_nome}) ===")
    # Percorremos pelo índice para calcular área e litros de cada talhão.
    for i in range(len(c.talhao)):
        area = c.calcular_area(i)       # m²
        litros = c.calcular_litros(i)   # L
        print(f"[{i}] Talhão={c.talhao[i]}, Área={area:.2f} m², Litros={litros:.2f} L")

def atualizar_registro(cultura_nome):  # Pessoa B
    c = repo.get(cultura_nome)

    if len(c.talhao) == 0:
        print("⚠️ Nenhum talhão cadastrado para atualizar.")
        return

    # Pergunta qual índice o usuário quer alterar (posição na lista).
    idx_txt = input("Índice do talhão a alterar: ")

    # Tenta converter para inteiro (tratando erro de digitação).
    try:
        idx = int(idx_txt)
    except ValueError:
        print("⚠️ Índice inválido.")
        return

    # Confere se o índice existe (0 até tamanho-1).
    if idx < 0 or idx >= len(c.talhao):
        print("Índice inválido.")
        return

    # Campos que podem ser alterados:
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

    # Novo valor (como texto por enquanto).
    novo_txt = input(f"Novo valor para '{campo}': ").strip()

    # Convertemos para o tipo correto:
    # - talhao: texto
    # - ruas: inteiro
    # - demais: float
    if campo == "talhao":
        novo_val = novo_txt
    elif campo == "ruas":
        try:
            novo_val = int(novo_txt)
        except ValueError:
            print("⚠️ Valor inválido para 'ruas'. Deve ser um número inteiro.")
            return
    else:
        try:
            novo_val = float(novo_txt)
        except ValueError:
            print(f"⚠️ Valor inválido para '{campo}'. Deve ser um número.")
            return

    # getattr(c, campo) retorna a lista certa (ex.: c.largura, c.raio, etc.).
    # [idx] posiciona no talhão correto, e gravamos o novo valor.
    getattr(c, campo)[idx] = novo_val
    print("✅ Talhão atualizado com sucesso.")
    # Obs.: aqui atualizamos "em memória". Não grava em arquivo — isso é feito na exportação CSV.

def deletar_registro(cultura_nome):  # Pessoa B
    c = repo.get(cultura_nome)

    if len(c.talhao) == 0:
        print("⚠️ Nenhum talhão cadastrado para deletar.")
        return

    idx_txt = input("Índice do talhão a deletar: ")
    try:
        idx = int(idx_txt)
    except ValueError:
        print("⚠️ Índice inválido.")
        return

    if idx < 0 or idx >= len(c.talhao):
        print("⚠️ Índice inválido.")
        return

    # Removemos o talhão em TODAS as listas para manter tudo alinhado.
    c.talhao.pop(idx)
    c.ruas.pop(idx)
    c.metros_por_rua.pop(idx)
    c.dose_ml_por_m.pop(idx)

    if cultura_nome == "cafe":
        c.comprimento.pop(idx)
        c.largura.pop(idx)
    else:
        c.raio.pop(idx)

    print("✅ Talhão deletado com sucesso.")

def exportar_csv():  # Pessoa B
    # Caminho do arquivo de saída (você pode mudar se quiser).
    caminho = "dados.csv"

    rows = []  # Aqui vamos juntar todas as linhas a serem escritas no CSV.

    # Percorremos os talhões de café e calculamos valores derivados (área e litros).
    c = repo.cafe
    for i in range(len(c.talhao)):
        area = c.calcular_area(i)
        litros = c.calcular_litros(i)
        rows.append([
            "cafe", c.talhao[i], area,
            c.ruas[i], c.metros_por_rua[i], c.dose_ml_por_m[i],
            litros,
        ])

    # Percorremos os talhões de soja.
    s = repo.soja
    for i in range(len(s.talhao)):
        area = s.calcular_area(i)
        litros = s.calcular_litros(i)
        rows.append([
            "soja", s.talhao[i], area,
            s.ruas[i], s.metros_por_rua[i], s.dose_ml_por_m[i],
            litros,
        ])

    # Abrimos/criamos o CSV e escrevemos cabeçalho + linhas.
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["cultura","talhao","area_m2","ruas","metros_por_rua","dose_ml_por_m","litros"])
        writer.writerows(rows)

    print(f"✔ Exportado para {caminho}")
    # Você pode abrir esse arquivo no Excel/Google Sheets para conferir.

def loop():  # Pessoa B
     # Loop principal do programa: exibe menu, lê opção e chama a função correspondente.
    while True:
        op = menu()  # Retorna a opção válida como string.

        if op == "1":
            cultura = escolher_cultura()
            inserir_registro(cultura)

        elif op == "2":
            cultura = escolher_cultura()
            listar_registros(cultura)

        elif op == "3":
            cultura = escolher_cultura()
            atualizar_registro(cultura)

        elif op == "4":
            cultura = escolher_cultura()
            deletar_registro(cultura)

        elif op == "5":
            exportar_csv()

        elif op == "0":
            print("Até mais!")
            break  # Sai do loop e encerra o programa.

        else:
            print("⚠️ Opção inválida.")  # Blindagem extra (não deve acontecer por causa do menu())

# ==============================
# MAIN
# ==============================
if __name__ == "__main__":  # Pessoa B
    # Ponto de entrada: se o arquivo for executado diretamente (e não importado), inicia o app.
    loop()
    # O loop() só termina quando o usuário escolhe "0" no menu.

