# ========================================================
# FarmTech Solutions - Integração com API Meteorológica
# ========================================================
# Script R para coletar dados climáticos via API pública
# e exibir informações processadas no terminal

# Carregar bibliotecas necessárias
suppressPackageStartupMessages({
  library(httr)      # Para requisições HTTP
  library(jsonlite)  # Para processar JSON
  library(dplyr)     # Para manipulação de dados
})

# Função para carregar variáveis do arquivo .env
carregar_env <- function(arquivo = ".env") {
  if (!file.exists(arquivo)) {
    cat("❌ Arquivo .env não encontrado!\n")
    cat("📋 Crie um arquivo .env com sua API_KEY:\n")
    cat("   API_KEY=sua_chave_aqui\n\n")
    return(FALSE)
  }
  
  # Ler linhas do arquivo .env
  linhas <- readLines(arquivo, warn = FALSE)
  
  # Processar cada linha
  for (linha in linhas) {
    # Ignorar comentários e linhas vazias
    linha <- trimws(linha)
    if (nchar(linha) == 0 || startsWith(linha, "#")) {
      next
    }
    
    # Separar chave=valor
    if (grepl("=", linha)) {
      partes <- strsplit(linha, "=", fixed = TRUE)[[1]]
      if (length(partes) >= 2) {
        chave <- trimws(partes[1])
        valor <- trimws(paste(partes[2:length(partes)], collapse = "="))
        
        # Remover aspas se existirem
        valor <- gsub('^["\']|["\']$', '', valor)
        
        # Definir variável de ambiente
        do.call(Sys.setenv, setNames(list(valor), chave))
      }
    }
  }
  
  return(TRUE)
}

# Carregar configurações do arquivo .env
if (!carregar_env()) {
  stop("Não foi possível carregar as configurações do arquivo .env")
}

# Configurações da API
API_KEY <- Sys.getenv("API_KEY")
BASE_URL <- "http://api.openweathermap.org/data/2.5"

# Função para obter dados meteorológicos atuais
obter_clima_atual <- function(cidade, pais = "BR") {
  cat("🌤️  Buscando dados meteorológicos...\n")
  
  # Construir URL da requisição
  url <- paste0(
    BASE_URL, "/weather",
    "?q=", URLencode(paste(cidade, pais, sep = ",")),
    "&appid=", API_KEY,
    "&units=metric",  # Celsius, km/h, etc.
    "&lang=pt"        # Português
  )
  print(url)
  tryCatch({
    # Fazer requisição HTTP
    resposta <- GET(url)
    
    # Verificar se a requisição foi bem-sucedida
    if (status_code(resposta) != 200) {
      stop("Erro na API: ", status_code(resposta))
    }
    
    # Converter resposta JSON para lista R
    dados <- fromJSON(content(resposta, "text", encoding = "UTF-8"))
    
    return(dados)
    
  }, error = function(e) {
    cat("❌ Erro ao obter dados meteorológicos:\n")
    cat("   ", conditionMessage(e), "\n")
    return(NULL)
  })
}

# Função para obter previsão de 5 dias
obter_previsao_5dias <- function(cidade, pais = "BR") {
  cat("📅 Buscando previsão de 5 dias...\n")
  
  url <- paste0(
    BASE_URL, "/forecast",
    "?q=", URLencode(paste(cidade, pais, sep = ",")),
    "&appid=", API_KEY,
    "&units=metric",
    "&lang=pt"
  )
  
  tryCatch({
    resposta <- GET(url)
    
    if (status_code(resposta) != 200) {
      stop("Erro na API: ", status_code(resposta))
    }
    
    dados <- fromJSON(content(resposta, "text", encoding = "UTF-8"))
    return(dados)
    
  }, error = function(e) {
    cat("❌ Erro ao obter previsão:\n")
    cat("   ", conditionMessage(e), "\n")
    return(NULL)
  })
}

