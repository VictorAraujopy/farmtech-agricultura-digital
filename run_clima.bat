@echo off
REM Script para executar o sistema de clima meteorológico
REM Uso: run_clima.bat [cidade]
REM Exemplo: run_clima.bat "Rio de Janeiro"

cd rscript
if "%1"=="" (
    Rscript --vanilla clima_api.R
) else (
    echo %1 | Rscript --vanilla clima_api.R
)
cd ..