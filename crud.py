
# LISTA QUE ARMAZENA TODOS OS CONTROLES
controles = []

# CONTADOR PARA GERAR IDs
proximo_id = 1

while True:

    print("\n===== CONTROLE REMOTO =====")
    print("1 - Cadastrar controle")
    print("2 - Ver controles")
    print("3 - Atualizar controle")
    print("4 - Excluir controle")
    print("5 - Usar controle")
    print("0 - Sair")

    opcao = input("\nEscolha uma ação: ")

    # CRIAR
    if opcao == "1":

        marca = input("Digite a marca: ")
        tipo = input("Digite o tipo: ")

        # CRIA UM DICIONÁRIO COM OS DADOS DO CONTROLE
        controle = {
            "id": proximo_id,
            "marca": marca,
            "tipo": tipo,
            "volume": 10,
            "canal": 1,
            "ligado": False
        }

        # ADICIONA O DICIONÁRIO NA LISTA
        controles.append(controle)

        print("Controle cadastrado com sucesso!")
        print("ID do controle:", proximo_id)

        proximo_id += 1

    # VISUALIZAR
    elif opcao == "2":

        if len(controles) > 0:

            print("\n--- CONTROLES CADASTRADOS ---")

            for controle in controles:

                print("\nID:", controle["id"])
                print("Marca:", controle["marca"])
                print("Tipo:", controle["tipo"])
                print("Volume:", controle["volume"])
                print("Canal:", controle["canal"])
                print("Status:", "Ligada" if controle["ligado"] else "Desligada")

        else:
            print("Nenhum controle cadastrado!")

    # ATUALIZAR
    elif opcao == "3":

        if len(controles) > 0:

            id_busca = int(input("Digite o ID do controle: "))

            encontrado = False

            for controle in controles:

                if controle["id"] == id_busca:

                    controle["marca"] = input("Digite a nova marca: ")
                    controle["tipo"] = input("Digite o novo tipo: ")

                    print("Controle atualizado!")
                    encontrado = True
                    break

            if encontrado == False:
                print("ID não encontrado!")

        else:
            print("Nenhum controle cadastrado!")

    # DELETAR
    elif opcao == "4":

        if len(controles) > 0:

            id_busca = int(input("Digite o ID do controle: "))

            encontrado = False

            for controle in controles:

                if controle["id"] == id_busca:

                    controles.remove(controle)

                    print("Controle excluído!")
                    encontrado = True
                    break

            if encontrado == False:
                print("ID não encontrado!")

        else:
            print("Nenhum controle cadastrado!")

    # UTILIZAR CONTROLE
    elif opcao == "5":

        if len(controles) > 0:

            id_busca = int(input("Digite o ID do controle que deseja utilizar: "))

            controle_selecionado = None

            for controle in controles:

                if controle["id"] == id_busca:
                    controle_selecionado = controle
                    break

            if controle_selecionado != None:

                while True:

                    print("\n===== FUNÇÕES DO CONTROLE =====")
                    print("1 - Ligar/Desligar")
                    print("2 - Aumentar volume")
                    print("3 - Diminuir volume")
                    print("4 - Próximo canal")
                    print("5 - Canal anterior")
                    print("0 - Voltar")

                    comando = input("Escolha: ")

                    if comando == "1":

                        controle_selecionado["ligado"] = not controle_selecionado["ligado"]

                        print("Estado da TV:", controle_selecionado["ligado"])

                    elif comando == "2":

                        if controle_selecionado["ligado"] == True:

                            if controle_selecionado["volume"] < 100:
                                controle_selecionado["volume"] += 10

                            print("Volume:", controle_selecionado["volume"])

                        else:
                            print("A TV está desligada!")

                    elif comando == "3":

                        if controle_selecionado["ligado"] == True:

                            if controle_selecionado["volume"] > 0:
                                controle_selecionado["volume"] -= 10

                            print("Volume:", controle_selecionado["volume"])

                        else:
                            print("A TV está desligada!")

                    elif comando == "4":

                        if controle_selecionado["ligado"] == True:

                            controle_selecionado["canal"] += 1

                            print("Canal:", controle_selecionado["canal"])

                        else:
                            print("A TV está desligada!")

                    elif comando == "5":

                        if controle_selecionado["ligado"] == True:

                            if controle_selecionado["canal"] > 1:
                                controle_selecionado["canal"] -= 1

                            print("Canal:", controle_selecionado["canal"])

                        else:
                            print("A TV está desligada!")

                    elif comando == "0":
                        break

                    else:
                        print("Comando inválido!")

            else:
                print("ID não encontrado!")

        else:
            print("Cadastre um controle primeiro!")

    # SAIR
    elif opcao == "0":

        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida!")
