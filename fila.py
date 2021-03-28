class FilaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class FilaEncadeada:
    def __init__(self):
        self.__inicio = None
        self.__tamanho = 0

    def inicio(self):
        if self.vazia():
            raise FilaException('A fila está vazia')

        return self.__inicio

    def vazia(self):
        return self.__tamanho == 0

    def tamanho(self):
        return self.__tamanho

    def inserir(self, novo_surfista):
        aux = self.__inicio

        if aux == None:
            self.__inicio = novo_surfista

        else:
            while aux.get_prox() != None:
                aux = aux.get_prox()

            aux.set_prox(novo_surfista)

        self.__tamanho += 1

    def remover(self):
        if self.vazia():
            raise FilaException('A fila está vazia')

        self.__inicio = self.__inicio.get_prox()
        self.__tamanho -= 1

    def mostrar_elemento(self):
        pass

    def __str__(self):
        saida = 'Fila: ['
        p = self.__inicio

        while p != None:
            saida += f'{p.get_nome()},{p.get_titulos()},{p.get_idade(),p.get_cpf()}'
            p = p.get_prox()

            if p != None:
                saida += ', '

        saida += ']'
        return saida

    def imprimir(self):
        print(self.__str__())
