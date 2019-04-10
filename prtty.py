import networkx as nx
import matplotlib.pyplot as plt
#-----------------------------------------
# FILE DEDICATED TO PROTOTYPING FEATURES
#-----------------------------------------
g = nx.DiGraph()
g.add_node('A')
g.add_node('B')
g.add_weighted_edges_from([('A','B',1)])

nx.draw(g, with_labels = True)
plt.show()