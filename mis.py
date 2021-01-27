# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations, chain
import itertools
import copy
from random import randrange
import time

################### GRAPH GENERATOR ###################
def generateGraph(n):
    mydict = {}
    quantEdge = (n * (n - 1))/2
    edges = []
    for i in range(1, n + 1):
        mydict[str(i)] = []

    for i in range(1, randrange(1, quantEdge)):
        edge = [str(randrange(1, n)), str(randrange(1, n))]
        copia = copy.deepcopy(edge)
        copia.reverse()      
        while((edge[0] == edge[1]) or (edge in edges) or (copia in edges)):
            edge = [str(randrange(1, n)), str(randrange(1, n))]
            copia = copy.deepcopy(edge)
            copia.reverse()  
        edges.append(edge)
    for edge in edges:
        mydict[edge[0]].append(str(edge[1]))
        mydict[edge[1]].append(str(edge[0]))

    return mydict


################### Brute Force #####################

def plotBF(conjuntoMaximoIndependente):

    if (conjuntoMaximoIndependente == None):
        print("Grafo vazio")
        return

    conjuntoMaximoIndependente_plot = nx.Graph()

    for i in conjuntoMaximoIndependente:
        conjuntoMaximoIndependente_plot.add_node(i)

    nx.draw_networkx(conjuntoMaximoIndependente_plot)
    plt.savefig("conjuntoMaximoIndependente_forcaBruta.png")

def findsubsets(s):
    subsets = []
    for i in range(len(s), 0, -1):
        subsets.append(list(itertools.combinations(s, i)))
    return subsets


def maxIndSetBF(graph):
    subsets_lists = findsubsets(graph)

    for subset_list in subsets_lists:  # [('a', 'b', 'c')]
        for subset in subset_list:  # ('a', 'b', 'c')
            flag = False
            for vertex in subset:  # a
                for vertex_else in subset:
                    if(vertex_else != vertex):
                        if vertex_else in graph[vertex]:
                            flag = True
                            break
                if(flag):
                    break
            if (not flag):
                return subset
    return None

######################################################

################ Heuristic Algorithm #################

def plotHA(conjuntoMaximoIndependente):

    conjuntoMaximoIndependente_plot = nx.Graph()

    for i in conjuntoMaximoIndependente.keys():
        conjuntoMaximoIndependente_plot.add_node(i)

    for i in conjuntoMaximoIndependente.keys():
        for j in conjuntoMaximoIndependente[i]:
            conjuntoMaximoIndependente_plot.add_edge(i, j)

    nx.draw_networkx(conjuntoMaximoIndependente_plot)
    plt.savefig("conjuntoMaximoIndependente_algoritmoHeuristico.png")

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

def maxIndSetHA(graph):
    v = degree(graph)

    if(v == -1):
        return graph

    graph1 = copy.deepcopy(graph)
    graph2 = copy.deepcopy(graph)

    n1 = delete(graph1, v)
    n2 = deleteNeighbors(graph2, v)

    return maxIndSetHA(n1) if(len(n1) > len(n2)) else maxIndSetHA(n2)


######################################################


# INSTÂNCIA DO PROBLEMA

# graph = {"a": ["b", "c"],
#          "b": ["a", "c"],
#          "c": ["a", "b"],
#          "d": ["e", "f", "g", "h"],
#          "e": ["d", "f"],
#          "f": ["e", "d", "g", "h"],
#          "g": ["d", "f", "h", "n"],
#          "h": ["d", "f", "g", "n"],
#          "i": ["j", "k", "n"],
#          "j": ["i", "k", "l"],
#          "k": ["i", "j", "l", "m", "n"],
#          "l": ["j", "k", "m"],
#          "m": ["k", "l", "n"],
#          "n": ["i", "g", "h", "k", "m"],
#          "o": ["p", "q"],
#          "p": ["o", "q"],
#          "q": ["o", "p"],
#          "r": ["s", "t"],
#          "s": ["r", "t"],
#          "t": ["r", "s", "u"],
#          "u": ["t"],
#          "v": ["x"],
#          "x": ["v"]
# 		}

"""
graph = {
        "a": ["c", "e"],
        "b": ["d", "f"],
        "c": ["a", "d"],
        "d": ["c", "b"],
        "e": ["a", "f"],
        "f": ["b", "e"],
}
"""
tamanhos = [4, 8, 12, 16, 20, 24] ## 16, 32

for i in tamanhos:
    print("Tamanho: " + str(i))
    graph = generateGraph(i)

    somaBF = 0
    somaHA = 0
    quant = 3

    for j in range(1, quant+1):
        copia = copy.deepcopy(graph)

        inicio = time.time()
        maxIndSetBF(copia)
        fim = time.time()

        tempo = round((fim - inicio) * 1000, 4)
        somaBF += tempo
        print("Tempo FB: " + str(tempo))

        inicio = time.time()
        maxIndSetHA(copia)
        fim = time.time()

        tempo = round((fim - inicio) * 1000, 4)
        somaHA += tempo
        print("Tempo HA: " + str(tempo))

    print("Media de tempo BF: " + str(somaBF/quant))
    print("Media de tempo HA: " + str(somaHA/quant))
    print()
    


