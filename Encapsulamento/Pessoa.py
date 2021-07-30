class Pessoa:

    def __init__(self, codigo, nome, endereco, telefone):
        self.__codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.__telefone = telefone

    def imprime_nome(self):
        print("Nome: ", self.nome)

    def __imprimefone(self):
        print("Telefone: ", self.__telefone)



