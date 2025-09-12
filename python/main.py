from ui import (
    menu,
    escolher_cultura,
    inserir_registro,
    listar_registros,
    atualizar_registro,
    deletar_registro,
    exportar_csv,
)


def loop():
    while True:
        op = menu()
        if op == "1":
            inserir_registro(escolher_cultura())
        elif op == "2":
            listar_registros(escolher_cultura())
        elif op == "3":
            atualizar_registro(escolher_cultura())
        elif op == "4":
            deletar_registro(escolher_cultura())
        elif op == "5":
            exportar_csv()
        elif op == "0":
            print("Até mais!")  # Sai do loop e encerra o programa.
            break
        else:
            print("⚠️ Opção inválida.")   # Blindagem extra (não deve acontecer por causa do menu())


if __name__ == "__main__":
    """Ponto de entrada: se o arquivo for executado diretamente (e não importado), inicia o app.
    O loop() só termina quando o usuário escolhe "0" no menu.
    """
    loop()