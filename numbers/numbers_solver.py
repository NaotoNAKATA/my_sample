# -*- coding: utf-8 -*-


class num_box:
	""" 数字クラス """
	def __init__(self, _len=9, _num=-1):
		""" 初期化 数字未確定のときは-1 """
		self.num = _num
		if(_num==-1):
			self.cand = [i for i in range(1, _len+1) ]
			self.init = False
		else:
			# 初期化時に確定ならTrue(表示のため)
			self.cand = []
			self.init = True
	
	def is_ok(self):
		""" 確定していれば True """
		return (self.num > 0 and len(self.cand)==0)

	def set(self, _num):
		""" 数字を確定させる """
		self.num = _num
		self.cand = []

	def del_cand(self, _cand):
		""" 候補を消す """
		for c in filter(lambda x:x in self.cand, _cand):
			self.cand.remove(c)
	
	def cand_len(self):
		""" 候補の数 """
		return len(self.cand)
	
	def solve(self):
		""" 候補が一つなら確定する """
		if 1==self.cand_len():
			self.num = self.cand[0]
			self.cand = []


class num_set:
	""" 数字のセットクラス """
	def __init__(self, _num_box_list):
		""" num_boxクラスの参照を受け取る """
		self.num_box = _num_box_list
		self.len = len(_num_box_list)

		self.det_num = []
		self.not_det_num = []
		self.update_det()

	def is_ok(self):
		""" セット内の数字がすべて確定していれば True """
		return all( map(lambda x:x.is_ok(), self.num_box) )

	def update_det(self):
		""" 確定リスト、未確定リスト更新 """
		self.det_num = list( map(lambda x:x.num, filter(lambda x:x.is_ok(), self.num_box) ) )
		self.not_det_num = [i for i in range(1, self.len+1) if i not in self.det_num]
	
	def solve1(self):
		""" 確定したリストにある数字を各数字クラスから削除 """
		self.update_det()
		for nb in self.num_box:
			nb.del_cand( self.det_num )
	
	def solve2(self):
		""" 数字クラスのソルバーを起動 """
		for nb in self.num_box:
			nb.solve()
			
	def solve3(self):
		""" 未確定リストの数字で、num_boxの候補の中で、一つしかなかったら確定 """
		# 確定リスト、未確定リスト更新
		self.update_det()

		# 未確定リストを倍
		not_det_num = self.not_det_num + self.not_det_num

		# 未確定リストから、候補数字を削除
		for nb in self.num_box:
			for c in nb.cand:
				if c in not_det_num:
					not_det_num.remove(c)
		
		# 残った数字は、候補が一つだけなので確定する
		for n in not_det_num:
			for nb in self.num_box:
				if n in nb.cand:
					nb.set(n)
					break
			else:
				# ここにきたらおかしい
				pass
	
	def solve4(self):
		""" ２つ組は、候補を絞る """
		cand_pair = list(filter( lambda x:x.cand_len()==2, self.num_box))
		
		# とりあえず、候補を比較して2個以外を削除
		if len(cand_pair)==2:
			if cand_pair[0].cand == cand_pair[1].cand:
				for nb in filter( lambda x:x.cand_len()!=2, self.num_box):
					nb.del_cand( cand_pair[0].cand )
		elif len(cand_pair)==3:
			if cand_pair[0].cand == cand_pair[1].cand:
				for nb in filter( lambda x:x.cand_len()!=2, self.num_box):
					nb.del_cand( cand_pair[0].cand )
			elif cand_pair[0].cand == cand_pair[2].cand:
				for nb in filter( lambda x:x.cand_len()!=2, self.num_box):
					nb.del_cand( cand_pair[0].cand )
			elif cand_pair[1].cand == cand_pair[2].cand:
				for nb in filter( lambda x:x.cand_len()!=2, self.num_box):
					nb.del_cand( cand_pair[1].cand )
		elif len(cand_pair)==4:
			if cand_pair[0].cand == cand_pair[1].cand:
				for nb in filter( lambda x:x.cand_len()!=2, self.num_box):
					nb.del_cand( cand_pair[0].cand )
			elif cand_pair[0].cand == cand_pair[2].cand:
				for nb in filter( lambda x:x.cand_len()!=2, self.num_box):
					nb.del_cand( cand_pair[0].cand )
			elif cand_pair[0].cand == cand_pair[3].cand:
				for nb in filter( lambda x:x.cand_len()!=2, self.num_box):
					nb.del_cand( cand_pair[0].cand )
			elif cand_pair[1].cand == cand_pair[2].cand:
				for nb in filter( lambda x:x.cand_len()!=2, self.num_box):
					nb.del_cand( cand_pair[1].cand )
			elif cand_pair[1].cand == cand_pair[3].cand:
				for nb in filter( lambda x:x.cand_len()!=2, self.num_box):
					nb.del_cand( cand_pair[1].cand )
			elif cand_pair[2].cand == cand_pair[3].cand:
				for nb in filter( lambda x:x.cand_len()!=2, self.num_box):
					nb.del_cand( cand_pair[2].cand )
					
					
					
					
	
	def solve5(self):
		""" 3つ組は、候補を絞る """
		cand_pair = list(filter( lambda x:x.cand_len()==2, self.num_box))
		
		# 決めうちで削除
		if len(cand_pair)==3:
			tri = list( set( cand_pair[0].cand + cand_pair[1].cand + cand_pair[2].cand) )
			if len(tri)==3:
				for nb in filter( lambda x:x.cand_len()!=2, self.num_box):
					nb.del_cand( tri )
			
	def solve(self):
		self.solve1()
		self.solve2()
		self.solve3()
		self.solve4()
		self.solve5()

