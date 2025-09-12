#!/usr/bin/env python3
"""
Script de execução para o sistema FarmTech em Python
Executa o programa principal mantendo compatibilidade com a estrutura de pastas
"""

import sys
import os

# Adicionar a pasta python ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'python'))

# Importar e executar o loop principal
from main import loop

if __name__ == "__main__":
    loop()