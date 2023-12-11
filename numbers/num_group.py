# -*- coding: utf-8 -*-

from num_box import num_box

class num_group:
	""" 数字クラスのグループ """
	def __init__(self, _num_box_list):
		""" num_boxクラスの参照を受け取る """
		self.nb_list = _num_box_list
		self.len = len(_num_box_list)

		# 確定リスト(グループ内で確定している数字)
		self.det_num = []
		
		# 未確定リスト
		self.not_det_num = []
		
		# 確定、未確定リスト更新
		self.update_det()

	def is_ok(self):
		""" セット内の数字がすべて確定していれば True """
		return all( map(lambda x:x.is_ok(), self.nb_list) )

	def update_det(self):
		""" 確定リスト、未確定リスト更新 """
		self.det_num = list(
			map(lambda x:x.num,
				filter(lambda x:x.is_ok(), self.nb_list)
			)
		)
		self.not_det_num = [i for i in range(1, self.len+1) if i not in self.det_num]
	
	def solve1(self):
		""" 確定したリストにある数字を各数字クラスから削除 """
		self.update_det()
		for nb in self.nb_list:
			nb.del_cand( self.det_num )
	
	def solve2(self):
		""" 数字クラスのソルバーを起動 """
		for nb in self.nb_list:
			nb.solve()
			
	def solve3(self):
		""" 未確定リストの数字で、num_boxの候補の中で、一つしかなかったら確定 """
		# 確定リスト、未確定リスト更新
		self.update_det()

		# 未確定リストを倍
		not_det_num = self.not_det_num + self.not_det_num

		# 未確定リストから、候補数字を削除
		for nb in self.nb_list:
			for c in nb.cand:
				if c in not_det_num:
					not_det_num.remove(c)
		
		# 残った数字は、候補が一つだけなので確定する
		for n in not_det_num:
			for nb in self.nb_list:
				if n in nb.cand:
					nb.set(n)
					break
			else:
				# ここにきたらおかしい
				pass
	
	def solve4(self):
		""" ２つ組は、候補を絞る """
		cand_pair = list(
			filter( lambda x:x.cand_len()==2, self.nb_list)
			)
		
		if len(cand_pair)>=2:
			for i in range( len(cand_pair)-1 ):
				for j in range(i+1, len(cand_pair) ):
					if cand_pair[i].cand == cand_pair[j].cand:
						for nb in filter( lambda x:x.cand_len()!=2, self.nb_list):
							nb.del_cand( cand_pair[i].cand )
						break
	
	def solve5(self):
		""" 3つ組は、候補を絞る """
		cand_pair = list(filter( lambda x:x.cand_len()==2, self.nb_list))
		
		# 決めうちで削除
		if len(cand_pair)==3:
			tri = list( set( cand_pair[0].cand + cand_pair[1].cand + cand_pair[2].cand) )
			if len(tri)==3:
				for nb in filter( lambda x:x.cand_len()!=2, self.nb_list):
					nb.del_cand( tri )
			
	def solve(self):
		if self.is_ok():
			return
			
		self.solve1()
		self.solve2()
		self.solve3()
		self.solve4()
		self.solve5()
