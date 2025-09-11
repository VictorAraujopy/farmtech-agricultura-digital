# FarmTech Solutions - Agricultura Digital 🌱

## 📋 Sobre o Projeto

A **FarmTech Solutions** desenvolveu uma aplicação Python para atender uma fazenda inovadora que busca migrar para a **Agricultura Digital**. O sistema permite o gerenciamento de cultivos, cálculo de áreas de plantio e otimização do uso de insumos agrícolas.

### 🎯 Objetivos

- Gerenciar dados de duas culturas principais: **Café** e **Soja**
- Calcular áreas de plantio com geometrias específicas para cada cultura
- Otimizar o manejo de insumos com cálculos precisos de aplicação
- Fornecer análises estatísticas dos dados coletados
- Simular ambiente colaborativo de desenvolvimento com versionamento Git

## 🌾 Culturas Suportadas

### ☕ Café
- **Geometria**: Área retangular (comprimento × largura)
- **Aplicação**: Ideal para plantios em terrenos regulares
- **Insumos**: Cálculo baseado em dose mL/metro linear

### 🌱 Soja
- **Geometria**: Área circular (baseada no raio)
- **Aplicação**: Ideal para sistemas de irrigação circular
- **Insumos**: Cálculo baseado em dose mL/metro linear

## 🏗️ Arquitetura do Sistema

```
farmtech-agricultura-digital/
├── main.py              # Ponto de entrada da aplicação
├── models.py            # Classes de modelo (TalhaoBase, TalhaoCafe, TalhaoSoja)
├── repo.py              # Repositório de dados e operações CRUD
├── ui.py                # Interface de usuário e validações
├── analise_estatistica.R # Análises estatísticas em R
├── dados.csv            # Arquivo de exportação de dados
└── README.md            # Documentação do projeto
```

### 🔧 Componentes Principais

#### `models.py` - Modelos de Dados
- **TalhaoBase**: Classe base com funcionalidades comuns
- **TalhaoCafe**: Especialização para cultura do café (área retangular)
- **TalhaoSoja**: Especialização para cultura da soja (área circular)

#### `repo.py` - Repositório de Dados
- **Cultura**: Classe base para operações CRUD
- **Cafe/Soja**: Classes específicas para cada cultura
- **Repo**: Gerenciador central dos dados em memória

#### `ui.py` - Interface do Usuário
- Funções de input seguro com validação
- Menu interativo com opções CRUD
- Exportação para CSV
- Tratamento de erros e feedback ao usuário

#### `analise_estatistica.R` - Análises Estatísticas
- Cálculo de médias, desvios padrão, mínimos e máximos
- Processamento automático de dados numéricos
- Uso da biblioteca `dplyr` para manipulação eficiente

## 🚀 Como Executar

### Pré-requisitos

**Python 3.12:**
```bash
# Verificar versão do Python
python --version
```

**R (para análises estatísticas):**
```r
# Instalar pacotes necessários
install.packages("dplyr")
```

### 💻 Executando a Aplicação Python

```bash
# Navegar até o diretório do projeto
cd farmtech-agricultura-digital

# Executar a aplicação
python main.py
```

### 📊 Executando Análises Estatísticas

```bash
# Após gerar dados na aplicação Python
# Executar script R
Rscript analise_estatistica.R
```

## 🎮 Funcionalidades

### Menu Principal

```
===== MENU =====
1) Inserir     # Adicionar novos talhões
2) Listar      # Visualizar talhões cadastrados
3) Atualizar   # Modificar dados existentes
4) Deletar     # Remover talhões
5) Exportar CSV # Gerar arquivo para análises
0) Sair        # Encerrar aplicação
```

### 📝 Inserção de Dados

**Para Café (Área Retangular):**
- Nome/ID do talhão
- Número de ruas de plantio
- Comprimento de cada rua (metros)
- Dose de aplicação (mL/metro)
- Comprimento total do talhão (metros)
- Largura do talhão (metros)

**Para Soja (Área Circular):**
- Nome/ID do talhão
- Número de ruas de plantio
- Comprimento de cada rua (metros)
- Dose de aplicação (mL/metro)
- Raio do talhão (metros)

### 🧮 Cálculos Automáticos

#### Área de Plantio
- **Café**: `área = comprimento × largura`
- **Soja**: `área = π × raio²`

#### Quantidade de Insumos
```python
litros_necessários = ruas × metros_por_rua × (dose_ml_por_m ÷ 1000)
```

**Exemplo prático:**
- 10 ruas × 100 metros/rua × 500 mL/metro = 500.000 mL = 500 litros

### 📈 Análises Estatísticas (R)

O script R gera automaticamente:
- **Média** de todas as variáveis numéricas
- **Desvio padrão** para análise de variabilidade
- **Valores mínimos e máximos** para range de dados
- **Análise por cultura** quando aplicável

## 💾 Estrutura de Dados

### Armazenamento em Memória (Vetores/Arrays)
Os dados são organizados em vetores Python (listas) dentro das classes:

```python
class Cultura:
    def __init__(self):
        self.talhoes: list[TalhaoBase] = []  # Array de talhões
```

### Exportação CSV
Estrutura do arquivo `dados.csv`:

