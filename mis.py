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
def degree(graph):
    l = 0
    for i in graph.keys():
        if(len(graph[i]) > l):
            l = len(graph[i])
    return l

# function to find the vertex with highest degree of a given graph
# (returns the last find vertex that has a degree equals to the graph´s degree)

# O(n)

#o(v) talvez mudar isso aqui porque o carlos falou
def findVertex(graph):
    l = degree(graph)
    for i in graph.keys():
        if(len(graph[i]) == l):
            v = i
    return v

# function that deletes all references to vertex v in the graph


# O(n²)

def delete(graph, v):
	gh = dict(graph)
	gh.pop(v)
	for i in gh.keys():  # n
		for j in gh[i]:  # n-1
			if(j == v):
				gh[i].remove(j)
	return gh

# function that deletes all neighbors (and their references) of a node

# O(n³)

def deleteVizinhos(graph, v):
    for i in range(0, len(graph[v])):
        graph = delete(graph, graph[v][0])
    return graph

# T(n) = T(n-1) + n² = O(n²)
# T(n) = T(n-1) + n² = O(n²) verificar se é n^3


def maxIndSet1(graph):
    if(degree(graph) == 0):
        return graph
    v = findVertex(graph)
    maxIndSet1(delete(graph, v))
    return graph

# O(n³)

def maxIndSet2(graph):
    if(degree(graph) == 0):
        return graph
    v = findVertex(graph)
    maxIndSet2(deleteVizinhos(graph, v))
    return graph

# function to find the maximum independent set of a given graph


def maxIndSet(graph):
    graph1 = dict(graph)
    graph2 = dict(graph)
    n1 = maxIndSet1(graph1)
    n2 = maxIndSet2(graph2)
    print("Conjunto Independente I: ")
    print(n1)
    print()
    print("Conjunto Independente II: ")
    print(n2)
    print()
    print("Conjunto Independente Máximo: ")
    return graph1 if(len(n1) > len(n2)) else graph2



def maxIndSet(graph):	
	if(degree(graph) == 0):
		return graph
	graph1 = dict(graph)
	graph2 = dict(graph)
	v = findVertex(graph)
	n1 = maxIndSet(delete(graph1, v)) 
	print(v)
	print(n1)
	n2 = maxIndSet(deleteVizinhos(graph2, v))
	return n1 if(len(n1) > len(n2)) else n2


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

maxIndSet(graph)

# Trecho de código referente a aquisição das imagens do grafo e do seu respectivo conjunto indepente máximo


