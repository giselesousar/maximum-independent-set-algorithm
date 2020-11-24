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
def degree(graph):
	l = 0
	for i in graph.keys():
		if(len(graph[i]) > l):
			l = len(graph[i])
	return l

# function to find the vertex with highest degree of a given graph 
# (returns the last find vertex that has a degree equals to the graph´s degree)
def findVertex(graph):
	l = degree(graph)
	for i in graph.keys():
		if(len(graph[i]) == l):
			v = i
	return v	

# function that deletes all references to vertex v in the graph 
def delete(graph, v):
	graph.pop(v)
	for i in graph.keys():
		for j in graph[i]:
			if(j == v):
				graph[i].remove(j)
	return graph

# function that deletes all neighbors (and their references) of a node
def deleteVizinhos(graph, v):
	for i in range (0, len(graph[v])):
		graph = delete(graph, graph[v][0])
		# a cada deletar os valores da chave em questão (representa o vértice que terá seus vizinhos excluídos)
		# vão automaticamente se deslocando para o início da fila, pois o espaço da primeiro posição foi liberado 
	return graph

def maxIndSet1(graph):
	if(degree(graph) == 0):
		return graph
	v = findVertex(graph)
	maxIndSet1(delete(graph, v))
	return graph

def maxIndSet2(graph):
	if(degree(graph) == 0):
		return graph
	v = findVertex(graph)
	maxIndSet2(deleteVizinhos(graph, v))
	return graph

#function to find the maximum independent set of a given graph
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

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
	

print(maxIndSet(graph))