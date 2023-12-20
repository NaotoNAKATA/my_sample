# -*- coding: utf-8 -*-

import os
import openpyxl
from openpyxl.styles import Font
from openpyxl.styles import PatternFill

from num_solver import num_solver
from num_template import num_template
		
class num_read_q:
	""" 数独問題読み込みクラス """
	def __init__(self, _path, _temp):
		""" 初期化 """
		
		# テンプレートの読み込み
		self.te = num_template(_temp)
		
		# 問題の読み込み
		book = openpyxl.load_workbook(_path)
		
		for sheet in book.worksheets:
			# シート名をキーにする
			name = sheet.title
			print(name)
			
			# テンプレートの選択
			te = self.te.get( sheet['A1'].value )
			
			# 問題クラスの初期化
			nq = num_solver(te)
			
			# テンプレートに従って問題の読み込み
			for idx in te['template']:
				num = sheet[idx].value
				# 空欄のとき
				if num==None:
					num=-1
				nq.set(idx, _num=num)
			
			# 問題クラスの構築
			nq.configure(te)
			
			# 問題を解く
			nq.solve()
			
			# 解答を書き出す
			for idx, n in nq.nb.items():
				if n.is_ok():
					sheet[idx].value= n.num
					if n.init==False:
						sheet[idx].font = Font(bold=True, color='FF0000' )
				else:
					val ='('
					for c in  n.cand:
						val+='{},'.format(c)
					val +=')'
					sheet[idx].value= val
					sheet[idx].fill = PatternFill(patternType='solid', fgColor='FFFF00')
		
		# 別名で保存
		path2 = os.path.splitext(_path)
		book.save(path2[0] + '_solve' + path2[1])
			
if __name__ == "__main__":
	q_book = [
		['./sample.xlsx', './template.xlsx'],
		['./ナンプレ_20240306.xlsx', './template.xlsx',],
		['./ナンプレ_20240306_2.xlsx', './template_20240306.xlsx',],
	]
	for qb, te in q_book:
		print(qb)
		num_read_q(qb, te)