# Função para formatar e exibir dados climáticos atuais
exibir_clima_atual <- function(dados) {
  if (is.null(dados)) {
    cat("❌ Dados não disponíveis\n")
    return()
  }
  
  cat("\n" , rep("=", 50), sep="")
  cat("\n🌍 CONDIÇÕES METEOROLÓGICAS ATUAIS")
  cat("\n" , rep("=", 50), sep="")
  
  # Informações básicas
  cat("\n📍 Localização:", dados$name, ",", dados$sys$country)
  cat("\n🕐 Atualizado em:", as.POSIXct(dados$dt, origin = "1970-01-01", tz = "America/Sao_Paulo"))
  
  # Condições gerais
  cat("\n\n☁️  CONDIÇÕES GERAIS:")
  if (!is.null(dados$weather) && length(dados$weather) > 0) {
    if (is.list(dados$weather[[1]])) {
      cat("\n   Tempo:", dados$weather[[1]]$description)
    } else {
      cat("\n   Tempo:", "Informação não disponível")
    }
  } else {
    cat("\n   Tempo:", "Informação não disponível")
  }
  
  if (!is.null(dados$visibility)) {
    cat("\n   Visibilidade:", round(dados$visibility / 1000, 1), "km")
  }
  
  # Temperatura
  cat("\n\n🌡️  TEMPERATURA:")
  cat("\n   Atual:", round(dados$main$temp, 1), "°C")
  cat("\n   Sensação térmica:", round(dados$main$feels_like, 1), "°C")
  cat("\n   Mínima:", round(dados$main$temp_min, 1), "°C")
  cat("\n   Máxima:", round(dados$main$temp_max, 1), "°C")
  
  # Umidade e pressão
  cat("\n\n💧 UMIDADE E PRESSÃO:")
  cat("\n   Umidade relativa:", dados$main$humidity, "%")
  cat("\n   Pressão atmosférica:", dados$main$pressure, "hPa")
  
  # Vento
  cat("\n\n💨 VENTO:")
  if (!is.null(dados$wind$speed)) {
    cat("\n   Velocidade:", round(dados$wind$speed * 3.6, 1), "km/h")  # m/s para km/h
  }
  if (!is.null(dados$wind$deg)) {
    cat("\n   Direção:", dados$wind$deg, "° (", obter_direcao_vento(dados$wind$deg), ")")
  }
  if (!is.null(dados$wind$gust)) {
    cat("\n   Rajadas:", round(dados$wind$gust * 3.6, 1), "km/h")
  }
  
  # Sol
  cat("\n\n☀️  SOL:")
  nascer <- as.POSIXct(dados$sys$sunrise, origin = "1970-01-01", tz = "America/Sao_Paulo")
  por <- as.POSIXct(dados$sys$sunset, origin = "1970-01-01", tz = "America/Sao_Paulo")
  cat("\n   Nascer do sol:", format(nascer, "%H:%M"))
  cat("\n   Pôr do sol:", format(por, "%H:%M"))
  
  # Chuva (se houver)
  if (!is.null(dados$rain)) {
    cat("\n\n🌧️  PRECIPITAÇÃO:")
    if (!is.null(dados$rain$`1h`) && !is.na(dados$rain$`1h`)) {
      cat("\n   Última hora:", dados$rain$`1h`, "mm")
    }
    if (!is.null(dados$rain$`3h`) && !is.na(dados$rain$`3h`)) {
      cat("\n   Últimas 3h:", dados$rain$`3h`, "mm")
    }
  }
  
  cat("\n", rep("=", 50), "\n")
}

