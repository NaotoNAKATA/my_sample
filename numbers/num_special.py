# -*- coding: utf-8 -*-

from num_box import num_box
from num_group import num_group

# 特殊クラス
class num_joint(num_group):
	""" (特殊)ジョイント """
	def __init__(self, _num_box_list, _max_num=9):
		""" num_boxクラスの参照を受け取る """
		# 配列長は2で固定
		super().__init__(_num_box_list)
		
		# 最大数字は引数で受け取る
		self.max_num = _max_num
		
	def solve3(self):
		""" 確定数字の隣の候補を削除する """
		for i, nb in enumerate(self.nb_list):
			if nb.is_ok():
				exp_cand = [ nb.num-1, nb.num+1]
				del_cand = [ j for j in range(1,self.max_num+1) if j not in exp_cand ]
				
				if i>0:
					self.nb_list[i-1].del_cand(del_cand)
				
				if i<(self.len-1):
					self.nb_list[i+1].del_cand(del_cand)
					
	def solve4(self):
		""" 候補が連番になっているか """
		for i in range(self.len):
			if not self.nb_list[i].is_ok():
				# 連番の候補を作成
				cand = self.nb_list[i].cand
				cand1 = list( map(lambda x:x-1, cand) )
				cand2 = list( map(lambda x:x+1, cand) )
				
				# 重複削除
				cand3 = list( set(cand1+cand2) )
				
				# 範囲外削除
				cand4 = [ c for c in cand3 if c>0 or c<=self.max_num ]
				
				# 削除リスト作成
				del_cand = [ c for c in range(1,self.max_num+1) if c not in cand4 ]
				
				# 隣の候補を削除
				if i>0:
					self.nb_list[i-1].del_cand(del_cand)
				if i<(self.len-1):
					self.nb_list[i+1].del_cand(del_cand)
	
	def solve5(self):
		# 実装なし
		pass
		
class num_ineq(num_group):
	""" (特殊)不等号 """
	def __init__(self, _num_box_list, _max_num=9):
		""" num_boxクラスの参照を受け取る """
		# 配列長は2で固定
		# 必ず昇順で初期化すること
		super().__init__(_num_box_list)
		
		# 最大数字は引数で受け取る
		self.max_num = _max_num
		
	def solve3(self):
		""" 確定数字の隣の候補を削除する """
		for i, nb in enumerate(self.nb_list):
			if nb.is_ok():
				if i==0:
					f = lambda x:x<=self.nb_list[0].num
				elif i==1:
					f = lambda x:x>=self.nb_list[1].num
						
				del_cand = [ j for j in range(1,self.max_num+1) if f(j) ]
				self.nb_list[1-i].del_cand(del_cand)
				
		# 候補を削除したので更新
		self.solve2()
	
	def solve4(self):
		""" 候補が昇順になっているか """
		for i, nb in enumerate(self.nb_list):
			if not nb.is_ok():
				if i==0:
					if self.nb_list[0].cand==[]:
						f = lambda x:False
					else:
						f = lambda x:x<=min(self.nb_list[0].cand)
				elif i==1:
					if self.nb_list[1].cand==[]:
						f = lambda x:False
					else:
						f = lambda x:x>=max(self.nb_list[1].cand)
						
				del_cand = [ j for j in range(1,self.max_num+1) if f(j) ]
				self.nb_list[1-i].del_cand(del_cand)
		
		# 候補を削除したので更新
		self.solve2()
	
	def solve5(self):
		# 実装なし
		pass
	
class num_sum(num_group):
	""" (特殊)合計 """
	def __init__(self, _num_box_list, _sum):
		""" num_boxクラスの参照を受け取る """
		super().__init__(_num_box_list)
		
		# 合計数字
		self.sums = _sum
		
	def solve1(self):
		pass
	
	def solve3(self):
		# 最後の一つを確定させる
		self.update_det()
		if self.len==len(self.det_num)+1:
			for nb in self.nb_list:
				if not nb.is_ok():
					nb.set( self.sums - sum(self.det_num) )
					break
		
	def solve4(self):
		pass
	
	def solve5(self):
		pass
		
