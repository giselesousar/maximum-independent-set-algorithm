# -*- coding: utf-8 -*-

"""
Maxset(G);
Begin /* to return the size of the largest Independent Set of G*/ 
	If degree(G) = 0 then 
		Maxset = all vertices in G 
	Else 
		Choose a vertex v*; 
	n1 = Maxset(G - {v*}); 
	n2 = Maxset(G – {v*} – Nb(v*)); 
	Maxset = maximum_of(n1, n2); 
end; 
"""

# Algorithm

# function to find the degree of a given graph
# (will be the number of edges in the node with the highest number of neighboring)


# O(n)

#o(v)

# function to find the degree of a given graph
# (will be the number of edges in the node with the highest number of neighboring)



# O(n)


def degree(graph):
	l = 0
	v = -1
	for i in graph.keys():
		if(len(graph[i]) > l):
			l = len(graph[i])
			v = i
	return v

# function to find the vertex with highest degree of a given graph
# (returns the last find vertex that has a degree equals to the graph´s degree)

# O(n)

#o(v) talvez mudar isso aqui porque o carlos falou

# O(n)


def findVertex(graph):
    l = degree(graph)
    for i in graph.keys():
        if(len(graph[i]) == l):
            v = i
    return v

# function that deletes all references to vertex v in the graph


# O(n²)

# O(n²)
def delete(graph, v):
    graph.pop(v)
    for i in graph.keys():  # n
        for j in graph[i]:  # n-1
            if(j == v):
                graph[i].remove(j)
    return graph

# function that deletes all neighbors (and their references) of a node

# O(n³)


def deleteNeighbors(graph, v):
    for i in range(0, len(graph[v])):
        graph = delete(graph, graph[v][0])
    return graph

# T(n) = T(n-1) + n² = O(n²)
# T(n) = T(n-1) + n² = O(n²) verificar se é n^3

import copy

def maxIndSet(graph):
	v = degree(graph)

	if(v == -1):
		return graph

	graph1 = copy.deepcopy(graph)
	graph2 = copy.deepcopy(graph)

	n1 = delete(graph1, v)
	n2 = deleteNeighbors(graph2, v)

	return maxIndSet(n1) if(len(n1) > len(n2)) else maxIndSet(n2)

graph = {"a": ["b", "c"],
         "b": ["a", "c"],
         "c": ["a", "b"],
         "d": ["e", "f", "g", "h"],
         "e": ["d", "f"],
         "f": ["e", "d", "g", "h"],
         "g": ["d", "f", "h", "n"],
         "h": ["d", "f", "g", "n"],
         "i": ["j", "k", "n"],
         "j": ["i", "k", "l"],
         "k": ["i", "j", "l", "m", "n"],
         "l": ["j", "k", "m"],
         "m": ["k", "l", "n"],
         "n": ["i", "g", "h", "k", "m"],
         "o": ["p", "q"],
         "p": ["o", "q"],
         "q": ["o", "p"],
         "r": ["s", "t"],
         "s": ["r", "t"],
         "t": ["r", "s", "u"],
         "u": ["t"],
         "v": ["x"],
         "x": ["v"]
		}

print(maxIndSet(graph))

# Trecho de código referente a aquisição da imagem do conjunto máximo independente 

import networkx as nx
import matplotlib.pyplot as plt

conjuntoMaximoIndependente = maxIndSet(graph)

conjuntoMaximoIndependente_plot = nx.Graph()

for i in conjuntoMaximoIndependente.keys():
    conjuntoMaximoIndependente_plot.add_node(i)

for i in conjuntoMaximoIndependente.keys():
    for j in conjuntoMaximoIndependente[i]:
        conjuntoMaximoIndependente_plot.add_edge(i, j)

nx.draw_networkx(conjuntoMaximoIndependente_plot)
plt.savefig("conjuntoMaximoIndependente_plot.png")