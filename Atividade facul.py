#Por padrão vou usar tudo em Metros 

import csv

class Cultura:  # Pessoa A: definir atributos comuns; Pessoa B: métodos de cálculo depois
    def __init__(self, nome):
       # renomeado p/ seguir o enunciado
       self.talhao = []             #(não existia)
       self.ruas = []               # ok (já existia como 'ruas')
       self.metros_por_rua = []     # era: self.Mpr
       self.dose_ml_por_m = []      # era: self.mlpM
       # removidos: self.cult, self.area (não são necessárias pelo enunciado)
    #listas criadas para armazenar 

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


    # Pessoa B: implementar depois (área retângulo)
    def calcular_area(self, i):
        # atualizado p/ nomes do enunciado
        return self.comprimento[i] * self.largura[i]
        #calcula a area do talhão baseado no comprimento e largura(retangulo)


class Soja(Cultura):  # Pessoa A: definir atributos específicos (raio)
    def __init__(self):
      super().__init__("soja")
      self.raio = [] #por padrão ele ta em Metros
        
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
       #pra puxar a instancia 
    def get(self, cultura_nome):  # Pessoa A
       if cultura_nome == "cafe":
           return self.cafe
       else:
           return self.soja
       #retornar a instancia de cultura a partir do nome 

repo = Repo()


# ==============================
# FUNÇÕES DO APP (MENU + CRUD + EXPORT + LOOP)
# ==============================

def menu(self):  
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
        #sistema de menu simples, caso a escolha esteja fora do planejado ira dar erro
    
def escolher_cultura(self):  
    while True:
        escolha = input("Qual cultura você quer operar? (cafe/soja): ").strip().lower()
        if escolha in ["cafe", "soja"]:
            return escolha
        else:
            print("⚠️ Digite apenas 'cafe' ou 'soja'.")
        #sistema para escolha simples
        #strip - serve para tirar os espaços do input para n causar problemas 
        #lower - server para deixar para deixar o input todo em minusculo 


def inserir_registro(cultura_nome):  # Pessoa A
    c = repo.get(cultura_nome) #pega a instância como "café" ou "soja"
    
    #dados sobre a plantação 
    talhao = input("ID/Nome do talhão: ")
    ruas = int(input("Número de ruas: "))
    metros = float(input("Comprimento de cada rua (m): "))
    dose = float(input("Dose em mL por metro: "))

    c.talhao.append(talhao)
    c.ruas.append(ruas)
    c.metros_por_rua.append(metros)
    c.dose_ml_por_m.append(dose)

    #pega os dados da plantação e salve nas respectivas listas

    #///////////////////////////////

    #Dados mais espeficicos 
    
    if cultura_nome == "cafe":
        comprimento = float(input("Comprimento do talhão (m): "))
        largura = float(input("Largura do talhão (m): "))
        c.comprimento.append(comprimento)
        c.largura.append(largura)
    else:
        raio = float(input("Raio do talhão (m): "))
        c.raio.append(raio)
    print("✅ Talhão cadastrado com sucesso!")

    #pega as medidas e salve nas respectivas listas



def listar_registros(cultura_nome):  # Pessoa A
    c = repo.get(cultura_nome)#para acessar os dados da cultura certa.

    if len(c.talhao) == 0: # verifica se a lsita "talhao" esta vazia e printa um erro se estiver 
        print(f"⚠️ Nenhum talhão cadastrado em {cultura_nome}.")
        return
    # percorre todos os talhões pelo índice
    print(f"\n=== Lista de talhãos ({cultura_nome}) ===")
    for i in range(len(c.talhao)):
        area = c.calcular_area(i)  # calcula a área do talhão no índice i
        litros = c.calcular_litros(i)  # calcula os litros necessários para o talhão i
         # mostra tudo numa linha: índice, nome do talhão, área e litros
        print(f"[{i}] Talhão={c.talhao[i]}, Área={area:.2f} m², Litros={litros:.2f} L")


