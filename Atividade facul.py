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


