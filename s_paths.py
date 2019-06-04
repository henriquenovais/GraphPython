import networkx as nx
from collections import deque
from heapq import heappush, heappop
from itertools import count
import numpy as np

#--------------------------
# MÉTODOS PARA ENCONTRAR
# OS MENORES CAMINHOS
#--------------------------

def dijkstra(G, inicial, final=None, weight='weight'):
    
    inicial = {inicial}
    if final in inicial:
        return (0, [final])
    weight = pesos(G, weight)
    caminhos = {inicio: [inicio] for inicio in inicial}  #Dicionario de caminhos possiveis
    
    G_succ = G._succ if G.is_directed() else G._adj
    pred = None
    push = heappush
    pop = heappop
    dist = {}  # Dicionario de distancias finais
    visao = {}
    #margem eh uma estrutura heapq com tres tuplas (distance,c,nodo)
    c = count()
    margem = []
    for inicio in inicial:
        if inicio not in G:
            raise print("O vertice inicial não foi encontrado")
        visao[inicio] = 0
        push(margem, (0, next(c), inicio))
    while margem:
        (d, _, v) = pop(margem)
        if v in dist:
            continue  # Caso o no ja tenha sido buscado
        dist[v] = d
        if v == final:
            break
        for u, e in G_succ[v].items():
            cost = weight(v, u, e)
            if cost is None:
                continue
            vu_dist = dist[v] + cost
            if u not in visao or vu_dist < visao[u]:
                visao[u] = vu_dist
                push(margem, (vu_dist, next(c), u))
                if caminhos is not None:
                    caminhos[u] = caminhos[v] + [u]
                if pred is not None:
                    pred[u] = [v]
            elif vu_dist == visao[u]:
                if pred is not None:
                    pred[u].append(v)

    if final is None:
        return (dist, caminhos)
    try:
        return (dist[final], caminhos[final])
    except KeyError:
        raise print("Nao ha caminho para esse vertice")

def pesos(G, weight):
    if callable(weight):
        return weight
 #Metodo para retornar uma função que retorna os pesos de um determinado grafo
    if G.is_multigraph():
        return lambda u, v, d: min(attr.get(weight, 1) for attr in d.values())
    return lambda u, v, data: data.get(weight, 1)


def bellman_ford(G, inicial, final=None, weight='weight'):
    if inicial == final:
        return (0, [inicial])

    weight = pesos(G, weight)

    caminhos = {inicial: [inicial]}  # dicionario de caminhos

    dist = None #Definicao da variavel de distancia para realizar o calculo da distancia entre os grafos
    pred = None  #Nao vao ser utilizados dicionarios de listas
    for s in [inicial]:
        if s not in G:
            raise print("O objeto não esta em G")

    if pred is None:
        pred = {v: [] for v in [inicial]}

    if dist is None:
        dist = {v: 0 for v in [inicial]}

    G_succ = G.succ if G.is_directed() else G.adj #Ajuste de classificacao de acordo com o tipo do grafo
    inf = float('inf') #definindo infinito [utilizado para grafos inalcansaveis]
    n = len(G)

    count = {}
    q = deque([inicial])
    na_fila = set([inicial])
    while q:
        u = q.popleft()
        na_fila.remove(u)

        if all(pred_u not in na_fila for pred_u in pred[u]):
            dist_u = dist[u]
            for v, e in G_succ[u].items():
                dist_v = dist_u + weight(v, u, e)

                if dist_v < dist.get(v, inf):
                    if v not in na_fila:
                        q.append(v)
                        na_fila.add(v)
                        count_v = count.get(v, 0) + 1
                        if count_v == n:
                            raise nx.NetworkXUnbounded(
                                "Ciclo de custo negativo detectado")
                        count[v] = count_v
                    dist[v] = dist_v
                    pred[v] = [u]

                elif dist.get(v) is not None and dist_v == dist.get(v):
                    pred[v].append(u)

    if caminhos is not None:
        dsts = [final] if final is not None else pred
        for dst in dsts:

            caminho = [dst]
            cur = dst

            while pred[cur]:
                cur = pred[cur][0]
                caminho.append(cur)

            caminho.reverse()
            caminhos[dst] = caminho

    if final is None:
        return (dist, caminhos)
    try:
        return (dist[final], caminhos[final])
    except KeyError:
        msg = "Vertice %s não é alcalçável de  %s" % (final, inicial)
        raise print("Não há caminho")

def floyd_warshall(G):
    n = G.number_of_nodes()
    W = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                W[i, j] = 0
            elif G.has_edge(i, j):
                W[i, j] = G.get_edge_data(i, j)['weight']
            else:
                W[i, j] = np.inf
    n = W.shape[0]
    D0 = W
    for k in range(0, n):
        Dk = np.zeros((n, n))
        for i in range(0, n):
            for j in range(0, n):
                Dk[i, j] = min(D0[i, j], D0[i, k] + D0[k, j])
        D0 = Dk

    return Dk

if __name__ == '__main__':
    #Grafo para realizar o teste
    G = nx.DiGraph()
    elist = [(1, 2, {'weight':5}), (2, 3, {'weight':3}), (3, 5, {'weight':1}), (4, 5,{'weight':7.3}),(2, 5 ,{'weight':6.2})]
    G.add_edges_from(elist)


    #Formato para chamar as funções
    Res = dijkstra(G, 1, 5, 'weight')
    print(Res)

    Res2 = bellman_ford(G, 1, 5, 'weight')
    print(Res2)

    print( floyd_warshall(G))

