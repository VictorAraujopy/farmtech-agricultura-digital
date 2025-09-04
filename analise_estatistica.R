suppressPackageStartupMessages(library(dplyr))

# Ler os dados do CSV (ajuste se o path for diferente)
dados <- read.csv("dados.csv", header = TRUE, sep = ",", dec = ".")

# Calcular estatísticas direto em todas as colunas numéricas
estatisticas <- dados %>%
  summarise(
    across(
      where(is.numeric),
      list(
        media  = ~mean(.x, na.rm = TRUE),
        desvio = ~sd(.x,   na.rm = TRUE),
        minimo = ~min(.x,  na.rm = TRUE),
        maximo = ~max(.x,  na.rm = TRUE)
      ),
      .names = "{.col}_{.fn}"
    )
  )

# Mostrar resultado
print(estatisticas)


