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
						
	def solve(self):
		self.solve1()
		self.solve2()
		self.solve3()
		self.solve4()

class numbers_solver:
	""" ナンバーズクラス """
	def __init__(self):
		pass
		
		