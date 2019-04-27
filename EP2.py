# EP2  Gabriel Yudi Hirata  9349666
class Grafo:
    def __init__(self):
        self.grafo = {}
        
    def AcrescentaVertice(self,v):
        assert type(v) is str, "Vértice deve ser do tipo string, mas recebi %s." %type(v)
        assert v not in self.grafo, "O vértice %s já existe." %v
        self.grafo[v] = {}

    def RemoveVertice(self,v):
        assert v in self.grafo, "O vértice %s não existe." %v
        assert self.grafo[v] != {}, "O vértice %s tem um arco associado." %v
        self.grafo.pop(v)
            
    def AcrescentaArco(self,v1,v2,w):
        assert v1 in self.grafo, "O vértice %s não existe." %v1
        assert v2 in self.grafo, "O vértice %s não existe." %v2      
        assert type(v1) is str and type(v2) is str, "Vértices devem ser strings, recebi %s e %s" %(type(v1), type(v2)) 
        self.grafo[v1][v2] = w

    def RemoveArco(self,v1,v2):
        assert v2 in self.grafo[v1], "Arco entre %s e %s não existe." %(v1,v2)
        self.grafo[v1].pop(v2)
        
    # def ImprimeGrafo():    

