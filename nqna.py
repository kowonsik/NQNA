#-*- coding: utf-8 -*-
from __future__ import division # To forace float point division

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


q_id={1:10, 2:39, 3:44, 4:14, 5:33, 6:21, 7:65, 8:88, 9:11, 10:23}

q_label={1:1, 2:1, 3:2, 4:3, 5:2, 6:3, 7:3, 8:3, 9:2, 10:2}

q_exemplar={1:39, 2:44, 3:88, 4:11, 5:23}

G_q = np.matrix([\
	[1, 0, 1, 0, 0],\
	[0, 1, 0, 0, 1],\
	[1, 0, 1, 1, 0],\
	[0, 0, 1, 1, 0],\
	[0, 1, 0, 0, 1]])

#def draw_net():
#	try:
#		G=nx.path_graph(8)
#		nx.draw(G)
#		#plt.savefig("simple_path.png") # save as png
#		plt.show() # display
#	except:
#	        raise



if __name__ == "__main__":
	print " running news quatation network analysis....."

	# 동일 label을 찾기 위한 작업
	inv_label = {}
	for k, v in q_label.iteritems():
		inv_label[v] = inv_label.get(v, [])
		inv_label[v].append(k)

	print inv_label

	G=[None]*len(inv_label)

	for i, k in enumerate(inv_label):
		print i,inv_label[k] 
		G[i] = nx.DiGraph()
		G[i].add_path(inv_label[k])
		#nx.draw(G[i],pos=nx.spring_layout(G[i]))
		nx.draw_networkx(G[i])

	#for i in items(inv_label):
	#	G[i] = nx.DiGraph()
	#	G[i].add_path(j)
	#	nx.draw(G[i])

	#print inv_label[1][0]
	#H=nx.path_graph(q_num)
	#G.add_nodes_from(H)

	#nx.draw(G1)
	#nx.draw(G2)
	plt.show()

