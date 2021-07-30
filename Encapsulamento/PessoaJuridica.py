from Pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cnpj, inscricaoEstadual, qtdadeFuncionarios):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cnpj = cnpj
        self.__inscricaoEstadual = inscricaoEstadual
        self.qtdadeFuncionarios = qtdadeFuncionarios

    def imprimeCNPJ(self):
        print("CNPJ: ", self.__cnpj)

    def __emitirnotafiscal(self):
        print("Nota fiscal Emitida")