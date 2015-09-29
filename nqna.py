#-*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from openpyxl.workbook import Workbook
from openpyxl import load_workbook


q_id={0:23, 1:10, 2:39, 3:44, 4:14, 5:33, 6:21, 7:66, 8:88, 9:11}
q_label={0:1, 1:4, 2:0, 3:2, 4:3, 5:4, 6:1, 7:2, 8:2, 9:1}
q_exemplar={0:23, 1:39, 2:44, 3:14, 4:33}

G_q = np.matrix([\
	[1, 0, 1, 0, 0],\
	[0, 1, 0, 0, 1],\
	[1, 0, 1, 1, 0],\
	[0, 0, 1, 1, 0],\
	[0, 1, 0, 0, 1]])

labels={}

def draw_graph(graph):
	# extract nodes from graph
	nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])

	# create networkx graph
	G=nx.Graph()

	# add nodes
	for node in nodes:
		labels[node]=node
		G.add_node(node)

	# add edges
	for edge in graph:
		G.add_edge(edge[0], edge[1])

	# draw graph
		pos = nx.shell_layout(G)
		nx.draw(G, pos)
		nx.draw_networkx_labels(G, pos, labels)

	# save as png
	plt.savefig("./png/connection_path.png") 

	# show graph
	plt.show()

# same label finding
def find_same_label(q_label):
	for k, v in q_label.iteritems():
		inv_label[v] = inv_label.get(v, [])
		inv_label[v].append(k)

def create_connect(q_id, q_exemplar, G_q):
	for i in range(0, G_q.shape[0]):
		for j in range(0, G_q.shape[1]):
			if str(i) not in str(j):
				if (G_q[i, j])==1:
					graph.append((q_exemplar[i],q_exemplar[j]))	

	for k in range(0, len(inv_label)):
		v_size = len(inv_label[k])

		for h in range(0, v_size):
			graph.append((q_exemplar[k],q_id[inv_label[k][h]]))

	draw_graph(graph)

def write_excel_result(q_id, q_label, q_exemplar, G_q, excel_path, sheet_count):
	print " creating excel result....."
	wb=Workbook()

	for i in range(1,sheet_count):
		ws = wb.create_sheet()
	
	sheetList = wb.get_sheet_names()
	first = wb.get_sheet_by_name(sheetList[0])

	# write column name
	first.cell(row=1, column=1).value = 'id'
	first.cell(row=1, column=2).value = 'label'
	first.cell(row=1, column=3).value = 'exemplar'

	# ID input
	for k, v in q_id.iteritems():
		first.cell(row=k+2, column=1).value = v # start of 'k' is '2' 
		first.cell(row=k+2, column=3).value = 0 # init value = 0 

	# Level input
	for k, v in q_label.iteritems():
		first.cell(row=k+2, column=2).value = v # start of 'k' is '2' 


	# Exemplar input
	for k, v in q_id.iteritems():
		for j, h in q_exemplar.iteritems():
			if first.cell(row=k+1, column=1).value == h : 
				first.cell(row=k+1, column=3).value = 1 
	# second sheet
	# matrix input
	second = wb.get_sheet_by_name(sheetList[1])

	for i in range(1, G_q.shape[0]+1): 
		second.cell(row=1, column=i+1).value = i 

	for j in range(1, G_q.shape[0]+1): 
		second.cell(row=j+1, column=1).value = j 

	for m in range(0, G_q.shape[0]):
		for n in range(0, G_q.shape[1]):
			second.cell(row=m+2, column=n+2).value = G_q[m,n]

	# third sheet
	# same group
	third = wb.get_sheet_by_name(sheetList[2])

	for k, v in q_id.iteritems():
		third.cell(row=k+2, column=1).value = v #  
		third.cell(row=1, column=k+2).value = v # 

		for i, j in q_label.iteritems():
			if q_label[k]==q_label[i]:
				third.cell(row=k+2, column=i+2).value = 0 
	
	#def one_depth_connect(ii,jj):
	#	for kk, vv in q_id.iteritems():
	#		for i_k, j_v in q_label.iteritems():
	#			if q_label[kk]==ii and q_label[i_k]==jj:
	#				third.cell(row=kk+2, column=i_k+2).value = 1 

	# 1 depth connection
	for i in range(0, G_q.shape[0]):
		for j in range(0, G_q.shape[1]):
			if str(i) not in str(j):
				if (G_q[i, j])==1:
					for kk, vv in q_id.iteritems():
						for i_k, j_v in q_label.iteritems():
							if q_label[kk]==i and q_label[i_k]==j:
								third.cell(row=kk+2, column=i_k+2).value = 1 

					
	wb.save(excel_path)
	print " save excel result "
	

# parameter
graph = []
inv_label = {}
excel_path = './result.xlsx'
sheet_count = 4

if __name__ == "__main__":
	print " running news quatation network analysis....."

	# for fiding same label
	find_same_label(q_label)

	# excel id, label, exemplar, G_q(matrix) result
	write_excel_result(q_id, q_label, q_exemplar, G_q, excel_path, sheet_count)
	
	# make graph
	create_connect(q_id, q_exemplar, G_q)



