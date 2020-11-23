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

#Algorithm

#function to find the degree of a given graph
def degree(graph):
	l = 0
	for i in graph.keys():
		if(len(graph[i]) > l):
			l = len(graph[i])
	return l

#function to find the vertex with highest degree of a given graph
def findVertex(graph):
	l = degree(graph)
	for i in graph.keys():
		if(len(graph[i]) == l):
			v = i
	return v	

#deleta todas as referencias ao vertice v no grafo 
def delete(graph, v):
	graph.pop(v)
	for i in graph.keys():
		for j in graph[i]:
			if(j == v):
				graph[i].remove(j)
	return graph

def deleteVizinhos(graph, v):
	for i in range (0, len(graph[v])):
		graph = delete(graph, graph[v][0])
	return graph

def maxIndSet1(graph):
	if(degree(graph) == 0):
		return graph
	v = findVertex(graph)
	n1 = maxIndSet1(delete(graph, v))
	return graph

def maxIndSet2(graph):
	if(degree(graph) == 0):
		return graph
	v = findVertex(graph)
	n1 = maxIndSet1(deleteVizinhos(graph, v))
	return graph

#function to find the maximum independent set of a given graph
def maxIndSet(graph):
	graph1 = dict(graph)
	graph2 = dict(graph)
	n1 = maxIndSet1(graph1)
	n2 = maxIndSet2(graph2)
	return graph1 if(len(n1) > len(n2)) else graph2

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
	

print(maxIndSet(graph))


