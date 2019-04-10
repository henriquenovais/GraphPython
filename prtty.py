import networkx as nx
import matplotlib.pyplot as plt
#-----------------------------------------
# FILE DEDICATED TO PROTOTYPING FEATURES
#-----------------------------------------
g = nx.DiGraph()
g.add_weighted_edges_from([(1,2,1), (3,1,1)])


nx.draw(g, with_labels = True)
plt.show()