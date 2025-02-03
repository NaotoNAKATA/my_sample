# -*- coding: utf-8 -*-

import os

from num_box import num_box
from num_group import num_group
from num_special import num_joint
from num_special import num_njoint
from num_special import num_ineq
from num_special import num_sum
from num_special import num_arrow
from num_special import num_mult
from num_overlap import num_overlap

class num_solver:
	""" 数独問題クラス """
	version = '1.2.4'
	def __init__(self, te):
		""" 初期化 """
		# 全数字(num_box)
		self.nb = {}
		
		# 全グループ(num_group)
		self.grp = []
		
		# 最大数字
		self.len = te['length']
		
	def configure(self, te):
		""" ソルバー作成 """
		# グループを作成
		self.make_group(te['group'], num_group)
		
		# グループ間の重なり
		self.make_overlap()
		
		# 特殊グループ
		special = [
			['joint', num_joint, self.len], # (特殊)ジョイント
			['njoint', num_njoint, self.len], # (特殊)ジョイントの反転
			['inequal', num_ineq, self.len], # (特殊)不等号
			['arrow', num_arrow, None], # (特殊)合計アロー
			['mult', num_mult, None], # (特殊)九九
		]
		for [key, ng, arg] in special:
			self.make_group(te[key], ng, arg)
			
		# (特殊)足し算
		self.make_sums(te['sums'])
			
		# (特殊)偶数
		self.del_odd(te['even'])
		
	def set(self, _idx, _num=-1):
		""" 数字クラスの登録 """
		self.nb[_idx] = num_box(
				_len=self.len, _num=_num)
	
	def make_group(self, group_list, ng, arg=None):
		""" グループの作成 """
		for group in group_list:
			num_box_list = []
			for idx in group:
				num_box_list.append( self.nb[idx] )
			
			if arg==None:
				self.grp.append( ng(num_box_list) )
			else:
				self.grp.append( ng(num_box_list, arg) )
				
	def make_overlap(self):
		""" 重なりをチェック """
		l = len(self.grp)
		for i in range( l-1 ):
			for j in range(i, l):
				no = num_overlap( self.grp[i], self.grp[j] )
				if no.is_overlap():
					self.grp.append( no )
	
	def make_sums(self, sums_list):
		""" (特殊)足し算 """
		for s, sums in sums_list:
			num_box_list = []
			for idx in sums:
				num_box_list.append( self.nb[idx])
		
			self.grp.append( num_sum(num_box_list, s) )
	
	def del_odd(self, evn_list):
		""" 奇数を削除 """
		for evn in evn_list:
			for idx in evn:
				self.nb[idx].del_cand_odd()
		
	def is_ok(self):
		""" クラス内の数字がすべて確定していれば True """
		return all( map(lambda x:x.is_ok(), self.nb.values()) )

	def solve(self):
		""" 解く """
		for i in range(30):
			# 各グループのsolverを起動
			for g in self.grp:
				g.solve()
			
			# すべて確定でbreak
			if self.is_ok():
				print('solve...{}'.format(i))
				self.result = '{}'.format(i)
				break
		else:
			print('not solve')
			self.result = 'N'
