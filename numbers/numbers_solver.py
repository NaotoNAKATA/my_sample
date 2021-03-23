# -*- coding: utf-8 -*-


class num_box:
	""" 数字クラス """
	def __init__(self, _len=9):
		""" 初期化 数字未確定のときは-1 """
		self.num = -1
		self.cand = [i for i in range(1, _len+1) ]
	
	def is_ok(self):
		""" 確定していれば True """
		return (self.num > 0)

	def set(self, _num):
		""" 数字を確定させる """
		self.num = _num
		self.cand = []

	def del_cand(self. _cand):
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
		self.not_det_num = list( map(lambda x:x.num, filter(lambda x:not x.is_ok(), self.num_box) ) )
	
	def solve1(self):
		""" 確定したリストにある数字を各数字クラスから削除 """
		map(lambda x:x.del_cand( self.det_num ), self.num_box)
	
	def solve2(self):
		""" 数字クラスのソルバーを起動 """
		map(lambda x:x.solve(), self.num_box)
			
	def solve3(self):
		""" 未確定リストの数字で、num_boxの候補の中で、一つしかなかったら確定 """
		# 確定リスト、未確定リスト更新
		self.update_det()

		# 未確定リストを倍
		not_det_num = self.not_det_num + self.not_det_num

		# 未確定リストで残った数字があればそれば確定できるはず






#class num_box:
#	def __init__(self, _num_len=9):
#		num = [i for i in range(1, _num_len+1) ]
#	
#	def is_ok(self):
#		return len(self.num)==1
#	
#	def has_num(self. _num):
#		return _num in self.num
#		
#	def del_num(self. _num):
#		if not self.is_ok() and self.has_num(_num):
#			self.num.remove(_num)
#	
#	def set_num(self, _num):
#		self.num = [_num]
#	
#class comb_box:
#	def __init__(self, _num_len=9):
#		comb = [ num_box(_num_len) for i in range(_num_len) ]
#		num_len = _num_len
#
#	def is_ok(self):
#		return False not in map(lambda x:x.is_ok(), self.comb)
#	
#	def solve(self):
#		self.check1()
#		self.check2()
#		self.check3()
#	
#	def check1(self):
#		""" ボックス内で確定した数字があるときは、他のボックスから候補を削除しておく """
#		num_ok = map(lambda x:x.num[0], filter(lambda x:x.is_ok() , self.comb) )
#		for n in num_ok:
#			map(lambda x:x.del_num(n), self.comb)
#
#	def check2(self):
#		""" 他のボックスの候補が無いときは、数字を確定する """
#		num_ok = list( map(lambda x:x.num[0], filter(lambda x:x.is_ok() , self.comb) ) )
#		num_cand = [ i for i in range(1, self.num_len+1) if i not in num_ok]
#
#		for n in num_cand:
#			c = filter(lambda x:x.has_num(n), self.comb)
#			if len(c)==1:
#				c[0].set_num(n)
#
#	def check3(self):
#		""" ２つ組は、候補を絞る """
#		pair = filter(lambda x:len(x.num)==2, self.comb)
#		if len(pair)>=2:
#			for i in range(len(pair)-1):
#				for j in range(i+1,len(pair)):
#					if pair[i].num==pair[j].num:
#						for c in self.comb:
#							if c.num!=pair[i].num:
#								c.del_num(pair[i].num[0])
#								c.del_num(pair[i].num[1])
#
