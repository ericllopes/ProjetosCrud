# LISTA DE CONTROLES

controles = []

while True:

    print("\n===== CONTROLE REMOTO =====")
    print("1 - Cadastrar controle")
    print("2 - Ver controles")
    print("3 - Atualizar controle")
    print("4 - Excluir controle")
    print("5 - Usar controle")
    print("0 - Sair")

    opcao = input("\nEscolha uma ação: ")

    match opcao:

        # CRIAR

        case "1":
            marca = input("Digite a marca: ")
            tipo = input("Digite o tipo: ")

            controle = {
                "marca": marca,
                "tipo": tipo,
                "volume": 10,
                "canal": 1,
                "ligado": False
            }

            controles.append(controle)

            print("Controle cadastrado!")

        # VISUALIZAR

        case "2":
            if len(controles) > 0:

                print("\n--- CONTROLES CADASTRADOS ---")

                for i in range(len(controles)):
                    print("\nControle", i + 1)
                    print("Marca:", controles[i]["marca"])
                    print("Tipo:", controles[i]["tipo"])
                    print("Volume:", controles[i]["volume"])
                    print("Canal:", controles[i]["canal"])
                    print("Status:", controles[i]["ligado"])

            else:
                print("Nenhum controle cadastrado!")

        # ATUALIZAR

        case "3":
            if len(controles) > 0:

                print("\n--- CONTROLES CADASTRADOS ---")

                for i in range(len(controles)):
                    print(i + 1, "-", controles[i]["marca"])

                numero = int(input("\nEscolha o controle que deseja atualizar: "))

                if numero >= 1 and numero <= len(controles):

                    indice = numero - 1

                    controles[indice]["marca"] = input("Digite a nova marca: ")
                    controles[indice]["tipo"] = input("Digite o novo tipo: ")

                    print("Controle atualizado!")

                else:
                    print("Controle inválido!")

            else:
                print("Nenhum controle cadastrado!")

        # DELETAR

        case "4":
            if len(controles) > 0:

                print("\n--- CONTROLES CADASTRADOS ---")

                for i in range(len(controles)):
                    print(i + 1, "-", controles[i]["marca"])

                numero = int(input("\nEscolha o controle que deseja excluir: "))

                if numero >= 1 and numero <= len(controles):

                    indice = numero - 1

                    controles.pop(indice)

                    print("Controle excluído!")

                else:
                    print("Controle inválido!")

            else:
                print("Nenhum controle cadastrado!")

        # UTILIZAR CONTROLE

        case "5":
            if len(controles) > 0:

                print("\n--- CONTROLES CADASTRADOS ---")

                for i in range(len(controles)):
                    print(i + 1, "-", controles[i]["marca"])

                numero = int(input("\nEscolha o controle que deseja utilizar: "))

                if numero >= 1 and numero <= len(controles):

                    indice = numero - 1

                    while True:

                        print("\n===== FUNÇÕES DO CONTROLE =====")
                        print("1 - Ligar/Desligar")
                        print("2 - Aumentar volume")
                        print("3 - Diminuir volume")
                        print("4 - Próximo canal")
                        print("5 - Canal anterior")
                        print("0 - Voltar")

                        comando = input("Escolha: ")

                        match comando:

                            case "1": # LIGA E DESLIGA A TV
                                controles[indice]["ligado"] = not controles[indice]["ligado"]

                                if controles[indice]["ligado"] == True:
                                    print("Estado da TV: ligado")
                                else:
                                    print("Estado da TV: desligado")

                            case "2": # AUMENTA O VOLUME EM 10
                                if controles[indice]["ligado"] == True:
                                    if controles[indice]["volume"] < 100:
                                        controles[indice]["volume"] += 10

                                    print("Volume:", controles[indice]["volume"])
                                else:
                                    print("A TV está desligada!")

                            case "3": # DIMINUI O VOLUME EM 10
                                if controles[indice]["ligado"] == True:
                                    if controles[indice]["volume"] > 0:
                                        controles[indice]["volume"] -= 10

                                    print("Volume:", controles[indice]["volume"])
                                else:
                                    print("A TV está desligada!")

                            case "4": # AUMENTA O CANAL EM 1
                                if controles[indice]["ligado"] == True:
                                    controles[indice]["canal"] += 1

                                    print("Canal:", controles[indice]["canal"])
                                else:
                                    print("A TV está desligada!")

                            case "5": # DIMINUI O CANAL EM 1
                                if controles[indice]["ligado"] == True:
                                    if controles[indice]["canal"] > 1:
                                        controles[indice]["canal"] -= 1

                                    print("Canal:", controles[indice]["canal"])
                                else:
                                    print("A TV está desligada!")

                            case "0":
                                break

                            case _:
                                print("Opção inválida!")

                else:
                    print("Controle inválido!")

            else:
                print("Nenhum controle cadastrado!")

        case "0":
            print("Saindo do programa...")
            break

        case _:
            print("Opção inválida!")
