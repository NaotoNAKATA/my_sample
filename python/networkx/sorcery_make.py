# -*- coding: utf-8 -*-

import networkx as nx

#
# グラフ作成
#
def make_network(node_list, edge, **kwargs):
	# グラフの作成
	G = nx.DiGraph(format='png')
	
	# ノードリストをフラグで分割
	s_node = [ n for n, n_dic in node_list 
			if n_dic['s_e']=='s' ]
	e_node = [ n for n, n_dic in node_list 
			if n_dic['s_e']=='e' ]
	n_node = [ n for n, n_dic in node_list 
			if n_dic['s_e']=='n' ]
	__node = [ n for n, n_dic in node_list 
			if n_dic['s_e']==None ]
	
	# 色付きエッジを最後尾にする
	edge_list = []
	edge_c_list = []
	for (s, e , e_dic) in edge:
		if s in s_node or e in e_node or  s in __node or e in __node:
			if 'color' in e_dic.keys():
				edge_c_list.append( (s, e , e_dic) )
			else:
				edge_list.append( (s, e , e_dic) )
				
	edge_list= edge_list + edge_c_list
	
	# 色付きエッジのノードを最後尾にする
	node_list_i = list( list( zip(*node_list) )[0] )
	for (s, e , e_dic) in edge_c_list:
		i = node_list_i.index(s)
		
		node = node_list.pop(i)
		node_list = node_list + [node]
		
		node_i = node_list_i.pop(i)
		node_list_i = node_list_i + [node_i]
	
	# ノードの追加
	G.add_nodes_from( node_list )
	
	# エッジの追加
	G.add_edges_from( edge_list )
	
	return G

#
# 経路探索
#
def shortest_path(G):
	
	
	
	pass
	
	
	
if __name__ == '__main__':
	
	G=nx.DiGraph()
	
	G.add_edge(1,2,distance=100,cost=100)
	G.add_edge(2,3,distance=150,cost=100)
	G.add_edge(1,3,distance=220,cost=300)
	G.add_edge(3,4,distance=120,cost=200)
	G.add_edge(4,5,distance=10,cost=500)
	
	result = nx.shortest_path(G, source=1, target=5)
	print(result)
	
	result=nx.shortest_path(G,source=1,target=5, weight='distance')
	print(result)

	result = nx.shortest_path(G,source=1,target=5, weight='cost')
	print(result)


	pass