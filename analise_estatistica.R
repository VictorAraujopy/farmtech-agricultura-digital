#Carregar a library
library(dplyr)

#Ler os dados do arquivo CSV
dados <- read.csv("dados.csv", header = TRUE, sep = ",", dec = ".")

#Selecionar apenas as colunas numéricas do dataset
dados_numericos <- dados %>% select(where(is.numeric))

#Calcular estatísticas básicas (média, desvio, mínimo, máximo)
estatisticas <- dados_numericos %>%
  summarise_all(list(
    media = mean,
    desvio = sd,
    minimo = min,
    maximo = max
  ), na.rm = TRUE)  # 'na.rm = TRUE' ignora valores faltantes (NA)

#Mostrar o resultado
print(estatisticas)