# -*- coding: utf-8 -*-

import networkx as nx

#
# グラフ作成
#
def make_network(node_list, edge, **kwargs):
	# グラフの作成
	G = nx.DiGraph(format='png')
	
	# ノードの追加
	G.add_nodes_from( node_list )
	
	# ノードリストをフラグで分割
	s_node = [ n for n, n_dic in node_list 
			if n_dic['s_e']=='s' ]
	e_node = [ n for n, n_dic in node_list 
			if n_dic['s_e']=='e' ]
	n_node = [ n for n, n_dic in node_list 
			if n_dic['s_e']=='n' ]
	__node = [ n for n, n_dic in node_list 
			if n_dic['s_e']==None ]
	
	# エッジの追加
	edge_list = []
	for (s, e , e_dic) in edge:
		if s in s_node or e in e_node:
			edge_list.append( (s, e , e_dic) )
		elif s in __node or e in __node:
			edge_list.append( (s, e , e_dic) )
		
	G.add_edges_from( edge_list )
		
	return G
	