import networkx as n
import matplotlib.pyplot as p
G = n.Graph()
G.add_edges_from([(5, 6), (8, 6), (5, 2), (9, 3),
                 (4, 2), (8, 1), (8, 2), (3, 6)])
print(n.adjacency_matrix(G).todense())
n.draw_networkx(G, with_labels=True, node_color='purple', node_shape='s')
p.xlabel('X-axis')
p.ylabel('Y-axis')
p.title('Graph')
p.show()
