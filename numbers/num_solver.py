# -*- coding: utf-8 -*-

import os
import openpyxl
from openpyxl.styles import Font
from openpyxl.styles import PatternFill

from num_box import num_box
from num_group import num_group
from num_template import num_template
from num_special import num_joint
from num_special import num_ineq

class num_solver:
	""" 数独問題クラス """
	def __init__(self, _len=9):
		""" 初期化 """
		# 全数字(num_box)
		self.nb = {}
		
		# 全グループ(num_group)
		self.grp = []
		
		# (特殊)ジョイントクロス (num_joint)
		self.jnt = []
		
		# (特殊)不等号 (num_ineq)
		self.fto = []
		
		# 最大数字
		self.len = _len
		
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
	
	def make_joint(self, joint_list, _len):
		""" (特殊)ジョイントクロス """
		num_box_list = []
		for idx in joint_list:
			num_box_list.append( self.nb[idx])
			
		self.jnt.append( num_joint(num_box_list, _len) )
	
	def make_ineq(self, ineq_list, _len):
		""" (特殊)不等号 """
		num_box_list = []
		for idx in ineq_list:
			num_box_list.append( self.nb[idx])
			
		self.fto.append( num_ineq(num_box_list, _len) )
	
	def del_odd(self, evn_list):
		""" 奇数を削除 """
		for idx in evn_list:
			self.nb[_idx] .del_cand_odd()
	
	def is_ok(self):
		""" クラス内の数字がすべて確定していれば True """
		return all( map(lambda x:x.is_ok(), self.nb.values()) )

	def solve(self):
		""" 解く """
		for i in range(30):
			# 各グループのsolverを起動
			for g in self.grp:
				g.solve()
				
			for j in self.jnt:
				j.solve()
				
			for f in self.fto:
				f.solve()
			
			# すべて確定でbreak
			if self.is_ok():
				print('solve...{}'.format(i))
				break
		else:
			print('not solve')
