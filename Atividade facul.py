#cudepinto12

class Cultura:  # Pessoa A: definir atributos comuns; Pessoa B: métodos de cálculo depois
    def __init__(self, nome):
       self.cult = ["cafe", "soja"]
       self.area = []
       self.ruas = []
       self.Mpr = []
       self.mlpM = []
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

        return self.ruas[i] * self.Mpr[i] * (self.mlpM[i] / 1000) 
    #faz o calculo de litros baseado nas informações que vc me deu
        


class Cafe(Cultura):  # Pessoa A: definir atributos específicos (comprimento, largura)
    def __init__(self):
     super().__init__("cafe")
     self.comprimento = [] 
     self.larg = []
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
        return self.comprimento[i] * self.larg[i]
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

def menu_principal(self):  # Pessoa A
    
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

    #amo cuzinho
    #https://www.jusbrasil.com.br/doutrina/secao/art-163-dano-codigo-penal-comentado-ed-2022/1728397427
    
    """
    PESSOA A:
    OBJETIVO:
    - Perguntar ao usuário qual cultura deseja operar.
    - Retornar "cafe" ou "soja".

    PASSOS:
    1) Mostrar prompt: "Cultura [1=Café  2=Soja]: "
    2) Ler entrada.
    3) Mapear "1" -> "cafe"; "2" -> "soja"; qualquer outra -> padrão (ex.: "soja").
    4) Retornar a string.
    """
    pass


def inserir_registro(cultura_nome):  # Pessoa A
    """
    PESSOA A:
    OBJETIVO:
    - Receber do usuário os dados do talhão e adicioná-los nas LISTAS da cultura escolhida.

    PASSOS:
    1) Obter a cultura no repositório: c = repo.get(cultura_nome).
    2) Pedir e APENDAR nas listas COMUNS, na MESMA ordem:
        - talhao (str)
        - ruas (int)
        - metros_por_rua (float)
        - dose_ml_por_m (float)
    3) Se 'cafe': pedir 'comprimento' (float) e 'largura' (float) e apendar nas listas específicas.
       Se 'soja' : pedir 'raio' (float) e apendar.
    4) Exibir confirmação ("Registro inserido.").
    5) NUNCA deixe listas com comprimentos diferentes: cada talhão cria um item em TODAS as listas daquela cultura.
    """
    pass


def listar_registros(cultura_nome):  # Pessoa A
    """
    PESSOA A:
    OBJETIVO:
    - Percorrer os índices dos vetores da cultura escolhida e imprimir:
        [i] talhao=...  area_m2=...  litros=...

    PASSOS:
    1) c = repo.get(cultura_nome)
    2) Se a lista c.talhao estiver vazia, imprimir "(vazio)" e retornar.
    3) Para i em range(len(c.talhao)):
        - area = c.calcular_area(i)        (Pessoa B já implementou nas classes)
        - litros = c.calcular_litros(i)    (Pessoa B implementará)
        - print formatado com índice e valores.
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
   
    


def deletar_registro(cultura_nome):  # Pessoa B
    """
    PESSOA B:
    OBJETIVO:
    - Remover o talhão de índice 'idx' de TODAS as listas correspondentes da cultura.

    PASSOS:
    1) c = repo.get(cultura_nome)
    2) Pedir 'idx'; validar o range.
    3) Executar pop(idx) nas listas COMUNS:
        talhao, ruas, metros_por_rua, dose_ml_por_m
    4) Executar pop(idx) na(s) lista(s) ESPECÍFICA(s):
        - Café: comprimento, largura
        - Soja: raio
    5) Confirmar ("Registro deletado.").
    """
    pass


def exportar_csv():  # Pessoa B
    """
    PESSOA B:
    OBJETIVO:
    - Gerar um arquivo CSV 'data/dados.csv' consolidando registros de CAFÉ e SOJA
      para que o script em R leia e calcule médias/desvios.

    COLUNAS SUGERIDAS:
    - cultura, talhao, area_m2, ruas, metros_por_rua, dose_ml_por_m, litros

    PASSOS:
    1) Criar uma lista 'rows' vazia.
    2) Para cada índice i dos talhões de café:
        - calcular area = cafe.calcular_area(i)
        - calcular litros = cafe.calcular_litros(i)
        - montar uma linha: ["cafe", talhao, area, ruas, metros_por_rua, dose, litros]
        - append em rows
    3) Repetir para soja (mesma lógica).
    4) Abrir (e criar se necessário) o arquivo 'data/dados.csv' para escrita.
    5) Escrever o cabeçalho e depois todas as linhas de 'rows'.
    6) Confirmar ("Exportado para data/dados.csv").
    7) TRATAR: criar a pasta 'data' se não existir (opcional).
    """
    pass


def loop():  # Pessoa B
    """
    PESSOA B:
    OBJETIVO:
    - Controlar o ciclo do programa (loop de menu) até o usuário escolher sair.

    PASSOS:
    1) while True:
         - op = menu_principal()   (ler opção)
         - if op == "1": inserir_registro(escolher_cultura())
         - elif op == "2": listar_registros(escolher_cultura())
         - elif op == "3": atualizar_registro(escolher_cultura())
         - elif op == "4": deletar_registro(escolher_cultura())
         - elif op == "5": exportar_csv()
         - elif op == "0": print("Até mais!") e break
         - else: print("Opção inválida.")
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
    - Aqui, simplesmente chamar loop().

    PASSOS:
    1) Chamar loop()
    """
    pass