class num_arrow(num_group):
	""" (特殊)合計アロー """
	def __init__(self, _num_box_list):
		""" num_boxクラスの参照を受け取る """
		super().__init__(_num_box_list)
		
		# 暗黙的に最大数字は9
		self.max_num = 9
		
	def solve1(self):
		# 合計に1は入らない
		if not self.nb_list[0].is_ok():
			self.nb_list[0].del_cand([1])
		
		# 足す側に9は入らない
		for nb in self.nb_list[1:]:
			if not nb.is_ok():
				nb.del_cand([self.max_num])
		
	def solve3(self):
		# 最後の一つを確定させる
		self.update_det()
		if self.len==len(self.det_num)+1:
			if not self.nb_list[0].is_ok():
				# 合計が未確定
				self.nb_list[0].set( sum(self.det_num) )
			else:
				# 足す側が未確定
				for nb in self.nb_list[1:]:
					if not nb.is_ok():
						nb.set( 2*self.nb_list[0].num - sum(self.det_num) )
						break
		
	def solve4(self):
		# 確定数字より小さい数字は合計にはならない
		self.update_det()
		if not self.nb_list[0].is_ok() and self.det_num!=[]:
			del_cand = [ c for c in self.nb_list[0].cand if c <=max(self.det_num) ]
			self.nb_list[0].del_cand( del_cand )
			
		# 合計の候補の最大数字以上の数字は、足す側に入らない
		if not self.nb_list[0].is_ok():
			m = max( self.nb_list[0].cand )
			del_cand = [ c for c in range(1,self.max_num) if c>=m ]
			for nb in self.nb_list[1:]:
				nb.del_cand( del_cand )
			
	def solve5(self):
		pass
		
class num_mult(num_group):
	""" (特殊)九九 """
	def __init__(self, _num_box_list):
		""" num_boxクラスの参照を受け取る """
		super().__init__(_num_box_list)
		
		# 暗黙的に最大数字は9
		self.max_num = 9
		
	def solve1(self):
		# 最初の2マスに1は入らない
		for nb in self.nb_list[:2]:
			nb.del_cand([1])
	
	def solve3(self):
		# 最初の2マスが確定したら、残りも確定
		for nb in self.nb_list[:2]:
			if not nb.is_ok():
				break
		else:
			m = self.nb_list[0].num * self.nb_list[1].num
			if self.len==3:
				self.nb_list[2].set(m)
			elif self.len==4:
				self.nb_list[2].set(int(m/10))
				self.nb_list[3].set(m%10)
	
	def solve4(self):
		# 最初の2マスのうちどちらかが確定しているときは候補を絞る
		if self.is_ok():
			return
		
		if self.nb_list[0].is_ok() or self.nb_list[1].is_ok():
			if self.nb_list[0].is_ok():
				ok = self.nb_list[0]
				ng = self.nb_list[1]
			else:
				ok = self.nb_list[1]
				ng = self.nb_list[0]
			
			del_cand = []
			cand2 = []
			cand3 = []
			for c in ng.cand:
				m = c * ok.num
				
				# 左辺の候補を削除
				if self.len==3 and m>9:
					del_cand.append(c)
				elif self.len==4 and m<12:
					del_cand.append(c)
				
				# 右辺の候補を削除
				if self.len==3 and m<=9:
					cand2.append(m)
				elif self.len==4 and m>=12:
					cand2.append(int(m/10))
					cand3.append(m%10)
			
			ng.del_cand( del_cand )
			
			del_cand2 = [ i for i in range(1,10) if i not in cand2 ]
			del_cand3 = [ i for i in range(1,10) if i not in cand3 ]
			
			self.nb_list[2].del_cand( del_cand2 )
			if self.len==4:
				self.nb_list[3].del_cand( del_cand3 )
	
	def solve5(self):
		pass
	