| cultura | talhao | area_m2 | ruas | metros_por_rua | dose_ml_por_m | litros |
| ------- | ------ | ------- | ---- | -------------- | ------------- | ------ |
| cafe    | T001   | 5000.0  | 20   | 100.0          | 500.0         | 1000.0 |
| soja    | T002   | 7853.98 | 15   | 120.0          | 300.0         | 540.0  |

## 🔄 Controle de Fluxo

### Estruturas de Decisão (`if/elif/else`)
- Validação de entrada de dados
- Seleção de cultura (café/soja)
- Navegação no menu principal
- Tratamento de erros

### Estruturas de Repetição (`while/for`)
- Loop principal da aplicação
- Validação contínua de inputs
- Iteração sobre listas de talhões
- Processamento de dados para exportação

## 🛡️ Tratamento de Erros

### Validações Implementadas
- **Tipos de dados**: Conversão segura int/float
- **Valores vazios**: Verificação de strings não vazias
- **Índices**: Validação de posições em arrays
- **Campos**: Verificação de atributos válidos
- **Formato numérico**: Aceita vírgula e ponto decimal

### Mensagens de Feedback
- ✅ **Sucesso**: Confirmações de operações
- ⚠️ **Aviso**: Alertas para correções
- 📋 **Informação**: Dados listados formatados

## 🧪 Exemplos de Uso

### Cenário: Fazenda com Café e Soja

**Talhão de Café:**
```
Nome: Talhão Sul
Ruas: 25
Metros por rua: 80
Dose: 400 mL/m
Comprimento: 200m
Largura: 150m

→ Área: 30.000 m²
→ Insumos: 800 litros
```

**Talhão de Soja:**
```
Nome: Pivô Central 1
Ruas: 30
Metros por rua: 100
Dose: 350 mL/m
Raio: 75m

→ Área: 17.671 m²
→ Insumos: 1.050 litros
```

## 📊 Relatórios e Análises

### Saída do Programa Python
```
=== Lista de talhões (cafe) ===
[0] Talhão=Sul, Área=30000.00 m², Litros=800.00 L
[1] Talhão=Norte, Área=25000.00 m², Litros=600.00 L
```

### Saída das Análises R
```r
  area_m2_media area_m2_desvio ruas_media ruas_desvio litros_media litros_desvio
1      22500.5       3535.534       20.5    3.535534        650.5      141.4214
```

---

# FarmTech Solutions - Monitor Meteorológico

Sistema de monitoramento meteorológico para agricultura digital, desenvolvido em R com integração à API do OpenWeatherMap.

## 🚀 Configuração

### 1. Pré-requisitos
- R instalado (versão 4.0 ou superior)
- Bibliotecas R necessárias: `httr`, `jsonlite`, `dplyr`

### 2. Instalação das bibliotecas
```r
install.packages(c("httr", "jsonlite", "dplyr"))
```

### 3. Configuração da API Key

1. **Obtenha uma API key gratuita:**
   - Acesse: https://openweathermap.org/api
   - Crie uma conta gratuita
   - Obtenha sua API key

2. **Configure o arquivo .env:**
   ```bash
   # Copie o arquivo de exemplo
   cp .env.example .env
   
   # Edite o arquivo .env e adicione sua API key
   API_KEY=sua_api_key_aqui
   ```

## 📊 Como usar

### Execução básica
```bash
Rscript --vanilla clima_api.R
```

### Execução com cidade específica
```bash
echo "Rio de Janeiro" | Rscript --vanilla clima_api.R
echo "Salvador" | Rscript --vanilla clima_api.R
echo "Brasilia" | Rscript --vanilla clima_api.R
```

**Dica**: Para cidades com acentos, use a grafia sem acentos (ex: "Brasilia" ao invés de "Brasília")

## 🌟 Funcionalidades

- **Condições meteorológicas atuais**: Temperatura, umidade, pressão, vento
- **Previsão de 5 dias**: Tendências meteorológicas
- **Análise agrícola**: Recomendações baseadas nas condições climáticas
- **Interface amigável**: Saída formatada com emojis e cores

## 📁 Estrutura de arquivos

```
├── clima_api.R          # Script principal
├── .env                 # Configurações (não commitado)
├── .env.example         # Template de configuração
├── .gitignore           # Arquivos ignorados pelo Git
└── README.md            # Este arquivo
```

## 🔒 Segurança

- O arquivo `.env` contém informações sensíveis e **não deve ser commitado**
- Use o arquivo `.env.example` como template
- Mantenha sua API key privada

## 🌾 Análise Agrícola

O sistema fornece análises específicas para agricultura:

- **Temperatura ideal**: 18-28°C para a maioria das culturas
- **Umidade recomendada**: 60-80% para desenvolvimento ótimo
- **Alertas**: Geada, estresse térmico, risco de doenças fúngicas
- **Tendências**: Previsões para planejamento agrícola

## 🐛 Solução de problemas

### Erro: "API Key não configurada"
- Verifique se o arquivo `.env` existe
- Confirme se a API_KEY está definida corretamente

### Erro: "Bibliotecas não encontradas"
- Execute: `install.packages(c("httr", "jsonlite", "dplyr"))`

### Erro: "Rscript não reconhecido"
- Instale o R: https://cran.r-project.org/
- Adicione o R ao PATH do sistema

---

## 📜 Licença

Este projeto foi desenvolvido para fins educacionais como parte do curso da FIAP.

---

🌱 **FarmTech Solutions** - Inovando a agricultura com tecnologia!
