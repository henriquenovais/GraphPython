import networkx as nx
import matplotlib.pyplot as plt
#-----------------------------------------
# FILE DEDICATED TO PROTOTYPING FEATURES
#-----------------------------------------

g = nx.Graph()
#g.add_edges_from([(1, 2, {'color': 'blue'}), (2, 3, {'weight': 8})])
g.add_edge(1, 2, weight=4.7 )
labels = nx.get_edge_attributes(g,'weight')
nx.draw_networkx_edge_labels(g,pos=nx.spring_layout(g),edge_labels=labels)
nx.draw(g, with_labels = True)
plt.show()
'''
G=nx.Graph()
i=1
G.add_node(i)
G.add_node(2)
G.add_node('')
G.add_edge(1,2,weight=0.5)
G.add_edge(1,3,weight=9.8)
pos=nx.get_node_attributes(G,'pos')
nx.draw(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()
nx.draw(g, with_labels = True)
'''