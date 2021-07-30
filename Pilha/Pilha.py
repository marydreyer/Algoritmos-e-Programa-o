from No import No

class Pilha:

    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def adicionar(self, valor):
        no = No(valor)
        if self.tamanho == 0:
            self.topo = no
        else: 
            no.proximo = self.topo
            self.topo = no
        self.tamanho += 1
    
    def imprimir(self):	
        if self.tamanho == 0:
            print("Pilha vazia!")
        else:
            aux = self.topo
            while(aux):
                print(aux.dado)
                aux = aux.proximo
            print("=========================")	
		        
    def remover(self):
		    if self.tamanho == 0:
			    print( "Pilha vazia!" )
		    elif self.tamanho == 1:
			    self.topo = None
			    self.tamanho = 0
		    else:
			    self.topo = self.topo.proximo
			    self.tamanho -= 1
		    self.imprimir()

    