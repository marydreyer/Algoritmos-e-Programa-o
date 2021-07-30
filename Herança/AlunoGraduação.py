from Aluno import Aluno

class AlunoFaculdade(Aluno):
   
  def __init__(self,nome,codigo,matricula,curso):
      Aluno.__init__(self,nome,codigo,matricula)
      self.curso = curso
      self.imprimirAF()

  def imprimirAF(self):
       print('\nAluno Graduação \nNome: {} \nCódigo: {} \nMatricula: {} \nCurso: {} '
        .format(self.nome, self.codigo, self.matricula, self.curso))