def atualizar_registro(cultura_nome):  # Pessoa B
    # pega o "banco" da cultura certa
    c = repo.get(cultura_nome)
    # se não existe nenhum terreno dessa cultura ele da erro
    if len(c.talhao) == 0:
        print("⚠️ Nenhum talhão cadastrado para atualizar.")
        return
    #pede ao user qual terreno ele quer mudar
    idx_txt = input("Índice do talhão a alterar: ")

    #tenta converter oq o usuario digitou para inteiro
    try: 
        idx = int(idx_txt)
    except ValueError:
        print("⚠️ Índice inválido.")
        return
    
    # 5) confere se esse índice existe (ex.: 0, 1, 2... até o tamanho da lista - 1)
    if idx < 0 or idx >= len(c.talhao):
        print("Índice inválido.")
        return
    # 6) mostra os campos disponíveis para alterar (todos os atributos)
    campos =  ["talhao", "ruas", "metros_por_rua", "dose_ml_por_m"]

    # inclui os campos específicos da cultura
    if cultura_nome == "cafe":
        campos += ["comprimento", "largura"]
    else:
        campos += ["raio"]
    print("Campos disponíveis para alterar: " + ", ".join(campos))
    campo = input("Qual campo alterar? ").strip().lower()
    #se o campo digitado n existir ele da erro
    
    if campo not in campos:
        print("⚠️ Campo inválido.")
        return
    
    # 7) pede o novo valor para o campo escolhido
    novo_txt = input(f"Novo valor para '{campo}': ").strip()


    # 12) converte o novo valor para o tipo certo:
    #     - talhao = texto
    #     - ruas = inteiro
    #     - os demais (metros_por_rua, dose_ml_por_m, comprimento, largura, raio) = número decimal

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
        
    #  getattr(c, campo) pega a LISTA certa dentro do objeto (ex.: c.largura, c.raio, c.metros_por_rua)
    #  [idx] escolhe a posição do terreno que você quer mudar
    #  novo_val grava o novo valor nessa posição

    getattr(c, campo)[idx] = novo_val
    print("✅ Talhão atualizado com sucesso.")
        
    # (restante ainda a implementar pela Pessoa B)


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

    # Remove o talhão e todos os dados associados em todas as listas
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
    # caminho do arquivo CSV onde vamos salvar os dados
    caminho = "data/dados.csv" 

    rows = []  # lista de linhas que será gravada no CSV

    # percorre todos os terrenos de café
    c = repo.cafe
    for i in range(len(c.talhao)):
        area = c.calcular_area(i)          # calcula área daquele terreno
        litros = c.calcular_litros(i)      # calcula litros necessários
        # monta a linha com todos os dados e adiciona na lista 'rows'
        rows.append([
            "cafe", c.talhao[i], area,
            c.ruas[i], c.metros_por_rua[i], c.dose_ml_por_m[i],
            litros,
        ])

    # percorre todos os terrenos de soja
    s = repo.soja
    for i in range(len(s.talhao)):
        area = s.calcular_area(i)
        litros = s.calcular_litros(i)
        rows.append([
            "soja", s.talhao[i], area,
            s.ruas[i], s.metros_por_rua[i], s.dose_ml_por_m[i],
            litros,
        ])

    # abre o arquivo CSV no modo de escrita ("w") e garante codificação UTF-8
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)  # cria um "escritor" de CSV
        # escreve o cabeçalho (primeira linha do CSV)
        writer.writerow(["cultura","talhao","area_m2","ruas","metros_por_rua","dose_ml_por_m","litros"])
        # escreve todas as linhas guardadas em 'rows'
        writer.writerows(rows)

    # confirma para o usuário
    print(f"✔ Exportado para {caminho}")


def loop():  # Pessoa B
     # loop principal que mantém o programa rodando até o usuário sair
    while True:
        op = menu()  # mostra menu e espera escolha (string)

        if op == "1":
            cultura = escolher_cultura()   # escolhe café ou soja
            inserir_registro(cultura)      # insere novo terreno

        elif op == "2":
            cultura = escolher_cultura()
            listar_registros(cultura)      # lista todos os terrenos

        elif op == "3":
            cultura = escolher_cultura()
            atualizar_registro(cultura)    # atualiza dados de um terreno

        elif op == "4":
            cultura = escolher_cultura()
            deletar_registro(cultura)      # deleta um terreno

        elif op == "5":
            exportar_csv()                 # exporta todos para CSV

        elif op == "0":
            print("Até mais!")             # mensagem de saída
            break                          # sai do loop e termina o programa

        else:
            print("⚠️ Opção inválida.")     # caso o usuário digite errado


# ==============================
# MAIN
# ==============================
if __name__ == "__main__":  # Pessoa B
    # ponto de entrada do programa
    # se o arquivo for executado diretamente, começa o loop
    loop()


