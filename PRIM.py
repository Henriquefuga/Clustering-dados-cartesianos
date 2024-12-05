import math
import heapq
import matplotlib.pyplot as plt
import numpy as np

# Função para calcular a distância euclidiana entre dois pontos
def distancia_euclidiana(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# Função para encontrar a MST e armazenar as maiores arestas
def prim_mst_com_maiores_arestas(pontos, k):
    n = len(pontos)
    adj = {i: [] for i in range(n)}

    # Construindo a matriz de adjacência com distâncias
    for i in range(n):
        for j in range(i + 1, n):
            dist = distancia_euclidiana(pontos[i], pontos[j])
            adj[i].append((dist, j))
            adj[j].append((dist, i))

    # Algoritmo de Prim para encontrar a MST
    mst_arestas = []
    visitado = [False] * n
    pq = [(0, 0, -1)]  # (custo, nó atual, nó anterior)

    # Heap para armazenar as (k-1) maiores arestas
    maiores_arestas = []

    while pq:
        custo, u, pai = heapq.heappop(pq)
        if visitado[u]:
            continue
        visitado[u] = True

        if pai != -1:
            mst_arestas.append((pai, u, custo))
            # Inserir a aresta na heap de maiores arestas (min-heap)
            if len(maiores_arestas) < k - 1:
                heapq.heappush(maiores_arestas, (custo, pai, u))
            else:
                # Manter apenas as (k-1) maiores arestas
                heapq.heappushpop(maiores_arestas, (custo, pai, u))

        for proximo_custo, v in adj[u]:
            if not visitado[v]:
                heapq.heappush(pq, (proximo_custo, v, u))

    return mst_arestas, maiores_arestas

# Função para formar k clusters cortando as maiores arestas da MST
def prim_agrupamento(pontos, k):
    # Obter as arestas da MST e as maiores arestas
    mst_arestas, maiores_arestas = prim_mst_com_maiores_arestas(pontos, k)

    # Converter lista de maiores arestas em um conjunto para fácil remoção
    maiores_arestas_conjunto = set((u, v) if u < v else (v, u) for _, u, v in maiores_arestas)

    # Inicializar cada ponto como seu próprio cluster
    pai = list(range(len(pontos)))

    # Função para encontrar o "representante" de um cluster (com compressão de caminho)
    def encontrar(x):
        if pai[x] != x:
            pai[x] = encontrar(pai[x])
        return pai[x]

    # Função para unir dois clusters
    def unir(x, y):
        raizX = encontrar(x)
        raizY = encontrar(y)
        if raizX != raizY:
            pai[raizY] = raizX

    # Unir pontos na MST, exceto pelas k-1 maiores arestas removidas
    for u, v, _ in mst_arestas:
        if (u, v) in maiores_arestas_conjunto or (v, u) in maiores_arestas_conjunto:
            continue  # Ignorar as maiores arestas
        unir(u, v)

    # Agrupando os pontos em seus clusters
    clusters = {}
    for i in range(len(pontos)):
        raiz = encontrar(i)
        if raiz not in clusters:
            clusters[raiz] = []
        clusters[raiz].append(i)

    # Retornar os clusters finais
    return list(clusters.values())

# Função para ler coordenadas (x, y) de um arquivo .txt com tabulação e números float
def ler_pontos_do_arquivo(nome_arquivo):
    pontos = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()  # Remove espaços em branco no início e fim da linha
            if not linha:  # Ignora linhas vazias
                continue
            try:
                x, y = map(float, linha.split())  # Tenta dividir por espaço ou tabulação
                pontos.append((x, y))
            except ValueError:
                print(f"Erro ao ler a linha: {linha}. Linha ignorada.")
    return pontos

# Função para plotar os clusters
def plotar_clusters(pontos, clusters):
    cores = ['r', 'g', 'b', 'c', 'm', 'y', 'k']  # Cores para os clusters (até 7 clusters)
    
    plt.figure(figsize=(8, 6))
    
    for i, cluster in enumerate(clusters):
        cluster_pontos = np.array([pontos[idx] for idx in cluster])
        cor = cores[i % len(cores)]  # Ciclamos as cores se tivermos mais de 7 clusters
        plt.scatter(cluster_pontos[:, 0], cluster_pontos[:, 1], c=cor, label=f'Cluster {i + 1}')
    
    plt.title(f'Agrupamento de Pontos em {len(clusters)} Clusters')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.legend()
    plt.grid(True)
    plt.show()

# Exemplo de uso com arquivo .txt
if __name__ == "__main__":
    nome_arquivo = "dados.txt"  # nome do arquivo com as coordenadas
    pontos = ler_pontos_do_arquivo(nome_arquivo)
    
    k = 5  # número de clusters desejados

    clusters = prim_agrupamento(pontos, k)

    print("Clusters formados:")
    for cluster in clusters:
        print([pontos[i] for i in cluster])
    
    # Plotar os clusters formados
    plotar_clusters(pontos, clusters)