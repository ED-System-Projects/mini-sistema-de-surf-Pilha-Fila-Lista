class Surfista:
    def __init__(self, nome, titulos, idade, cpf):
        self.__nome = nome
        self.__titulos = titulos
        self.__idade = idade
        self.__cpf = cpf
        self.__prox = None

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo__nome

    def get_titulos(self):
        return self.__titulos

    def set_titulos(self, titulos):
        self.__titulos = titulos

    def incrementa_titulo(self):
        self.__titulos += 1

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_prox(self):
        return self.__prox

    def set_prox(self, proximo):
        self.__prox = proximo

    def __str__(self):
        return (f"Nome:    {self._nome}\n"
                f"Titulos: {self._titulos}\n"
                f"Idade:   {self._idade}\n"
                f"CPF:     {self._cpf}")
