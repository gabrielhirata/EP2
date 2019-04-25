# EP2  Gabriel Yudi Hirata  9349666
class Grafo:
    def __init__(self):
        self.vertice = {}
        self.arco = {}
        self.custo = []
        
    def AcrescentaVertice(self,v):
        if v in self.vertice:
            print("%s já existe." %v)
        else:
            self.vertice[v] = {}

    def RemoveVertice(self,v):
        if v not in self.vertice:
            print("%s não é um vértice existente." %v)
        elif self.arco[v] == {}:
            self.vertice.pop(v)
        else:
            print("O vértice %s contém arco(s) e não pode ser removido." %v)
            
    def AcrescentaArco(self,v1,v2,w):        
        if v1 or v2 not in self.vertice:
            print("%s ou %s não é vértice." %(v1,v2))
        else:
            self.vertice[v1].update({v2:w})

    def RemoveArco(self,v1,v2):
        if v2 not in self.vertice[v1]:
            print("Arco entre %s e %s não existe." %(v1,v2))
        else:
            self.vertice[v1].pop(v2)
        
    # def ImprimeGrafo():    

