# ==========================================================
# FUNÇÃO PARA CADASTRAR UM OBJETO
# ==========================================================

def cadastrar_item(itens):
    # Mostra o título da tela de cadastro.
    print("\n--- CADASTRO DE OBJETO ---")

    # Solicita o nome do objeto.
    nome = input("Nome do objeto: ")

    # Solicita uma descrição do objeto.
    descricao = input("Descrição do objeto: ")

    # Solicita o local onde o objeto foi encontrado.
    local = input("Local onde foi encontrado: ")

    # Solicita a data em que o objeto foi registrado.
    data = input("Data do registro (dd/mm/aaaa): ")

    # Verifica se o nome ficou vazio.
    # strip() remove os espaços extras.
    if nome.strip() == "":
        print("\nO nome do objeto não pode ficar vazio.")
        return

    # Verifica se a descrição ficou vazia.
    if descricao.strip() == "":
        print("\nA descrição não pode ficar vazia.")
        return

    # Verifica se o local ficou vazio.
    if local.strip() == "":
        print("\nO local não pode ficar vazio.")
        return

    # Verifica se a data ficou vazia.
    if data.strip() == "":
        print("\nA data não pode ficar vazia.")
        return

    # Cria um dicionário com os dados do objeto.
    item = {
        "nome": nome,
        "descricao": descricao,
        "local": local,
        "data": data
    }

    # Adiciona o objeto à lista.
    itens.append(item)

    print("\nObjeto cadastrado com sucesso!")


# ==========================================================
# FUNÇÃO PARA MOSTRAR O MENU
# ==========================================================

def mostrar_menu():
    print("\n================================")
    print(" ACHADOS E PERDIDOS DA ESCOLA")
    print("================================")
    print("1 - Cadastrar objeto")
    print("2 - Listar objetos")
    print("3 - Excluir objeto")
    print("4 - Sair")


# ==========================================================
# FUNÇÃO PRINCIPAL
# ==========================================================

def main():

    # Lista que armazenará os objetos cadastrados.
    itens = []

    # Mantém o sistema funcionando.
    while True:

        mostrar_menu()

        opcao = input("\nEscolha uma opção: ")

        # Cadastrar objeto
        if opcao == "1":
            cadastrar_item(itens)

        # Listar objetos
        elif opcao == "2":
            print("\n--- OBJETOS CADASTRADOS ---")

            if len(itens) == 0:
                print("Nenhum objeto cadastrado.")

            else:
                for item in itens:
                    print(item)

        # Excluir objeto
        elif opcao == "3":
            print("\nA exclusão será criada em outra aula.")

        # Sair
        elif opcao == "4":
            print("\nPrograma encerrado.")
            break

        # Opção inválida
        else:
            print("\nOpção inválida. Digite 1, 2, 3 ou 4.")


# ==========================================================
# INÍCIO DO PROGRAMA
# ==========================
main()
