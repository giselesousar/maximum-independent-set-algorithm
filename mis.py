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
	v = graph.keys()[0]
	l = degree(graph)
	for i in graph.keys():
		if(len(graph[i]) == l):
			v = i
	return v	

#function to find the maximum independent set of a given graph
#def maxIndSet(graph):
	

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
	

print(findVertex(graph))