# Função auxiliar para converter graus em direção do vento
obter_direcao_vento <- function(graus) {
  direcoes <- c("N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                "S", "SSO", "SO", "OSO", "O", "ONO", "NO", "NNO")
  index <- round((graus %% 360) / 22.5) + 1
  if (index > 16) index <- 1
  return(direcoes[index])
}

# Função para processar e exibir previsão resumida
exibir_previsao_resumida <- function(dados) {
  if (is.null(dados)) {
    cat("❌ Dados de previsão não disponíveis\n")
    return()
  }
  
  cat("\n" , rep("=", 60), sep="")
  cat("\n📅 PREVISÃO METEOROLÓGICA - 5 DIAS")
  cat("\n" , rep("=", 60), sep="")
  
  # Processar dados da previsão (pegar um ponto por dia ao meio-dia)
  previsoes <- dados$list
  
  # Converter timestamp para data
  previsoes$data <- as.POSIXct(previsoes$dt, origin = "1970-01-01", tz = "America/Sao_Paulo")
  previsoes$dia <- format(previsoes$data, "%Y-%m-%d")
  
  # Selecionar previsão do meio-dia (12:00) para cada dia
  previsao_diaria <- previsoes %>%
    group_by(dia) %>%
    filter(format(data, "%H") == "12" | row_number() == 1) %>%  # Preferencialmente meio-dia
    slice_head(n = 1) %>%
    ungroup() %>%
    slice_head(n = 5)  # Máximo 5 dias
  
  for (i in 1:nrow(previsao_diaria)) {
    linha <- previsao_diaria[i, ]
    
    cat("\n\n📆", format(linha$data, "%A, %d/%m"))
    
    # Verificar estrutura do weather
    if (!is.null(linha$weather) && length(linha$weather) > 0) {
      if (is.list(linha$weather[[1]])) {
        cat("\n   🌤️ ", linha$weather[[1]]$description)
      } else {
        cat("\n   🌤️ ", "Informação não disponível")
      }
    } else {
      cat("\n   🌤️ ", "Informação não disponível")
    }
    
    cat("\n   🌡️ ", round(linha$main$temp, 1), "°C")
    cat("  (", round(linha$main$temp_min, 1), "° - ", round(linha$main$temp_max, 1), "°)", sep="")
    cat("\n   💧 Umidade:", linha$main$humidity, "%")
    if (!is.null(linha$wind$speed)) {
      cat("\n   💨 Vento:", round(linha$wind$speed * 3.6, 1), "km/h")
    }
    if (!is.null(linha$rain) && !is.null(linha$rain$`3h`) && !is.na(linha$rain$`3h`) && linha$rain$`3h` > 0) {
      cat("\n   🌧️  Chuva:", linha$rain$`3h`, "mm")
    }
  }
  
  cat("\n", rep("=", 60), "\n")
}

# Função para calcular estatísticas agrícolas
calcular_stats_agricolas <- function(dados_atuais, dados_previsao) {
  cat("\n" , rep("=", 60), sep="")
  cat("\n🌾 ANÁLISE PARA AGRICULTURA")
  cat("\n" , rep("=", 60), sep="")
  
  if (!is.null(dados_atuais)) {
    temp_atual <- dados_atuais$main$temp
    umidade_atual <- dados_atuais$main$humidity
    
    cat("\n📊 CONDIÇÕES ATUAIS PARA CULTIVO:")
    
    # Análise de temperatura
    if (temp_atual >= 18 && temp_atual <= 28) {
      cat("\n   ✅ Temperatura IDEAL para a maioria das culturas (18-28°C)")
    } else if (temp_atual < 10) {
      cat("\n   ❄️  Temperatura BAIXA - risco de geada")
    } else if (temp_atual > 35) {
      cat("\n   🔥 Temperatura ALTA - estresse térmico possível")
    } else {
      cat("\n   ⚠️  Temperatura MODERADA - monitorar culturas sensíveis")
    }
    
    # Análise de umidade
    if (umidade_atual >= 60 && umidade_atual <= 80) {
      cat("\n   ✅ Umidade IDEAL para desenvolvimento das plantas")
    } else if (umidade_atual < 40) {
      cat("\n   🏜️  Umidade BAIXA - considerar irrigação")
    } else if (umidade_atual > 90) {
      cat("\n   🍄 Umidade ALTA - risco de doenças fúngicas")
    }
  }
  
  if (!is.null(dados_previsao)) {
    previsoes <- dados_previsao$list
    
    # Calcular médias dos próximos dias
    n_items <- min(8, nrow(previsoes))
    temps <- numeric(n_items)
    umidades <- numeric(n_items)
    
    for (i in 1:n_items) {
      temps[i] <- previsoes[i, ]$main$temp
      umidades[i] <- previsoes[i, ]$main$humidity
    }
    
    cat("\n\n📈 TENDÊNCIA (PRÓXIMAS 24H):")
    cat("\n   🌡️  Temperatura média:", round(mean(temps), 1), "°C")
    cat("\n   💧 Umidade média:", round(mean(umidades)), "%")
    
    # Verificar se há previsão de chuva
    chuva_total <- 0
    for (i in 1:min(8, nrow(previsoes))) {
      item <- previsoes[i, ]
      if (!is.null(item$rain) && !is.null(item$rain$`3h`) && !is.na(item$rain$`3h`)) {
        chuva_total <- chuva_total + item$rain$`3h`
      }
    }
    
    if (chuva_total > 0) {
      cat("\n   🌧️  Precipitação prevista:", round(chuva_total, 1), "mm")
      if (chuva_total > 20) {
        cat("\n   ⚠️  ATENÇÃO: Chuva intensa prevista")
      }
    } else {
      cat("\n   ☀️  Sem previsão de chuva nas próximas 24h")
    }
  }
  
  cat("\n", rep("=", 60), "\n")
}

# Função principal
main <- function() {
  cat("🌱 FarmTech Solutions - Monitor Meteorológico\n")
  cat("===========================================\n")
  
  # Verificar se API key foi configurada
  if (API_KEY == "" || is.na(API_KEY)) {
    cat("❌ ERRO: API Key não configurada!\n")
    cat("\n📋 Para usar este script:\n")
    cat("1. Acesse: https://openweathermap.org/api\n")
    cat("2. Crie uma conta gratuita\n")
    cat("3. Obtenha sua API key\n")
    cat("4. Adicione no arquivo .env: API_KEY=sua_chave_aqui\n\n")
    return()
  }
  
  # Solicitar cidade (com padrão)
  cat("\n🌍 Digite a cidade (ou ENTER para São Paulo): ")
  
  # Tentar ler da entrada padrão (funciona com pipes)
  tryCatch({
    cidade <- readLines("stdin", n = 1, warn = FALSE)
    if (length(cidade) == 0 || cidade == "" || is.na(cidade)) {
      cidade <- "São Paulo"
    }
  }, error = function(e) {
    # Se falhar, tentar readline (modo interativo)
    cidade <- readline()
    if (cidade == "" || is.na(cidade)) {
      cidade <- "São Paulo"
    }
  })
  
  # Limpar entrada e tratar codificação
  cidade <- trimws(cidade)
  
  # Converter codificação se necessário (Windows)
  if (.Platform$OS.type == "windows") {
    tryCatch({
      cidade <- iconv(cidade, from = "latin1", to = "UTF-8")
    }, error = function(e) {
      # Se falhar, manter original
    })
  }
  
  cat("\n🔍 Processando dados para:", cidade, "\n")
  
  # Obter dados meteorológicos
  clima_atual <- obter_clima_atual(cidade)
  previsao <- obter_previsao_5dias(cidade)
  
  # Exibir resultados
  exibir_clima_atual(clima_atual)
  exibir_previsao_resumida(previsao)
  calcular_stats_agricolas(clima_atual, previsao)
  
  cat("✅ Consulta meteorológica concluída!\n")
  cat("📊 Use estes dados para otimizar suas atividades agrícolas.\n\n")
}

# Verificar se as bibliotecas estão instaladas
verificar_bibliotecas <- function() {
  bibliotecas <- c("httr", "jsonlite", "dplyr")
  faltando <- bibliotecas[!bibliotecas %in% installed.packages()[,"Package"]]
  
  if (length(faltando) > 0) {
    cat("❌ Bibliotecas não encontradas:", paste(faltando, collapse = ", "), "\n")
    cat("📦 Para instalar, execute:\n")
    cat("   install.packages(c('", paste(faltando, collapse = "', '"), "'))\n\n", sep = "")
    return(FALSE)
  }
  
  return(TRUE)
}

# Executar programa principal
if (verificar_bibliotecas()) {
  main()
} else {
  cat("⚠️  Instale as bibliotecas necessárias antes de continuar.\n")
}
