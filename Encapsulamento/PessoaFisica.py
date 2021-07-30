from Pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, codigo, nome, endereço, telefone, cpf, idade, peso, altura):
        Pessoa.__init__(self, codigo, nome, endereço, telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso 
        self.altura = altura

    def imprime_cpf(self):
        print("CPF: ", self.__cpf)

    def __calcularIMC(self):
        imc = self.peso/self.altura**2
        print(round(imc,2))


