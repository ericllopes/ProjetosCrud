# variaveis do controle remoto

marca = "" # armazena a marca do controle
tipo = "" # armazena o tipo de controle
volume = 10 # define o volume inicial da tv
canal = 1 # define o canal inicial da tv
ligado = False # indica se a tv esta ligada ou nao
cadastrado = False # indica se existe um controle ou nao

while True:

    print("\n===== CONTROLE REMOTO =====")
    print("1 - Cadastrar controle")
    print("2 - Ver controle")
    print("3 - Atualizar controle")
    print("4 - Excluir controle")
    print("5 - Usar controle")
    print("0 - Sair")

    opcao = input("\nEscolha uma ação:")

    # CRIAR

    if opcao == "1":

        if cadastrado == False:
            marca = input("Digite a marca: ")
            tipo = input("Digite o tipo: ")
            cadastrado = True

            print("Controle cadastrado!")

        else:
            print("Já existe um controle cadastrado")

    # VISUALIZAR

    elif opcao == "2":

        if cadastrado == True:
            print("\n--- INFORMAÇÕES DO CONTROLE ---")
            print("Marca:", marca)
            print("Tipo:", tipo)
            print("Volume:", volume)
            print("Canal:", canal)
            print("Status:", ligado)

        else:
            print("Nenhum controle cadastrado!")

    # ATUALIZAR

    elif opcao == "3":

        if cadastrado == True:
            marca = input("Digite a nova marca: ")
            modelo = input("Digite o novo tipo: ")

            print("Controle atualizado!")

        else:
            print("Nenhum controle cadastrado!")

    # DELETAR

    elif opcao == "4":

        if cadastrado == True:
            marca = ""
            modelo = ""
            volume = 10
            canal = 1
            ligado = False
            cadastrado = False

            print("Controle excluído!")

        else:
            print("Nenhum controle cadastrado!")

    # UTILIZAR CONTROLE
    elif opcao == "5":

        if cadastrado == True:

            while True:

                print("\n===== FUNÇÕES DO CONTROLE =====")
                print("1 - Ligar/Desligar")
                print("2 - Aumentar volume")
                print("3 - Diminuir volume")
                print("4 - Próximo canal")
                print("5 - Canal anterior")
                print("0 - Voltar")

                comando = input("Escolha: ")

                if comando == "1": # LIGA OU DESLIGA A TV
                    ligado = not ligado
                    print("Estado da TV:", ligado)

                elif comando == "2": # AUMENTA O VOLUME EM 10
                    if ligado == True:
                        if volume < 100:
                            volume += 10
                        print("Volume:", volume)
                    else:
                        print("A TV está desligada!")

                elif comando == "3": # DIMINUI O VOLUME EM 10 
                    if ligado == True:
                        if volume > 0:
                            volume -= 10
                        print("Volume:", volume)
                    else:
                        print("A TV está desligada!")

                elif comando == "4": # PASSA PARA O PROXIMO CANAL
                    if ligado == True:
                        canal += 1
                        print("Canal:", canal)
                    else:
                        print("A TV está desligada!")

                elif comando == "5": # VOLTA PRO CANAL ANTERIOR
                    if ligado == True:
                        if canal > 1:
                            canal -= 1
                        print("Canal:", canal)
                    else:
                        print("A TV está desligada!")

                elif comando == "0": # SAI DO MENU DO CONTROLE
                    break

                else:
                    print("Comando inválido!")

        else:
            print("Cadastre um controle primeiro!")

    # SAIR 

    elif opcao == "0": # ENCERRA
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida!")