from Veiculo import Veiculo
from Bicicleta import Bicicleta
from Automovel import Automovel
from Carro import Carro 
from Moto import Moto

veiculo = Veiculo("VolksWagen", 4, "Fusca", 100)
bicicleta = Bicicleta('Caloi', 2, 'Montana', 20, 7, True)
automovel = Automovel("Fiat", 4, "Palio", 80, 300)
carro = Carro("Ford", 4, "ka", 40, 300, 2)
moto = Moto("Honda", 2, "CG TITAN", 50, 200, True)
opcao = "" 

while( opcao != "0" ):
    print("\n========IMPRIMIR DADOS========")
    print("1 - Veiculo")
    print("2 - Bicicleta")
    print("3 - Automovel")
    print("4 - Carro")
    print("5 - Moto")
    print("0 - Sair")

    opcao = input("Digite sua opção:")

    if opcao == "1":
        veiculo.acelerar(50)
        veiculo.frear(80)
        veiculo.imprimir()

    if opcao == "2":
        bicicleta.imprimir()

    if opcao == "3":
        automovel.imprimir()
    
    if opcao == "4":
        carro.imprimir()

    if opcao == "5":
        moto.imprimir()