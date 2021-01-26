# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations, chain
import itertools
import copy

# Trecho de código referente a aquisição da imagem do conjunto máximo independente

def plotarCMI(g):

    if (g == None):
        print("Grafo vazio")
        return

    conjuntoMaximoIndependente = g
    conjuntoMaximoIndependente_plot = nx.Graph()

    for i in conjuntoMaximoIndependente:
        conjuntoMaximoIndependente_plot.add_node(i)

    nx.draw_networkx(conjuntoMaximoIndependente_plot)
    plt.savefig("conjuntoMaximoIndependente_plot.png")


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
#          }
graph = {
         }
#  "d": ["b", "c", "e"],
#  "e": ["d", "f"],
#  "f": ["b", "e"]
#  }




plotarCMI(maxIndSet(graph))