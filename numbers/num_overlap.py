# -*- coding: utf-8 -*-

from num_box import num_box
from num_group import num_group

class num_overlap:
	""" グループの重なり """
	def __init__(self, _group_a, _group_b):
		""" 初期化  """
		self.overlap = []
		self.group_a = []
		self.group_b = []
		
		# 重なりが2以上のみ有効
		id_a = [ id(nb)  for nb in _group_a.nb_list ]
		id_b = [ id(nb)  for nb in _group_b.nb_list ]
		
		len_a_b = len(id_a) + len(id_b)
		len_ab = len( set( id_a + id_b ) )
		if (len_a_b-len_ab)<2:
			# 重なりが1以下なので無視
			self.ol = False
		elif id(_group_a)==id(_group_b):
			# 同じグループは無視
			self.ol = False
		else:
			self.ol = True
			
			# グループ分け
			id_overlap = []
			for a in id_a:
				for b in id_b:
					if a==b:
						id_overlap.append(a)
			
			for nb in _group_a.nb_list:
				if id(nb) in id_overlap:
					self.overlap.append(nb)
				else:
					self.group_a.append(nb)
			
			for nb in _group_b.nb_list:
				if id(nb) not in id_overlap:
					self.group_b.append(nb)
						
	def is_overlap(self):
		return self.ol
	
	def is_ok(self):
		o = all( map(lambda x:x.is_ok(), self.overlap) )
		a = all( map(lambda x:x.is_ok(), self.group_a) )
		b = all( map(lambda x:x.is_ok(), self.group_b) )
		return all([o, a, b])
	
	def solve1(self):
		# 重なりが2つ以上あって、AかつBに候補nが2つ以上あり、
		#Aー(AかつB)に候補nがないとき、
		#B−(AかつB)から候補nを削除できる
		
		def filter_cand(x):
			cand = []
			for nb in x:	
				cand += nb.cand
			return list(set(cand))
			
		cand_a = filter_cand(self.group_a)
		cand_b = filter_cand(self.group_b)
		cand_o = filter_cand(self.overlap)
		
		def filter_det(x):
			det = []
			for nb in x:
				if nb.num!=-1:
					det.append(nb.num)
			return list(set(det))
		
		det_a = filter_det(self.group_a)
		det_b = filter_det(self.group_b)
		det_o = filter_det(self.overlap)
		
		del_cand_a = []
		del_cand_b = []
		for c in cand_o:
			n = 0
			for nb in self.overlap:
				if c in nb.cand:
					n += 1
			
			if n >=2:
				if c not in cand_a and c not in det_a:
					del_cand_b.append(c)
				if c not in cand_b and c not in det_b:
					del_cand_a.append(c)
		
		for nb in self.group_a:
			nb.del_cand( del_cand_a )
		for nb in self.group_b:
			nb.del_cand( del_cand_b )
	
	def solve(self):
		self.solve1()
	