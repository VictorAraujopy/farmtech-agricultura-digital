@echo off
REM Script para executar a análise estatística dos dados
REM Certifique-se de que o arquivo dados.csv existe na raiz do projeto

cd rscript
Rscript --vanilla analise_estatistica.R
cd ..