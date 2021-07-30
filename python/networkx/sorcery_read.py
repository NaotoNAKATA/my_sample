# -*- coding: utf-8 -*-

import os
import openpyxl

#
# エクセル読み込み(個別)
#
def read_edge_sheet(edge_sheet):
	# 1行目はヘッダ
	edge = []
	for i in range(2, len(tuple(edge_sheet.rows))+1):
		# 始点ノード
		src = int(edge_sheet.cell(i,1).value)
		
		# 終点ノード
		dst = int(edge_sheet.cell(i,2).value)
		
		dic = {}
		# エッジラベル
		label = edge_sheet.cell(i,3).value
		if label!= None:
			dic['label'] = label
		
		# 選択肢なしフラグ
		flag = edge_sheet.cell(i,4).value
		if flag==1:
			dic['color'] = (1.0,0.0,0.0)

		edge.append((src, dst, dic))
		
	return edge
		
def read_node_sheet(node_sheet):
	node = {}
	for i in range(2, len(tuple(node_sheet.rows))+1):
		# ノード
		n = int(node_sheet.cell(i,1).value)
		
		# 大名称
		map = node_sheet.cell(i,2).value
		
		node_stat = {
			# 位置
			'pos' : (
				int(node_sheet.cell(i,4).value),
				int(node_sheet.cell(i,5).value)),
		}
		
		# ノードラベル
		label = node_sheet.cell(i,3).value
		if label!=None:
			node_stat['label'] = label
	
			
		# スタート-エンドフラグ
		s_e = node_sheet.cell(i,6).value
		#if s_e!=None:
		node_stat['s_e'] = s_e
		
		# ステータス
		status = node_sheet.cell(i,7).value
		if status==-1:
			node_stat['color'] = (1.0,0.0,0.0)
		elif status==4:
			node_stat['color']  = (0.0,1.0,0.0)
			
		# サイズ
		x = node_sheet.cell(i,8).value
		y = node_sheet.cell(i,9).value
		if x!=None and y!=None:
			node_stat['figsize'] = (x, y)
			
		# 出力に追加
		if map in node.keys():
			node[map]['node'].append( (n, node_stat) )
		else:
			node[map] = { 'node' : [ (n , node_stat) ]}
	
	return node
		
#
# エクセル読み込み
#
def read_xlsx(excelFileName):
	# エクセルファイルの読み込み
	book = openpyxl.load_workbook(excelFileName)

	# 全体マップ
	edge_all_sheet = book['NodeIDEdge']
	edge_all = read_edge_sheet(edge_all_sheet)
	
	node_all_sheet = book['NodeID']
	node_all = read_node_sheet(node_all_sheet)
	
	# 各マップ
	node_sheet = book['Node']
	node = read_node_sheet(node_sheet)
	
	edge_sheet = book['Edge']
	edge = read_edge_sheet(edge_sheet)
	
	book.close()
	
	# ノードIDの設定
	node_all['全体図']['oder'] = 0
	node_id_dic = { node_stat['label'] : n for n, node_stat in node_all['全体図']['node'] }
	for map in node.keys():
		node[map]['oder'] = node_id_dic[map]
	
	# figsizeを書き換え
	node_all['全体図']['figsize'] = (20, 20)
	node_figsize_dic = { node_stat['label'] : node_stat['figsize'] for n, node_stat in node_all['全体図']['node'] }
	for map in node.keys():
		node[map]['figsize'] = node_figsize_dic[map]
	
	return node, edge, node_all, edge_all

#
# メイン処理
#
def main(excelFileName):
	# エクセルファイルの読み込み
	node, edge, _, _ = read_xlsx(excelFileName)


if __name__ == '__main__':
	
	main('Sorcery01.xlsx')
	