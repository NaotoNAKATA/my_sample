# -*- coding: utf-8 -*-

class num_template:
	""" テンプレートクラス """
	def __init__(self, _path):
		""" 初期化 """
		self.tml = {}
		self.grp = {}
		self.len = 9
		
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
			
			# データの読み込み
			for iter_row in sheet.rows:
				head = iter_row[0].value
				
				# ヘッダがT(template),G(group)のみを処理
				if head=='T':
					# 数字が入る箱
					row = [ c.value for c in iter_row[1:] if c.value!=None]
					tml += row
				elif head=='G':
					# グループの読み込み
					row = [ c.value for c in iter_row[1:] if c.value!=None]
					grp.append(row)
				elif head=='E':
					self.len = iter_row[1].value
				else:
					continue
			
			# テンプレートに追加
			self.tml[name] = tml
			self.grp[name] = grp
			
	def get_grp(self, name):
		""" テンプレートの呼び出し """
		return self.grp[name]
					
	def get_tml(self, name):
		""" テンプレートの呼び出し """
		return self.tml[name]		

if __name__ == "__main__":
	te = num_template('./template.xlsx')
	