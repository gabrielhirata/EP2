# EP2  Gabriel Yudi Hirata  9349666
import re                   # importa biblioteca que usa expressão regular
class Grafo:
    def __init__(self):
        self.grafo = {}
        
    def AcrescentaVertice(self,v):
        assert type(v) is str, "Vértice deve ser do tipo string, mas recebi %s." %type(v)
        assert v not in self.grafo, "O vértice %s já existe." %v
        self.grafo[v] = {}

    def RemoveVertice(self,v):
        assert v in self.grafo, "O vértice %s não existe." %v
        assert self.grafo[v] == {}, "O vértice %s tem um arco associado." %v
        self.grafo.pop(v)
            
    def AcrescentaArco(self,v1,v2,w):
        assert v1 in self.grafo, "O vértice %s não existe." %v1
        assert v2 in self.grafo, "O vértice %s não existe." %v2      
        assert type(v1) is str and type(v2) is str, "Vértices devem ser strings, recebi %s e %s" %(type(v1), type(v2)) 
        self.grafo[v1][v2] = w
        self.grafo[v2][v1] = w

    def RemoveArco(self,v1,v2):
        assert v2 in self.grafo[v1], "Arco entre %s e %s não existe." %(v1,v2)
        self.grafo[v1].pop(v2)
        self.grafo[v2].pop(v1)

    # def AchaCaminhoMenorTempo(self,v1,v2):
    #     return path

    # def AchaCaminhoMenorCusto(self,v1,v2):
    #     return path

    # def ImprimeGrafo():

    def vizinho(self, v1, v2):
        return v2 in self.grafo[v1]

    def dijkstra(self,inicio,destino):
        assert inicio in self.grafo, "Vértice %s não existe" %inicio
        assert destino in self.grafo, "Vértice %s não existe" %destino
        S = {inicio}
        dist = {}
        Path = {}
        # inicializa o array dist[] com o peso dos arcos conectados ao vértice inicio
        for vertice in self.grafo:
            if vertice != inicio and vertice in self.grafo[inicio]:
                dist[vertice] = self.grafo[inicio][vertice][0]
                Path[vertice] = inicio
            else:
                print("vertice %s nao esta conectado a %s" %(vertice, inicio)) 
                dist[vertice] = float("inf")
        minimo = inicio

        while len(S) != len(self.grafo):
            # escolha um vértice M(minimo), que não esteja em S para o qual Dist[M] é minimo
            for vertice in self.grafo.keys() - S:
                if dist[vertice] <= dist[minimo]:
                    minimo = vertice
            S.add(minimo)
            for vertice in self.grafo.keys() - S: 
                if self.vizinho(minimo, vertice) and dist[vertice] > dist[minimo] + self.grafo[minimo][vertice]:
                    dist[vertice] = dist[minimo] + self.grafo[minimo][vertice]
                    Path[vertice] = minimo
            minimo = inicio

        path = []
        if dist[destino] != float("inf"):
            path.append(destino)
            vertice = Path[destino]
            while vertice != inicio:
                path.insert(0, vertice)
                vertice = Path[vertice]
            path.insert(0, vertice)
        print(dist)
        print(S)
        print(path)
        print(Path)

def ArquivoExiste(filename):
    try:
      open(filename, "r")
      return 1
    except IOError:
      print("Erro: Arquivo \"%s\" não encontrado." %filename)
      return 0

def LeArquivo():
    config = input("Digite o nome do arquivo com as configurações com a extensão: ")
    while not ArquivoExiste(config):
        config = input("Digite o nome do arquivo com as configurações com a extensão: ")

    c = Grafo()

    # adiciona os vértices
    for linha in open(config):
        c.AcrescentaVertice(linha.split(' ')[0])

    # adiciona os arcos
    for linha in open(config):
        arcos = linha.split(' ')
        origem = arcos.pop(0)
        for arco in arcos:
            arco = arco.split(':')
            destino = arco[0]
            custos = eval(arco[1])
            c.AcrescentaArco(origem, destino, custos)
    return c

# g = Grafo()
# g.AcrescentaVertice("AT")
# # print(g.grafo)
# g.AcrescentaVertice("BT")
# # print(g.grafo)
# g.AcrescentaVertice("CT")
# g.AcrescentaArco("AT","BT",[2,200])
# g.AcrescentaArco("AT","CT",[3,300])
# # print(g.grafo)
# # g.RemoveArco("AT","BT")
# # print(g.grafo)
# # g.RemoveVertice("AT")
# print(g.grafo)
# g.dijkstra("AT", "BT")


def main():
    c = LeArquivo()
    print(c.grafo)
    c.dijkstra("A","E")

if __name__== "__main__":
  main()
