'''
Coder: Jacky Shew
Description: Finds the length of the longest path starting from vertex 0 in a DAG

Input syntax: First line: No. of Vertices, following lines Adjecency list. Repeat until 0.
(Can always make the program ask but program is used personally so not required)

Input example:
6
1 2 3
2
3 5
4
5
 
6
3 5
2
 
4
 
4
0
'''

def DAG_longest_path(topological_sorted):
	DAG_path = [0] * len(topological_sorted)
	for node,edges in topological_sorted:
		for edge in edges:
			if DAG_path[edge]<=DAG_path[node]+1:
				DAG_path[edge] = DAG_path[node]+1
	return max(DAG_path)

def topological_sort(graph_unsorted):
    graph_sorted = []
    graph_unsorted = dict(graph_unsorted)
    while graph_unsorted:
        acyclic = False
        for node, edges in list(graph_unsorted.items()):
            for edge in edges:
                if edge in graph_unsorted:
                    break
            else:
                acyclic = True
                del graph_unsorted[node]
                graph_sorted.insert(0,(node, edges))
    return graph_sorted
	
def graph_list_prepare(extracted_input):
	total_vertices = int(extracted_input[0][0])
	if total_vertices == 0:
		return "The End"
	if total_vertices < 1:
		del extracted_input[0:2]
		return "False Value"
	graph_unsorted = extracted_input[1:total_vertices+1]
	for n in range(total_vertices):
		graph_unsorted[n] = tuple([n,list(graph_unsorted[n][0])])
		graph_unsorted[n] = tuple([n,list(map(int,''.join(graph_unsorted[n][1]).split()))])
	del extracted_input[0:total_vertices+1]
	return graph_unsorted
		
def input_extraction():
	matrix = ''
	matrix_list = []
	while matrix != '0':
		matrix = input()
		matrix_list.append(matrix)
	extracted_input = []
	for i in matrix_list:
		extracted_input.append(list([i.strip('\n')]))
	return extracted_input

graph_unsorted = ''
extracted_input = input_extraction()
DAG_max_length_list = []
while graph_unsorted != "The End" :
	graph_unsorted = graph_list_prepare(extracted_input)
	if graph_unsorted != "False Value":
		if graph_unsorted != "The End":	
			topological_sorted = topological_sort(graph_unsorted)
			DAG_max_length_list.append(DAG_longest_path(topological_sorted))
	else:
		DAG_max_length_list.append(0)
for i in DAG_max_length_list:
	print(i)