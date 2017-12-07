'''
Coder: Jacky Shew
Description: Returns maximum congestion level of a graph from some vertex u,v.
			 Congestion is defined as number of edge-disjoint paths meaning 
			 no usage of edges as other paths, however nodes may be reused.
Input: First Line: Total number of nodes. Following Lines: Adjacency list of the nodes.
	   Repeat until 0.
Input example:
8
4 5 7
5 6
6 7
7
0 7
0 1
1 2 7
0 2 3 4 6
4
1 2
0 2
3 0 1
2
0
'''

import time
import operator 
import networkx as nx
from networkx.algorithms.flow import edmonds_karp

def instantiate_graph(nodes):
	degree_pair_list = []
	G = nx.DiGraph()
	#G.add_nodes_from(list(range(nodes))) #can also add_nodes_from(another_graph) #augment
	for i in range(nodes):
		nodes_edge = input().split() #Returns list of nodes to connect to by node[n]
		for j in range(len(nodes_edge)): #Loops for length of elements in 'nodes to connect to'
			current_edge = int(nodes_edge[j])
			if current_edge > i: #Optimise by keeping already connected edges
				G.add_edge(i,current_edge, capacity=1)
				G.add_edge(current_edge, i, capacity=1)
				degree_pair_list += [(i,G.degree(i))]
	#print(degree_pair_list)			
	#print(G.edges)
	#print(G.nodes)
	start_time = time.time()
	while_counter = 0
	counter = 0
	congestion = 0
	visited_list = {}
	x = sorted(degree_pair_list, key=lambda x:x[1])
	while while_counter != nodes:
		i = x.pop()
		highest_degree_i = i[0]
		#print(highest_degree_i)
		if highest_degree_i > congestion:
			if highest_degree_i not in visited_list: 
				visited_list[highest_degree_i] = []
			for j in range(nodes): #highest_degree_i node source, j node sink
				if j not in visited_list: 
						visited_list[j] = []
				if highest_degree_i!=j and G.degree(highest_degree_i)//2 > congestion and G.degree(j)//2 > congestion and j not in visited_list[highest_degree_i]:
					#print("congestion:", congestion, 'G.degree(j):', G.degree(j))
					flow_value = nx.maximum_flow_value(G,highest_degree_i,j)
					congestion = max(congestion, flow_value)
					visited_list[j].append(highest_degree_i)
					counter += 1
					#print(highest_degree_i, j, "congestion:", congestion)
		while_counter += 1
	print(congestion)
	#print("Counter:", counter)
	#print("--- %s seconds ---" % (time.time() - start_time))
	

nodes = int(input()) #Start
while nodes != 0: #Optimise for duplicated graphs
	if nodes != 1:
		instantiate_graph(nodes)
	else:
		input()
		print(1)
	nodes = int(input())
	
'''import networkx as nx
from networkx.algorithms.flow import edmonds_karp
from networkx.algorithms import approximation as approx

G = nx.DiGraph()
G.add_edge('x','a', capacity=3.0)
G.add_edge('x','b', capacity=1.0)
G.add_edge('a','c', capacity=3.0)
G.add_edge('b','c', capacity=5.0)
G.add_edge('b','d', capacity=4.0)
G.add_edge('d','e', capacity=2.0)
G.add_edge('c','y', capacity=2.0)
G.add_edge('e','y', capacity=3.0)
R = edmonds_karp(G, 'x', 'y')
flow_value = nx.maximum_flow_value(G, 'x', 'y')
print(flow_value)
flow_value == R.graph['flow_value']
'''