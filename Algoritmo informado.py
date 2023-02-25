import time

class Vertice:
    def __init__(self, v, p):
        self.valor = v
        self.peso = p
        self.heuristica = v/p
        self.visitado = False

class Grafica:
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self, val, pes):
        if id not in self.vertices:
            self.vertices[val] = Vertice(val, pes)
            
    def AEstrella(self, r, PL, PA, camino):
        PA += self.vertices[r].peso
        if PA >= PL:
            print("\npeso: "+str(PA-self.vertices[r].peso))
            return 0
        self.vertices[r].visitado = True
        camino.append(self.vertices[r].valor)
        
        aux = 0
        min_val_heuristico = float(1000000) 
        for k in self.vertices:
            if self.vertices[k].visitado == False:
                if min_val_heuristico >= self.vertices[k].heuristica:
                    min_val_heuristico = self.vertices[k].heuristica
                    aux = int(k)
        if aux == 0:
            print("\npeso: "+str(PA))
            return 0
        self.AEstrella(aux, PL, PA, camino)

    
            
def main():
    inicio = time.time()
    print("Numero de nodos: ")
    NumNodos = float(input())
    print("Peso límite: ")
    pesoLimite = float(input())

    g = Grafica()
    for k in range(0,int(NumNodos)):
        print("Valor["+str(k+1)+"]: ")
        VN = float(input())
        print("Peso["+str(k+1)+"]: ")
        PN = float(input())
        g.agregarVertice(VN,PN)
        if k == 0:
            NodoInicial=VN
        

    pesoAcumulado =0.0
    camino = []
    g.AEstrella(NodoInicial, pesoLimite, float(pesoAcumulado), camino)
    print("\nCamino: "+str(camino))


    fin = time.time()
    print("\n\nTiempo de ejecución: "+ str(fin-inicio)+ " s")

main()