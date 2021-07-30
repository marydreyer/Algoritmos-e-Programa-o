from Aluno import Aluno
from AlunoEnsinoMedio import AlunoEnsMedio
from AlunoGraduação import AlunoFaculdade

aluno1 = Aluno("Mariana", 1, 604)
aluno2 = AlunoEnsMedio("Mariana" , 1, 604, "Segundo Ano")
aluno3 = AlunoFaculdade("Mariana", 1, 604, "Análise e Desenvolvimento de Sistemas")

aluno1.imprimir()
aluno2.imprimirAlunoEM()
aluno3.imprimirAF()