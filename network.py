import networkx as nx
from matplotlib import pyplot as plt


def	create_graph():
	return nx.Graph()

def	add_sub_list(G, head, node_list):

	for i in range(len(node_list)):
		G.add_edge(head['name'], node_list[i]['name'])

def	display_graph(graph):
	
	fig, ax = plt.subplots(nrows=1, ncols=1)
	ax.set_facecolor("grey")
	nx.draw(graph, with_labels=True, node_size=1000, node_color="skyblue", node_shape="s", alpha=1, linewidths=40)
	plt.draw()
	plt.show()
