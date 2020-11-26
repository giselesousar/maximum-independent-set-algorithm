# -*- coding: utf-8 -*-

def degree(graph):
    l = 0
    v = -1
    for i in graph.keys():
        if(len(graph[i]) > l):
            l = len(graph[i])
            v = i
    return v


def delete(graph, v):
    graph.pop(v)
    for i in graph.keys():
        for j in graph[i]:
            if(j == v):
                graph[i].remove(j)
    return graph

def deleteNeighbors(graph, v):
    for i in range(0, len(graph[v])):
        graph = delete(graph, graph[v][0])
    return graph

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


# INSTÂNCIA DO PROBLEMA

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