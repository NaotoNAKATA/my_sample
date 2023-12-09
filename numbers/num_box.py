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
