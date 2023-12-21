# -*- coding: utf-8 -*-

import os

from num_box import num_box
from num_group import num_group
from num_special import num_joint
from num_special import num_ineq
from num_overlap import num_overlap

class num_solver:
	""" 数独問題クラス """
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
		for group_list in te['group']:
			self.make_group(group_list)
			
		# グループ間の重なり
		self.make_overlap()
		
		# (特殊)ジョイント
		for joint_list in te['joint']:
			self.make_joint(joint_list, te['length'])
		
		# (特殊)不等号
		for ineq_list in te['inequal']:
			self.make_ineq(ineq_list, te['length'])
			
		# (特殊)偶数
		for evn_list in te['even']:
			self.del_odd( evn_list )
	
	def set(self, _idx, _num=-1):
		""" 数字クラスの登録 """
		self.nb[_idx] = num_box(
				_len=self.len, _num=_num)
	
	def make_group(self, group_list):
		""" グループの作成 """
		num_box_list = []
		for idx in group_list:
			num_box_list.append( self.nb[idx] )
			
		self.grp.append( num_group(num_box_list) )
	
	def make_overlap(self):
		""" 重なりをチェック """
		l = len(self.grp)
		for i in range( l-1 ):
			for j in range(i, l):
				no = num_overlap( self.grp[i], self.grp[j] )
				if no.is_overlap():
					self.grp.append( no )
		
	def make_joint(self, joint_list, _len):
		""" (特殊)ジョイントクロス """
		num_box_list = []
		for idx in joint_list:
			num_box_list.append( self.nb[idx])
			
		self.grp.append( num_joint(num_box_list, _len) )
	
	def make_ineq(self, ineq_list, _len):
		""" (特殊)不等号 """
		num_box_list = []
		for idx in ineq_list:
			num_box_list.append( self.nb[idx])
			
		self.grp.append( num_ineq(num_box_list, _len) )
	
	def del_odd(self, evn_list):
		""" 奇数を削除 """
		for idx in evn_list:
			self.nb[idx] .del_cand_odd()
	
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
				break
		else:
			print('not solve')
