#-*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from openpyxl.workbook import Workbook
from openpyxl import load_workbook

from na_config import * 
import na_tools as nt
import na_build

# parameter
graph = []
inv_label = {}

labels={}
 
NewsQuoObjs=nt.loadObjectBinaryFast(NEWS_QUO_OBJ)

#for (qid, obj_) in NewsQuoObjs:
#	for key in obj_.__dict__.items():
#		if key[0]=='quotation':
#			print key[1][0:10]

#try:
#	print 'loading ' +NEWS_QUO_OBJ
#	NewsQuoObjs=nt.loadObjectBinaryFast(NEWS_QUO_OBJ)
#except:
#	status_out=build_NewsQuoObjs()
#	print status_out
#	if status_out!=True:
#		print status_outNEWS_SRC_OBJ
#	print 'job done, and stored news quotation objects...'
#	NewsQuoObjs=nt.loadObjectBinaryFast(NEWS_QUO_OBJ)

#if argv_print==True:
#	print '********************************************************************'
#	print 'Print News Quotation Objects- NewsQuoObjs '
#	for (qid, obj_) in NewsQuoObjs:
#		print '==================================================='
#		print 'Quotation ID : ', qid
#		print '==================================================='
#		obj_.whoami()
#	print '********************************************************************'

def draw_graph(graph, q_exemplar):
	# extract nodes from graph
	nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])

	# create networkx graph
	G=nx.Graph()


	for (qid, obj_) in NewsQuoObjs:
		# add nodes
		for node in nodes:
			if qid==node:
				for key in obj_.__dict__.items():
					if key[0]=='quotation':
						#print key[1][0:10]
						labels[node]=str(node) +'\n'+ key[1][0:10]
				G.add_node(node)
					
	# add nodes
	#for node in nodes:
	#	labels[node]=node
	#	G.add_node(node)

	# add edges
	for edge in graph:
		G.add_edge(edge[0], edge[1])

	# draw graph
	#pos = nx.shell_layout(G)
	pos = nx.spring_layout(G)
	#pos = nx.random_layout(G)
	
	q_exemplar_node = [] 

	for k, v in q_exemplar.iteritems():
		q_exemplar_node.append(v)

	nx.draw(G, pos, node_size=200, font_size=5, node_color='r', nodelist=nodes)
	nx.draw(G, pos, node_size=300, font_size=5, node_color='r', nodelist=q_exemplar_node)
	nx.draw_networkx_labels(G, pos, labels)

	# save as png
	plt.savefig(SAVE_CONNECTION) 

	# show graph
	#plt.text(0,0,s='some text', bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center')
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
			if str(q_exemplar[k]) not in str(q_id[inv_label[k][h]]):
				#print str(q_exemplar[k]), str(q_id[inv_label[k][h]])
				graph.append((q_exemplar[k],q_id[inv_label[k][h]]))

	draw_graph(graph, q_exemplar)

def write_excel_result(q_id, q_label, q_exemplar, G_q, RESULT_EXCEL, SHEET_COUNT):
	print " creating excel result....."
	wb=Workbook()

	for i in range(1,SHEET_COUNT):
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

	# 1 depth connection
	for i in range(0, G_q.shape[0]):
		for j in range(0, G_q.shape[1]):
			if str(i) not in str(j):
				if (G_q[i, j])==1:
					#print i, j
					for kk, vv in q_id.iteritems():
						for i_k, j_v in q_label.iteritems():
							if q_label[kk]==i and q_label[i_k]==j:
								third.cell(row=kk+2, column=i_k+2).value = 1 
	# forth sheet
	# 2 depth connection

					
	wb.save(RESULT_EXCEL)
	print " save excel result "
	

