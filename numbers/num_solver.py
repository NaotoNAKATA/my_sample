# -*- coding: utf-8 -*-

import os
import openpyxl
from openpyxl.styles import Font
from openpyxl.styles import PatternFill

from num_box import num_box
from num_group import num_group
from num_template import num_template

class num_solver:
	""" 数独問題クラス """
	def __init__(self, _len=9):
		""" 初期化 """
		# 全数字(num_box)
		self.nb = {}
		
		# 全グループ(num_group)
		self.grp = []
		
		# 最大数字
		self.len = _len
		
	def set(self, _idx, _num=-1):
		""" 数字クラスの登録 """
		self.nb[_idx] = num_box(
				_len=self.len, _num=_num)
	
	def make_group(self, group_list):
		""" グループの作成 """
		num_box_list = []
		for idx in group_list:
			num_box_list.append( self.nb[idx] )
			
		self.grp.append( num_group(num_box_list) )
	
	def is_ok(self):
		""" クラス内の数字がすべて確定していれば True """
		return all( map(lambda x:x.is_ok(), self.nb.values()) )

	def solve(self):
		""" 解く """
		for i in range(30):
			# 各グループのsolverを起動
			for g in self.grp:
				g.solve()
			
			# すべて確定でbreak
			if self.is_ok():
				print('solve...{}'.format(i))
				break
		else:
			print('not solve')
		
class num_read_q:
	""" 数独計算クラス """
	def __init__(self, _path):
		""" 初期化 """
		
		# テンプレート
		self.te = num_template('./template.xlsx')
		
		# 問題の読み込み
		book = openpyxl.load_workbook(_path)
		for sheet in book.worksheets:
			# シート名をキーにする
			name = sheet.title
			print(name)
			
			# テンプレートの選択
			te_tml = self.te.get_tml( sheet['A1'].value )
			te_grp = self.te.get_grp( sheet['A1'].value )
			
			# 問題クラスの初期化
			nq = num_solver(_len=self.te.len)
			
			# テンプレートに従って問題の読み込み
			for idx in te_tml:
				num = sheet[idx].value
				# 空欄のとき
				if num==None:
					num=-1
				nq.set(idx, _num=num)
			
			# グループを作成
			for group_list in te_grp:
				nq.make_group(group_list)
				
			# 問題を解く
			nq.solve()
			
			# 書き出す
			for idx, n in nq.nb.items():
				if n.is_ok():
					sheet[idx].value= n.num
					if n.init==False:
						sheet[idx].font = Font(bold=True, color='FF0000' )
				else:
					#sheet[idx].value= n.cand
					#sheet[idx].font = Font(bold=True)
					sheet[idx].fill = PatternFill(patternType='solid', fgColor='FFFF00')
			
			
			
		# 別名で保存
		path2 = os.path.splitext(_path)
		book.save(path2[0] + '_solve' + path2[1])
			
if __name__ == "__main__":
	num_read_q('./sample.xlsx')
	num_read_q('./ナンプレ_20240306.xlsx')
	