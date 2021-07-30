from Pessoa import Pessoa
from PessoaJuridica import PessoaJuridica
from PessoaFisica import PessoaFisica




pf1 = PessoaFisica(1, "Mariana", "Rua Grêmio esquina Campeão", 5199887786, 2103365486, 38, 72, 1.65)
pf1.imprime_cpf()

pj1 = PessoaJuridica(2, "Roger","Rua Palmeiras", 123456789, "987654321", 456987123, 20)
pj1.imprimeCNPJ()


