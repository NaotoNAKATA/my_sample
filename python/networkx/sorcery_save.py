# -*- coding: utf-8 -*-

import os

import networkx as nx

#
# グラフ出力
#
def save_network(G, **kwargs, ):
	
	import numpy as np
	import matplotlib.pyplot as plt
	from matplotlib.font_manager import FontProperties
	
	# 引数取得
	title = kwargs['title']
	out_file = kwargs['out_file']
	figsize = kwargs['figsize']
	
	# フォントの読み込み
	fp = FontProperties(
		fname='./fonts/GenShinGothic-Normal.ttf', size=8)
	
	# 描画オブジェクトの作成
	fig = plt.figure(
		figsize=figsize,
	)

	# タイトルの設定
	fig.suptitle( title,
		fontproperties=fp,
		)

	# 描画エリアの追加
	ax = fig.add_subplot(111)
	
	# 枠線を消す
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	ax.spines['bottom'].set_visible(False)
	ax.spines['left'].set_visible(False)
	
	#
	# グラフの描画
	#
	
	# ノードの色を指定する
	node_color = []
	for n in G.nodes():
		if 'color' in G.nodes[n].keys():
			node_color.append( G.nodes[n]['color'] )
		else:
			node_color.append( '#1f78b4' )

	# エッジの色を指定する
	edge_color = []
	for e in G.edges():
		if  'color' in G.edges[e].keys():
			edge_color.append( G.edges[e]['color'] )
		else:
			edge_color.append('k')
	
	# ノードのラベルを追加する
	node_label = {}
	for n in G.nodes():
		if 'label' in G.nodes[n].keys():
			node_label[n] = '{0}\n{1}'.format(n, G.nodes[n]['label'])
		else:
			node_label[n] = n
	
	# エッジのラベルを追加する
	edge_label = {}
	for e in G.edges():
		if  'label' in G.edges[e].keys():
			edge_label[e] = G.edges[e]['label']
	
	# ノードの位置を指定する
	pos = {}
	for n in G.nodes():
		if 'pos' in G.nodes[n].keys():
			pos[n] = G.nodes[n]['pos']
		else:
			pos[n] = (10,10-len(pos))
	
	# グラフを描画(ノード、エッジ)
	nx.draw_networkx(G,
		pos=pos,
		#node_color=node_color,
		node_color=np.asanyarray(node_color, dtype=object),
		edge_color=edge_color,
		with_labels=False,
		node_size=600,
		ax=ax,
	)
	
	# ノードのラベルを描画
	nx_node = nx.draw_networkx_labels(G,
		pos=pos,
	    labels=node_label,
		ax=ax,
		font_size=8,
	)
	
	# ノードラベルを日本語化
	for t in nx_node.values():
	    t.set_fontproperties(fp)
	
	# エッジのラベルを描画
	nx_edge = nx.draw_networkx_edge_labels(G,
		pos=pos,
		edge_labels=edge_label,
		ax=ax,
		font_size=8,
	)
	
	# エッジラベルを日本語化
	for t in nx_edge.values():
	    t.set_fontproperties(fp)
	
	# 出力
	fig.savefig(out_file)
	
	fig.clf()
	plt.close()
	
#
# メイン処理
#
def main():
	# グラフの作成
	G = nx.DiGraph(format='png')
	
	# ノードの追加
	G.add_node(1)
	G.add_nodes_from([
		(2, {'color':(1.0,0.0,0.0)}),
		(3, {'color':(0.0,1.0,0.0)}),
		(4, {'color':(0.0,0.0,1.0)}),
	])
	#G.add_nodes_from([2,3,4])
	
	#G.nodes[2]['color'] = (1.0,0.0,0.0)
	#G.nodes[3]['color'] = (0.0,1.0,0.0)
	#G.nodes[4]['color'] = (0.0,0.0,1.0)
	
	G.nodes[1]['label'] = 'スタート'
	
	G.nodes[1]['pos'] = (0, 10)
	G.nodes[2]['pos'] = (0, 9)
	G.nodes[3]['pos'] = (-1, 8)
	G.nodes[4]['pos'] = (1, 8)
	
	# エッジの追加
	G.add_edge(1,2)
	G.add_edges_from([
		#(2,3),
		(2,3,{'color':(1.0,0.0,0.0), 'label':'鍵'}),
		(2,4),
	])
	
	#G.edges[2,3]['color'] = (1.0,0.0,0.0)
	#G.edges[2,3]['label'] = '鍵'
	G.edges[1,2]['label'] = 'from town'
	
	# 出力
	save_network(G,
		title='テスト',
		out_file='テスト.png',
		figsize=(20,20),
	)


if __name__ == '__main__':
	
	main()

	