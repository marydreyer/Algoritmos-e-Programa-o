class Aluno:

    def __init__(self,nome,codigo,matricula):
        self.nome = nome
        self.codigo = codigo
        self.matricula = matricula
        self.imprimir()

    def imprimir(self):
         print('\nAlunos\nNome: {} \nCódigo: {} \nMatricula: {} '
        .format(self.nome, self.codigo, self.matricula))


