from surfista import Surfista
from pilha import PilhaEncadeada
from lista import ListaEncadeada
from fila import FilaEncadeada
from campeonato import Campeonato

if __name__ == "__main__":

    # criando objetos surfista
    surfista1 = Surfista("Stephanie Gilmore", 2, 23, 95674)
    surfista2 = Surfista("Sally Fitzgibbons", 3, 26, 84562)
    surfista3 = Surfista("Brisa Hennessy", 1, 21, 34835)
    surfista4 = Surfista("Tatiana Weston", 4, 29, 36475)

    surfista5 = Surfista("Grant Baker", 1, 38, 82373)
    surfista6 = Surfista("Lucas Chianca", 3, 28, 27384)
    surfista7 = Surfista("Natxo Gonzalez", 2, 27, 27383)
    surfista8 = Surfista("Alex Botelho", 1, 31, 51865)

    surfista9 = Surfista("Connor O'Leary", 3, 26, 64316)
    surfista10 = Surfista("Matt Banting", 1, 35, 38715)
    surfista11 = Surfista("Owen Wright", 2, 45, 84724)
    surfista12 = Surfista("Ian Gentil", 5, 18, 48796)

    # criando objetos das estruturas de dados
    # surfistasL = ListaEncadeada()
    # surfistasP = PilhaEncadeada()
    # surfistasF = FilaEncadeada()

    campeonato1 = Campeonato("Pro Santa Cruz")

    campeonato1.adicionar_surfista_P(surfista5)
    campeonato1.adicionar_surfista_P(surfista6)
    campeonato1.adicionar_surfista_P(surfista7)
    campeonato1.adicionar_surfista_P(surfista8)

    campeonato1.adicionar_surfista_L(surfista1, 0)
    campeonato1.adicionar_surfista_L(surfista2, 1)
    campeonato1.adicionar_surfista_L(surfista3, 2)
    campeonato1.adicionar_surfista_L(surfista4, 3)

    campeonato1.adicionar_surfista_F(surfista9)
    campeonato1.adicionar_surfista_F(surfista10)
    campeonato1.adicionar_surfista_F(surfista11)
    campeonato1.adicionar_surfista_F(surfista12)

    # menu
    print("Seja bem-vindo ao sistema de surf! Escolha uma das opções abaixo:")

    while True:
        print("-"*62)
        print("[1] Consultar o Surfista mais jovem do Campeonato")
        print("[2] Consultar o Surfista mais velho do Campeonato")
        print("[3] Incrementar um novo título ao Surfista")
        print("[4] Remover Surfista da Pilha")
        print("[5] Remover Surfista da Lista")
        print("[6] Remover Surfista da Fila")
        print("[7] Buscar Surfista pelo CPF")
        print("[8] Exibir a Lista de Surfistas por ordem alfabética")
        print("[9] Mostrar lista de Surfistas com seus nomes e seus respectivos títulos")
        print("[10] Exibir o tamanho da Pilha da Surfistas")
        print("[11] Exibir o tamanho da Lista de Surfistas")
        print("[12] Exibir o tamanho da Fila da Surfistas:")

        print("-"*62)
        opcao_escolhida = input("Digite a opção desejada: ")
        print("-"*62)

        if opcao_escolhida == "1":
            print(f"Surfista mais jovem do Campeonato {campeonato1}:")
            print(campeonato1.menor_idade())

        elif opcao_escolhida == "2":
            print(f"Surfista mais velho do Campeonato {campeonato1}:")
            print(campeonato1.maior_idade())

        elif opcao_escolhida == "3":
            cpf = int(input("Digite o CPF do surfista que deseja incrementar um novo títulos:"))
            campeonato1.incrementa_titulo_surfista(cpf)

        elif opcao_escolhida == "4":
            print("Pilha atual:")
            campeonato1.surfistasP.imprimir()
            campeonato1.remover_surfista_P()
            print("Surfista removido da Pilha com sucesso!")
            print("Pilha após a remoção:")
            campeonato1.surfistasP.imprimir()

        elif opcao_escolhida == "5":
            print("Lista atual:")
            campeonato1.imprimir_surfistas()
            posicao = int(input("Digite a posição que deseja remover um surfista:"))
            campeonato1.remover_surfista_L(posicao)
            print("Surfista removido da Lista com sucesso!")
            print("Lista após a remoção:")
            campeonato1.imprimir_surfistas()

        elif opcao_escolhida == "6":
            print("Fila atual:")
            campeonato1.surfistasF.imprimir()
            campeonato1.remover_surfista_F()
            print("Surfista removido da Fila com sucesso!")
            print("Fila após a remoção:")
            campeonato1.surfistasF.imprimir()

        elif opcao_escolhida == "7":
            cpf = int(input("Digite o CPF do surfista que deseja:"))
            print(campeonato1.busca_surfista(cpf))

        elif opcao_escolhida == "8":
            campeonato1.ordena_surfistas()
            campeonato1.imprimir_surfistas()

        elif opcao_escolhida == "9":
            campeonato1.imprimir_surfistas()

        elif opcao_escolhida == "10":
            print(campeonato1.mostrar_tam_surfistasP())

        elif opcao_escolhida == "11":
            print(campeonato1.mostrar_tam_surfistasL())

        elif opcao_escolhida == "12":
            print(campeonato1.mostrar_tam_surfistasF())
        else:
          pass
