# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt

from collections import deque
from heapq import heappush, heappop
from itertools import count
#-----------------------------------------
# FILE DEDICATED TO PROTOTYPING FEATURES
#-----------------------------------------

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
            raise nx.NodeNotFound("Inicio {} nao esta no G".format(source))
        visao[inicio] = 0
        push(margem, (0, next(c), inicio))
    while margem:
        (d, _, v) = pop(margem)
        if v in dist:
            continue  # already searched this node.
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
        raise nx.NetworkXNoPath("Nao ha caminho para {}.".format(final))

def pesos(G, weight):
 #Metodo para retornar os pesos de um determinado grafo
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
            raise nx.NodeNotFound("Objeto inicial {} nao esta em G".format(s))

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
        msg = "Node %s not reachable from %s" % (final, inicial)
        raise nx.NetworkXNoPath(msg)


def floyd_warshall(G, weight='weight'):
    """Find all-pairs shortest path lengths using Floyd's algorithm.
    Parameters
    ----------
    G : NetworkX graph
    weight: string, optional (default= 'weight')
       Edge data key corresponding to the edge weight.
    Returns
    -------
    distance : dict
       A dictionary,  keyed by source and target, of shortest paths distances
       between nodes.
    Notes
    ------
    Floyd's algorithm is appropriate for finding shortest paths
    in dense graphs or graphs with negative weights when Dijkstra's algorithm
    fails.  This algorithm can still fail if there are negative cycles.
    It has running time $O(n^3)$ with running space of $O(n^2)$.
    See Also
    --------
    floyd_warshall_predecessor_and_distance
    floyd_warshall_numpy
    all_pairs_shortest_path
    all_pairs_shortest_path_length
    """
    # could make this its own function to reduce memory costs
    return floyd_warshall_predecessor_and_distance(G, weight=weight)[1]

def floyd_warshall_predecessor_and_distance(G, weight='weight'):
    """Find all-pairs shortest path lengths using Floyd's algorithm.
    Parameters
    ----------
    G : NetworkX graph
    weight: string, optional (default= 'weight')
       Edge data key corresponding to the edge weight.
    Returns
    -------
    predecessor,distance : dictionaries
       Dictionaries, keyed by source and target, of predecessors and distances
       in the shortest path.
    Examples
    --------
    >>> G = nx.DiGraph()
    >>> G.add_weighted_edges_from([('s', 'u', 10), ('s', 'x', 5),
    ...     ('u', 'v', 1), ('u', 'x', 2), ('v', 'y', 1), ('x', 'u', 3),
    ...     ('x', 'v', 5), ('x', 'y', 2), ('y', 's', 7), ('y', 'v', 6)])
    >>> predecessors, _ = nx.floyd_warshall_predecessor_and_distance(G)
    >>> print(nx.reconstruct_path('s', 'v', predecessors))
    ['s', 'x', 'u', 'v']
    Notes
    ------
    Floyd's algorithm is appropriate for finding shortest paths
    in dense graphs or graphs with negative weights when Dijkstra's algorithm
    fails.  This algorithm can still fail if there are negative cycles.
    It has running time $O(n^3)$ with running space of $O(n^2)$.
    See Also
    --------
    floyd_warshall
    floyd_warshall_numpy
    all_pairs_shortest_path
    all_pairs_shortest_path_length
    """
    from collections import defaultdict
    # dictionary-of-dictionaries representation for dist and pred
    # use some defaultdict magick here
    # for dist the default is the floating point inf value
    dist = defaultdict(lambda: defaultdict(lambda: float('inf')))
    for u in G:
        dist[u][u] = 0
    pred = defaultdict(dict)
    # initialize path distance dictionary to be the adjacency matrix
    # also set the distance to self to 0 (zero diagonal)
    undirected = not G.is_directed()
    for u, v, d in G.edges(data=True):
        e_weight = d.get(weight, 1.0)
        dist[u][v] = min(e_weight, dist[u][v])
        pred[u][v] = u
        if undirected:
            dist[v][u] = min(e_weight, dist[v][u])
            pred[v][u] = v
    for w in G:
        for u in G:
            for v in G:
                if dist[u][v] > dist[u][w] + dist[w][v]:
                    dist[u][v] = dist[u][w] + dist[w][v]
                    pred[u][v] = pred[w][v]
    return dict(pred), dict(dist)

G = nx.DiGraph()
'''
elist = [(1, 2, {'weight':5}), (2, 3, {'weight':3}), (3, 5, {'weight':1}), (4, 5,{'weight':7.3}),(2, 5 ,{'weight':6.2})]
G.add_edges_from(elist)

#Res = dijkstra_path(G, 1, 5)

#(length, path) = single_source_dijkstra(G, 1, target=5, weight='weight')
#Res = path

Res = dijkstra(G, 1, final=5, weight='weight')

print(Res)

#print(bellman_ford_path(G, 1, 5))
Res2 = bellman_ford(G, 1, final=5, weight='weight')

print(Res2)

print( nx.floyd_warshall_numpy(G))
'''       
elist = [(1, 2, {'weight':5}), (2, 3, {'weight':3}), (3, 4, {'weight':1}), (4, 5,{'weight':7.3})]
G.add_edges_from(elist)
nx.draw(G)
plt.show()