import xlrd
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell
from xlsxwriter.utility import xl_range
import os

class numbers_solver:
	""" ナンバーズクラス """
	def __init__(self, _q, _template='template.xlsx'):
		""" 初期化 """
		# テンプレートを開く
		book_temp = xlrd.open_workbook(_template)
		self.template = {}
		for name in book_temp.sheet_names():
			self.template[ name ] = {
				'num_box' : {},
				'num_set' : [],
			}
			
			sheet = book_temp.sheet_by_name(name)
			
			for i in range(1, sheet.nrows):
				val = sheet.cell(i,0).value
				if val=='T':
					for j in range(1, sheet.ncols):
						dat = sheet.cell(i,j).value
						self.template[ name ]['num_box'][dat] = (i, j)
				elif val=='G':
					buf = []
					for j in range(1, sheet.ncols):
						dat = sheet.cell(i,j).value
						buf.append(dat)
					self.template[ name ]['num_set'].append(buf)
		
				
		# 問題を開く
		book_q = xlrd.open_workbook(_q)
		self.q = {
			'file_name' : _q,
			'name':{},
		}
		for name in book_q.sheet_names():
			sheet = book_q.sheet_by_name(name)
			self.q['name'][name] = {
				'num_box':{},
				'num_set' : [],
				'template' : '',
			}
	
			template_name = sheet.cell(0,0).value
			self.q['name'][name]['template'] = template_name
			
			for (key, (i,j)) in self.template[ template_name ]['num_box'].items():
				dat = sheet.cell(i,j).value
				if dat=='':
					self.q['name'][name]['num_box'][key] = num_box()
				else:
					self.q['name'][name]['num_box'][key] = num_box( _num=int(dat) )
				
			for g in self.template[ template_name ]['num_set']:
				self.q['name'][name]['num_set'].append(
					num_set(
						[ self.q['name'][name]['num_box'][k] for k in g ]
					)
				)
	def write(self):
		""" 出力する """
		out_file_name = os.path.splitext(self.q['file_name'])[0] + '_solve.xlsx'
		book = xlsxwriter.Workbook(out_file_name)
		format1 = book.add_format({'bold': True, 'bg_color':'#FF0000'})
		
		for sheet_name, val in self.q['name'].items():
			sheet = book.add_worksheet(sheet_name)
			template_name = val['template']
		
			for (key, (i,j)) in self.template[ template_name ]['num_box'].items():
				if val['num_box'][key].init:
					sheet.write(i, j, val['num_box'][key].num ,format1)
				else:
					if val['num_box'][key].num ==-1:
						s = ''
						for c in val['num_box'][key].cand :
							s += str(c) + ','
						sheet.write(i, j,s )
					else:
						sheet.write(i, j, val['num_box'][key].num )
		book.close()
	
	def solve(self):
		for sheet_name, val in self.q['name'].items():
			for i in range(1000):
				for ns in val['num_set']:
					if not ns.is_ok():
						ns.solve()
					
				if all(map(lambda x:x.is_ok(),val['num_set'])):
					break


if __name__ == "__main__":
	
	ns = numbers_solver('sample.xlsx')
	ns.solve()
	ns.write()
	
	