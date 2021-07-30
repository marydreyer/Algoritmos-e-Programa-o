from Aluno import Aluno

class AlunoEnsMedio(Aluno):

    def __init__(self,nome,codigo,matricula,anoletivo):
        Aluno.__init__(self,nome,codigo,matricula)
        self.anoletivo = anoletivo
        self.imprimirAlunoEM()

    def imprimirAlunoEM(self):
         print('\nAluno Ensino Médio \nNome: {} \nCódigo: {} \nMatricula: {} \nAno Letivo: {} '
        .format(self.nome, self.codigo, self.matricula, self.anoletivo))
        