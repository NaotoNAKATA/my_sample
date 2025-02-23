# -*- coding: utf-8 -*-

class num_template:
	""" テンプレートクラス """
	def __init__(self, _path):
		""" 初期化 """
		self.dat = {}
		self.dat['relay'] = {}
		
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
			
			# バージョンシートは飛ばす
			if name == 'version':
				continue
				
			# リレーシートの処理
			if name == 'relay':
				for iter_row in sheet.rows:
					sorce_sheet = iter_row[0].value
					sorce_idx = iter_row[1].value
					dest_sheet = iter_row[2].value
					dest_idx = iter_row[3].value
				
					self.dat['relay'][sorce_sheet] = {
						'idx' : sorce_idx,
						'dest' : dest_sheet,
						'dest_idx' : dest_idx,
					}
				continue
			
			tml = []
			grp = []
			jnt = []
			njnt = []
			ineq = []
			evn = []
			sums = []
			arr = []
			mm = []
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
				elif head=='nJ':
					# (特殊)ジョイントの反転
					row = [ c.value for c in iter_row[1:] if c.value!=None]
					njnt.append(row)
				elif head=='F':
					# (特殊)不等号
					row = [ c.value for c in iter_row[1:] if c.value!=None]
					ineq.append(row)
				elif head=='V':
					# (特殊)偶数
					row = [ c.value for c in iter_row[1:] if c.value!=None]
					evn.append(row)
				elif head=='S':
					# (特殊)足し算
					s = int(iter_row[1].value)
					row = [ c.value for c in iter_row[2:] if c.value!=None]
					sums.append([s, row])
				elif head=='R':
					# (特殊)合計アロー
					row = [ c.value for c in iter_row[1:] if c.value!=None]
					arr.append(row)
				elif head=='M':
					# (特殊)九九
					row = [ c.value for c in iter_row[1:] if c.value!=None]
					mm.append(row)
				elif head=='E':
					len = iter_row[1].value
				else:
					continue
			
			# テンプレートに追加
			self.dat[name]={
				'template' : tml,
				'group' : grp,
				'joint' : jnt,
				'njoint' : njnt,
				'inequal' : ineq,
				'even' : evn,
				'sums' : sums,
				'arrow' : arr,
				'mult' : mm,
				'length' : len,
			}
			
	def get(self, name):
		""" テンプレートの呼び出し """
		if name in  self.dat:
			return self.dat[name]
		else:
				return None
				
	def has_relay(self, name):
		""" リレーがあるかどうか """
		if name in self.dat['relay'].keys():
			return True
		else:
			return False
			
	def get_relay(self, name):
		return self.dat['relay'][name]
		
if __name__ == "__main__":
	te = num_template('./template.xlsx')
	