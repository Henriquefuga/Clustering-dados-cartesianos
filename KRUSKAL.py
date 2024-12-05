import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import distance_matrix

class UnionFind:
    def __init__(self, n):
        self.pai = list(range(n))
        self.ranque = [0] * n

    def encontrar(self, u):
        if self.pai[u] != u:
            self.pai[u] = self.encontrar(self.pai[u])
        return self.pai[u]

    def unir(self, u, v):
        raiz_u = self.encontrar(u)
        raiz_v = self.encontrar(v)

        if raiz_u != raiz_v:
            if self.ranque[raiz_u] > self.ranque[raiz_v]:
                self.pai[raiz_v] = raiz_u
            elif self.ranque[raiz_u] < self.ranque[raiz_v]:
                self.pai[raiz_u] = raiz_v
            else:
                self.pai[raiz_v] = raiz_u
                self.ranque[raiz_u] += 1

    def componentes_conectadas(self):
        return len(set(self.encontrar(i) for i in range(len(self.pai))))

def ler_coordenadas(caminho_arquivo):
    coordenadas = []
    with open(caminho_arquivo, 'r') as f:
        for linha in f:
            x, y = map(float, linha.split())
            coordenadas.append((x, y))
    return np.array(coordenadas)

def agrupar_com_union_find(coordenadas, k):
    n = len(coordenadas)
    uf = UnionFind(n)

    matriz_distancias = distance_matrix(coordenadas, coordenadas)

    arestas = []
    for i in range(n):
        for j in range(i+1, n):
            arestas.append((matriz_distancias[i, j], i, j))
    arestas.sort()

    num_componentes = n
    for dist, i, j in arestas:
        if uf.encontrar(i) != uf.encontrar(j):
            uf.unir(i, j)
            num_componentes -= 1
        if num_componentes == k:
            break

    clusters = {}
    for idx, coord in enumerate(coordenadas):
        raiz = uf.encontrar(idx)
        if raiz not in clusters:
            clusters[raiz] = []
        clusters[raiz].append(coord)
    
    return clusters

def plotar_clusters(clusters):
    cores = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    plt.figure(figsize=(8, 6))

    for i, (id_cluster, pontos) in enumerate(clusters.items()):
        pontos = np.array(pontos)
        plt.scatter(pontos[:, 0], pontos[:, 1], c=cores[i % len(cores)], label=f'Cluster {id_cluster+1}')
    
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Agrupamento com Conjunto Disjunto')
    plt.show()

def main(caminho_arquivo, k):
    coordenadas = ler_coordenadas(caminho_arquivo)
    clusters = agrupar_com_union_find(coordenadas, k)
    plotar_clusters(clusters)

caminho_arquivo = 'dados.txt'
k = 7
main(caminho_arquivo, k)
