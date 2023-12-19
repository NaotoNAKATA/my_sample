# -*- coding: utf-8 -*-

class num_template:
	""" テンプレートクラス """
	def __init__(self, _path):
		""" 初期化 """
		self.dat = {}
		
		# テンプレートファイルの読み込み
		self.read_xlsx(_path)
		
	def read_xlsx(self, _path):
		""" テンプレートファイルの読み込み """
		import openpyxl
		book = openpyxl.load_workbook(_path, data_only=True)
		
		# 1シートに1テンプレート
		for sheet in book.worksheets:
			# シート名をキーにする
			name = sheet.title
			tml = []
			grp = []
			jnt = []
			ineq = []
			evn = []
			len = 9
			
			# データの読み込み
			for iter_row in sheet.rows:
				head = iter_row[0].value
				
				# ヘッダの処理
				if head=='T':
					# 数字が入る箱
					row = [ c.value for c in iter_row[1:] if c.value!=None]
					tml += row
				elif head=='G':
					# グループの読み込み
					row = [ c.value for c in iter_row[1:] if c.value!=None]
					grp.append(row)
				elif head=='J':
					# (特殊)ジョイント
					row = [ c.value for c in iter_row[1:] if c.value!=None]
					jnt.append(row)
				elif head=='F':
					# (特殊)不等号
					row = [ c.value for c in iter_row[1:] if c.value!=None]
					ineq.append(row)
				elif head=='V':
					# (特殊)偶数
					row = [ c.value for c in iter_row[1:] if c.value!=None]
					evn.append(row)
				elif head=='E':
					len = iter_row[1].value
				else:
					continue
			
			# テンプレートに追加
			self.dat[name]={
				'template' : tml,
				'group' : grp,
				'joint' : jnt,
				'inequal' : ineq,
				'even' : evn,
				'length' : len,
			}
			
	def get(self, name):
		""" テンプレートの呼び出し """
		return self.dat[name]
		
if __name__ == "__main__":
	te = num_template('./template.xlsx')
	