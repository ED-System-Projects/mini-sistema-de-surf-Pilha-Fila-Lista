class PilhaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class PilhaEncadeada():
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0

    def topo(self):
        if self.vazia():
            raise PilhaException('A pilha está vazia')

        return self.__topo

    def vazia(self):
        return self.__tamanho == 0

    def tamanho(self):
        return self.__tamanho

    def inserir(self, novo_surfista):
        novo_surfista.set_prox(self.__topo)
        # colocar o topo no prox do objeto passado como paramentro
        # nesse caso o prox do surfista
        self.__topo = novo_surfista
        # atribui o objeto atual ao topo, nesse caso, atribui o objeto surfista
        # ao topo da pilha

        self.__tamanho += 1

    def remover(self):
        if self.vazia():
            raise PilhaException('A pilha está vazia')

        self.__topo = self.__topo.get_prox()
        self.__tamanho -= 1

    def __str__(self):
        saida = 'Pilha: ['
        p = self.__topo

        while p != None:
            saida += f'{p.get_nome()},{p.get_titulos()},{p.get_idade(),p.get_cpf()}'
            p = p.get_prox()

            if p != None:
                saida += ', '

        saida += ']'
        return saida

    def imprimir(self):
        print(self.__str__())
