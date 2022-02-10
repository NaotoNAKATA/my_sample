# -*- coding: utf-8 -*-

import os
import networkx as nx

import sorcery_read
import sorcery_make
import sorcery_save

#
# メイン処理
#
def main(excelFileName):
	# ディレクトリの作成
	out_dir = os.path.splitext(
			os.path.basename( excelFileName ) )[0]
	
	if not os.path.exists( out_dir ):
		os.makedirs( out_dir )
	
	# エクセルファイルの読み込み
	node, edge, node_all, edge_all = sorcery_read.read_xlsx(excelFileName)
	
	# 全体図描画
	if True:
	#if False:
		map_all = '全体図'
		node_all_list = node_all[map_all]['node']
		node_all_oder = node_all[map_all]['oder']
		figsize_all = node_all[map_all]['figsize']
		
		# グラフの作成
		G = sorcery_make.make_network(node_all_list, edge_all)
		
		# 出力ファイル名
		out_file_all = '{0}/{1:0>2}_{2}.png'.format(
					out_dir, node_all_oder, map_all)
		
		print(os.path.basename(out_file_all))
		
		# グラフの出力
		sorcery_save.save_network(G,
			title=map_all,
			out_file=out_file_all,
			figsize=figsize_all,
		)
	
	# 各マップ毎に、グラフ作成して描画
	for map, map_dict in node.items():
		node_list = map_dict['node']
		node_oder = map_dict['oder']
		figsize = map_dict['figsize']
		
		# デバッグ用 特定のマップのみ処理
		if True:
		#if False:
			if node_oder!=8:
				continue
		
		# グラフの作成
		G = sorcery_make.make_network(node_list, edge)
		
		# 出力ファイル名
		out_file = '{0}/{1:0>2}_{2}.png'.format(
					out_dir, node_oder, map)
					
		print(os.path.basename(out_file))
	
		# グラフの出力
		sorcery_save.save_network(G,
			title=map,
			out_file=out_file,
			figsize=figsize,
		)
		
if __name__ == '__main__':
	
#	main('Sorcery01.xlsx')
#	main('Sorcery02.xlsx')
	main('Sorcery03.xlsx')
#	main('Sorcery04.xlsx')
	