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

class num_njoint(num_joint):
	""" (特殊)ジョイントの反転 """
	def __init__(self, _num_box_list, _max_num=9):
		""" num_boxクラスの参照を受け取る """
		super().__init__(_num_box_list, _max_num)
	
	def solve3(self):
		""" 確定数字の隣の候補を削除する """
		for i, nb in enumerate(self.nb_list):
			if nb.is_ok():
				del_cand = [ nb.num-1, nb.num+1]
				
				if i>0:
					self.nb_list[i-1].del_cand(del_cand)
				
				if i<(self.len-1):
					self.nb_list[i+1].del_cand(del_cand)
	
	def solve4(self):
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
					
		# 残り2項の時は候補を絞る
		elif self.len==len(self.det_num)+2:
			sums = self.sums - sum(self.det_num)
			nb_not_det = list( filter( lambda x:x.is_ok()==False, self.nb_list) )
			
			for i in range(2):
				del_cand = []
				for c in nb_not_det[i].cand:
					s = sums - c
					if not s in nb_not_det[1-i].cand:
						del_cand.append(c)
					
					nb_not_det[i].del_cand( del_cand )
		
	def solve4(self):
		# 合計数字以上の候補は削除する
		self.update_det()
		for nb in self.nb_list:
			if not nb.is_ok():
				del_cand = [ i for i in nb.cand if i>=self.sums ]
				nb.del_cand(del_cand)
	
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
	# 右辺 key:十の位、value:一の位の候補
	cand_r1 = {
					1 : [2,4,6,8],
					2 : [1,4,7,8],
					3 : [2,6],
					4 : [2],
					5 : [4,6],
					6 : [3],
					7 : [2],
					8 : [],
					9 : [],
				}
	# 左辺 key:右辺十の位、value:左辺の候補
	cand_l1 = {
					1 : [2,3,4,6,7,8,9],
					2 : [3,4,7,8,9],
					3 : [4,8,9],
					4 : [6,7],
					5 : [6,7,8,9],
					6 : [7,9],
					7 : [8,9],
					8 : [],
					9 : [],
				}
	# 右辺 key:一の位、value:十の位の候補
	cand_r0 = {
					1 : [2],
					2 : [1,3,4,7],
					3 : [6],
					4 : [1,2,5],
					5 : [],
					6 : [1,3,5],
					7 : [2],
					8 : [1,2],
					9 : [],
				}
	# 左辺 key:右辺一の位、value:左辺の候補
	cand_l0 = {
					1 : [3,7],
					2 : [3,4,6,7,8,9],
					3 : [7,9],
					4 : [2,3,6,7,8,9],
					5 : [],
					6 : [2,4,7,8,9],
					7 : [3,9],
					8 : [2,3,4,6,7,9],
					9 : [],
				}
				
	def __init__(self, _num_box_list):
		""" num_boxクラスの参照を受け取る """
		super().__init__(_num_box_list)
		
		# 暗黙的に最大数字は9
		self.max_num = 9
		
		# 以下は、同じグループである前提
		# 左辺に1,5は入らない
		for nb in self.nb_list[:2]:
			nb.del_cand([1,5])
		
		# 長さ3(積が一桁)は、2通りのみ
		# 2x3=6, 2x4=8,
		if self.len==3:
			del_cand1 = [1,          5,6,7,8,9]
			del_cand2 = [1,2,3,4,5,   7,    9]
			
			self.nb_list[0].del_cand( del_cand1 )
			self.nb_list[1].del_cand( del_cand1 )
			self.nb_list[2].del_cand( del_cand2 )
		
		# 長さ4(積が二桁)は、十の位に8,9はない(8x9=72)、一の位に5はない
		if self.len==4:
			self.nb_list[2].del_cand( [8,9] )
			self.nb_list[3].del_cand( [5] )
		
	def solve1(self):
		if self.is_ok():
			return
			
		# 左辺が確定したら、右辺も確定
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
	
	def solve3(self):
		if self.is_ok():
			return
		
		# 長さ3(積が一桁)で右辺が確定しているとき
		if self.len==3 and self.nb_list[2].is_ok():
			# 2x3=6, 2x4=8の2通りのみ
			if self.nb_list[2].num == 6:
				del_cand = [4]
			else:
				del_cand = [3]
			
			for nb in self.nb_list[:2]:
					nb.del_cand( del_cand )
		
		# 長さ4(積が二桁)のとき、右辺から左辺を推定する
		if self.len==4:
			if self.nb_list[2].is_ok() and self.nb_list[3].is_ok():
				# 右辺が確定しているとき
				m = self.nb_list[2].num*10 +  self.nb_list[3].num
				
				if self.nb_list[0].is_ok():
					del_cand = []
					for c in self.nb_list[1].cand:
						n = c * self.nb_list[0].num
						if n != m:
							del_cand.append( c )
					self.nb_list[1].del_cand( del_cand )
				elif self.nb_list[1].is_ok():
					del_cand = []
					for c in self.nb_list[0].cand:
						n = c * self.nb_list[1].num
						if n != m:
							del_cand.append( c )
					self.nb_list[0].del_cand( del_cand )
				else:
					del_cand1 = []
					for c0 in self.nb_list[0].cand:
						for c1 in self.nb_list[1].cand:
							n = c0 * c1
							if n == m:
								break
						else:
							del_cand1.append( c0 )
					
					del_cand2 = []
					for c1 in self.nb_list[1].cand:
						for c0 in self.nb_list[0].cand:
							n = c0 * c1
							if n == m:
								break
						else:
							del_cand2.append( c1 )
							
					self.nb_list[0].del_cand( del_cand1 )
					self.nb_list[1].del_cand( del_cand2 )
				
			elif self.nb_list[2].is_ok():
				# 十の位が確定しているとき
				c = self.nb_list[2].num
				
				del_cand = [ i for i in range(1,10) if i not in self.cand_r1[c] ]
				self.nb_list[3].del_cand( del_cand )
				
				del_cand = [ i for i in range(1,10) if i not in self.cand_l1[c] ]
				for nb in self.nb_list[:2]:
					nb.del_cand( del_cand )
			elif self.nb_list[3].is_ok():
				# 一の位が確定しているとき
				c = self.nb_list[3].num
				
				del_cand = [ i for i in range(1,10) if i not in self.cand_r0[c] ]
				self.nb_list[2].del_cand( del_cand )
				
				del_cand = [ i for i in range(1,10) if i not in self.cand_l0[c] ]
				for nb in self.nb_list[:2]:
					nb.del_cand( del_cand )
	def solve4(self):
		if self.is_ok():
			return
		
		# 左辺2項のうちどちらかが確定しているときは、候補を絞る
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
				
		# 左辺2項のうちどちらかが確定して、右辺も確定しているときは、残りの左辺1項は確定する
		if self.nb_list[0].is_ok() or self.nb_list[1].is_ok():
			for nb in self.nb_list[2:]:
				if not nb.is_ok():
					break
			else:
				if self.len==3:
					m = self.nb_list[2].num
				else:
					m = self.nb_list[2].num * 10 + self.nb_list[3].num
			
				if self.nb_list[0].is_ok():
					self.nb_list[1].set( int(m / self.nb_list[0].num) )
				else:
					self.nb_list[0].set( int(m / self.nb_list[1].num) )
			
	def solve5(self):
		pass
	