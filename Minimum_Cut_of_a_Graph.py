import random
import copy
import math

#Input file contains adjacency matrix with vertices that are adjacent to each vertex
#The graph is defined as an adjacency list instead of an adjacency matrix, especially as the graph is a sparse graph
with open("MinCut.txt") as f:
	content = [line.strip('\t').split() for line in f.readlines()];

#Converting the input text file into a dictionary in Python
#The first entry in each line acts as the key to the dictionary, and the rest of the line is the list stored at that key location
#The number of entries in the dictionary is the total number of vertices in the graph
input_dict = {d[0]: d[1:] for d in content};
no_of_vertices = len(input_dict);

#An edge is chosen at random from the graph - done by choosing two vertices at random
#The first vertex is chosen from the keys of the dictionary
#Second vertex is chosen from the adjacency list at that key location
#This method does not guarantee equal probability for all edges but its the easiest way to choose an edge at random without building the whole graph
def choose_edge(dict):
	vertex1 = list(dict.keys())[random.randint(0, len(dict) - 1)];
	vertex2 = dict[vertex1][random.randint(0, len(dict[vertex1]) - 1)];
	return vertex1, vertex2;

#An edge is chosen at random till only two vertices are left in the graph
#Add the adjacency list of the second vertex to the first, replace the second vertex with the first vertex, remove all self loops
#The length of the adjacency list when only two vertices are remaining is the minimum cut of the graph
def min_cut_calculation(dict):
	while len(dict) > 2:
		vertex1, vertex2 = choose_edge(dict);
		dict[vertex1].extend(dict[vertex2]);
		for entry in dict[vertex2]:
			for connection in range(0, len(dict[entry])):
				if dict[entry][connection] == vertex2:
					dict[entry][connection] = vertex1;
		while vertex1 in dict[vertex1]:
				dict[vertex1].remove(vertex1);
		del dict[vertex2];
	return len(dict[list(dict.keys())[0]])

#For one iteration the probability that we get the correct cut value is 2/n(n - 1) where n is the number of vertices
#This is a very low probability, but if we increase the number of runs, the probability can be improved to a much better value
#Typically running the program (n^2)*log(n) times ensures that the probability of failure is 1/n
#the function deepcopy() is used to return a copy of a compound object by copying all information of the original object into the new object
min_cut = min_cut_calculation(copy.deepcopy(input_dict));
for i in range(0, int(no_of_vertices*no_of_vertices*log(no_of_vertices))):
	min_cut_new = min_cut_calculation(copy.deepcopy(input_dict));
	if min_cut_new < min_cut:
		min_cut = min_cut_new;
print("The minimum cut of the given graph is:", min_cut)
