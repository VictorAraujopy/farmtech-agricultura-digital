"""Classe responsável pela interação no terminal com o usuário"""

import csv
from dataclasses import asdict
from repo import Repo
from models import TalhaoCafe, TalhaoSoja


repo = Repo()


# === Funções auxiliares de input seguro ===
def input_int(msg: str) -> int:
    while True:
        val = input(msg).strip()
        try:
            return int(val)
        except ValueError:
            print("⚠️ Digite um número inteiro válido.")


def input_float(msg: str) -> float:
    while True:
        val = input(msg).strip().replace(",", ".")  # aceita vírgula e troca para ponto posteriomente
        try:
            return float(val)
        except ValueError:
            print("⚠️ Digite um número válido (use ponto ou vírgula para decimais).")


def input_str(msg: str) -> str:
    while True:
        val = input(msg).strip()
        if val:
            return val
        print("⚠️ O valor não pode ser vazio.")


# === Funções de interface ===
def menu():
    """Exibe o menu de opções e só retorna quando a opção é válida."""
    print("\n===== MENU =====")
    print("1) Inserir")
    print("2) Listar")
    print("3) Atualizar")
    print("4) Deletar")
    print("5) Exportar CSV")
    print("0) Sair")
    return input("Escolha uma opção: ").strip()


def escolher_cultura():
    """Garante que o usuário digite apenas "cafe" ou "soja"."""
    while True:
        """.strip() remove espaços extras; 
        .lower() deixa tudo minúsculo para evitar erro por capitalização.
        """
        escolha = input("Qual cultura você quer operar? (cafe/soja): ").strip().lower()
        if escolha in ["cafe", "soja"]:
            return escolha
        print("⚠️ Digite apenas 'cafe' ou 'soja'.")


def inserir_registro(cultura_nome: str):
    # Coleta de dados gerais do talhão (iguais para qualquer cultura):
    nome_talhao = input_str("ID/Nome do talhão: ")
    ruas = input_int("Número de ruas: ")
    metros = input_float("Comprimento de cada rua (m): ")
    dose = input_float("Dose em mL por metro: ")

    # Dados específicos por cultura:
    if cultura_nome == "cafe":
        comprimento = input_float("Comprimento do talhão (m): ")
        largura = input_float("Largura do talhão (m): ")
        talhao = TalhaoCafe(nome_talhao, ruas, metros, dose, comprimento, largura)
        repo.cafe.adicionar(talhao)
    else:
        raio = input_float("Raio do talhão (m): ")
        talhao = TalhaoSoja(nome_talhao, ruas, metros, dose, raio)
        repo.soja.adicionar(talhao)

    print("✅ Talhão cadastrado com sucesso!")


def listar_registros(cultura_nome: str):
    repo.get(cultura_nome).listar(cultura_nome)


def atualizar_registro(cultura_nome: str):
    cultura = repo.get(cultura_nome)
    if not cultura.talhoes:
        print("⚠️ Nenhum talhão cadastrado para atualizar.")
        return

    try:
        """Tenta converter para inteiro (tratando erro de digitação).
        e pergunta qual índice o usuário quer alterar (posição na lista).
        """
        idx = input_int("Índice do talhão a alterar: ")
    except ValueError:
        print("⚠️ Índice inválido.")
        return

    # Confere se o índice existe (0 até tamanho-1).
    if idx < 0 or idx >= len(cultura.talhoes):
        print("Índice inválido.")
        return

    campos = list(asdict(cultura.talhoes[idx]).keys())
    print("Campos disponíveis para alterar: " + ", ".join(campos))

    campo = input("Qual campo alterar? ").strip().lower()
    if campo not in campos:
        print("⚠️ Campo inválido.")
        return

    novo_valor = input(f"Novo valor para '{campo}': ").strip()
    cultura.atualizar(idx, campo, novo_valor)


def deletar_registro(cultura_nome: str):
    cultura = repo.get(cultura_nome)
    if not cultura.talhoes:
        print("⚠️ Nenhum talhão cadastrado para deletar.")
        return

    try:
        """Tenta converter para inteiro (tratando erro de digitação).
        e pergunta qual índice o usuário quer alterar (posição na lista).
        """
        idx = int(input("Índice do talhão a deletar: "))
    except ValueError:
        print("⚠️ Índice inválido.")
        return

    cultura.deletar(idx)


def exportar_csv():
    caminho = "../dados.csv"  # Caminho do arquivo de saída (você pode mudar se quiser).
    rows = []  # Aqui vamos juntar todas as linhas a serem escritas no CSV.

    for cultura_nome, cultura in [("cafe", repo.cafe), ("soja", repo.soja)]:
        for t in cultura.talhoes:
            rows.append(t.to_row(cultura_nome))

    # Abrimos/criamos o CSV e escrevemos cabeçalho + linhas.
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["cultura", "talhao", "area_m2", "ruas", "metros_por_rua", "dose_ml_por_m", "litros"]
        )
        writer.writerows(rows)

    print(f"✔ Exportado para {caminho}")
    # Você pode abrir esse arquivo no Excel/Google Sheets para conferir.