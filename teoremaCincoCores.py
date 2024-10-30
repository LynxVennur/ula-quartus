import networkx as nx

def algoritmo_5_cores(grafo):
    is_planar, _ = nx.check_planarity(grafo)
    if not is_planar:
        print("O grafo não é planar, portanto o algoritmo das 5 cores não pode ser aplicado.")
        return False

    grafo_aux = grafo.copy()

    vertices = list(grafo_aux.nodes)
    ordem = []

    while vertices:
        for v in vertices:
            if grafo_aux.degree(v) <= 5:
                ordem.append(v)
                vertices.remove(v)
                grafo_aux.remove_node(v)
                break

    cores = {}
    for v in reversed(ordem): 
        vizinhos = list(grafo.neighbors(v))  
        cor_disponivel = set(range(5)) - {cores.get(vizinho) for vizinho in vizinhos if vizinho in cores}
        cores[v] = min(cor_disponivel)  

    num_cores_usadas = len(set(cores.values()))

    return cores

# Exemplo 1
vertices = [1, 2, 3, 4, 5, 6, 7, 8]
arestas = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (2, 4), (3, 5), (5, 6), (6, 7), (7, 8), (8, 6)]
grafo = nx.Graph()
grafo.add_nodes_from(vertices)
grafo.add_edges_from(arestas)
cores = algoritmo_5_cores(grafo)
print(f"Cores usadas no Exemplo 1: {cores}")
print(f"Quantidade de cores no Exemplo 1: {len(set(cores.values()))}\n")

# Exemplo 2
vertices = [1, 2, 3, 4, 5, 6]
arestas = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)]
grafo = nx.Graph()
grafo.add_nodes_from(vertices)
grafo.add_edges_from(arestas)
cores = algoritmo_5_cores(grafo)
print(f"Cores usadas no Exemplo 2: {cores}")
print(f"Quantidade de cores no Exemplo 2: {len(set(cores.values()))}\n")

# Exemplo 3
vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arestas = [(1, 2), (2, 3), (4, 5), (5, 6), (7, 8), (8, 9), (1, 4), (4, 7), (2, 5), (5, 8), (3, 6), (6, 9)]
grafo = nx.Graph()
grafo.add_nodes_from(vertices)
grafo.add_edges_from(arestas)
cores = algoritmo_5_cores(grafo)
print(f"Cores usadas no Exemplo 3: {cores}")
print(f"Quantidade de cores no Exemplo 3: {len(set(cores.values()))}\n")