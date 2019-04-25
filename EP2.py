# EP2  Gabriel Yudi Hirata  9349666
class Grafo:
    def __init__(self):
        self.grafo = {}
        self.vertice = {}
        self.arco = []
        
    def AcrescentaVertice(self,v):
        if v in self.grafo:
            print("%s já existe." %v)
        else:
            self.grafo[v] = {}

    def RemoveVertice(self,v):
        if v not in self.grafo:
            print("%s não é um vértice existente." %v)
        elif self.arco[v] == []:
            self.vertice.pop(v)
        else:
            print("O vértice %s contém arco(s) e não pode ser removido." %v)
            
    # def AcrescentaArco(v1,v2,w):        
    
    # def RemoveArco(v1,v2):
        
    # def ImprimeGrafo():    

