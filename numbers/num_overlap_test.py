# -*- coding: utf-8 -*-

import unittest

from num_box import num_box
from num_group import num_group
from num_overlap import num_overlap

class TestNumOverlap(unittest.TestCase):
	""" テスト """
	def setUp(self):
		self.num_box_list_a = [ num_box() for i in range(6) ]
		self.num_box_list_b = [ num_box() for i in range(6) ]
		self.num_box_list_ab = [ num_box() for i in range(3) ]
		
		self.num_group_a = num_group( self.num_box_list_a + self.num_box_list_ab )
		self.num_group_b = num_group( self.num_box_list_b + self.num_box_list_ab )
		
		self.num_overlap =num_overlap(self.num_group_a, self.num_group_b)
		
	def tearDown(self):
		pass
		
	def test_init(self):
		# 初期化のテスト
		self.assertTrue(self.num_overlap.is_overlap())
		
		exp_id_a = sorted( [ id(nb) for nb in self.num_box_list_a ] )
		exp_id_b = sorted( [ id(nb) for nb in self.num_box_list_b ] )
		exp_id_ab = sorted( [ id(nb) for nb in self.num_box_list_ab ] )
		
		res_id_a = sorted( [ id(nb) for nb in self.num_overlap.group_a ] )
		res_id_b = sorted( [ id(nb) for nb in self.num_overlap.group_b ] )
		res_id_ab = sorted( [ id(nb) for nb in self.num_overlap.overlap ] )
		
		self.assertEqual(res_id_a, exp_id_a)
		self.assertEqual(res_id_b, exp_id_b)
		self.assertEqual(res_id_ab, exp_id_ab)
		
	def test_solve1(self):
		# Aから候補を一つ消す
		for nb in self.num_box_list_b:
			nb.del_cand([3])
			
		# ソルバー起動
		for i in range(30):
			self.num_group_a.solve()
			self.num_group_b.solve()
			self.num_overlap.solve()
		
		for nb in self.num_box_list_a:
			self.assertEqual(nb.cand, [1,2,4,5,6,7,8,9])
		
		for nb in self.num_box_list_b:
			self.assertEqual(nb.cand, [1,2,4,5,6,7,8,9])
		
		for nb in self.num_box_list_ab:
			self.assertEqual(nb.cand, [1,2,3,4,5,6,7,8,9])
	
	def test_solve1_1(self):
		self.num_box_list_a[0].set(1)
		self.num_box_list_a[1].set(2)
		self.num_box_list_a[2].set(3)
		self.num_box_list_a[3].set(4)
		self.num_box_list_a[4].set(5)
		#self.num_box_list_a[5].set(6)
		
		# ソルバー起動
		for i in range(30):
			self.num_group_a.solve()
			self.num_group_b.solve()
			self.num_overlap.solve()
		
		self.assertEqual(self.num_box_list_a[5].cand, [6,7,8,9])
		
		for nb in self.num_box_list_b:
			self.assertEqual(nb.cand, [1,2,3,4,5,6,7,8,9])
		
		for nb in self.num_box_list_ab:
			self.assertEqual(nb.cand, [6,7,8,9])
	
	def test_solve1_2(self):
		self.num_box_list_a[0].set(1)
		self.num_box_list_a[1].set(2)
		self.num_box_list_a[2].set(3)
		self.num_box_list_a[3].set(4)
		self.num_box_list_a[4].set(5)
		self.num_box_list_a[5].set(6)
		
		# ソルバー起動
		for i in range(30):
			self.num_group_a.solve()
			self.num_group_b.solve()
			self.num_overlap.solve()
		
		self.assertEqual(self.num_box_list_a[5].cand, [])
		
		for nb in self.num_box_list_b:
			self.assertEqual(nb.cand, [1,2,3,4,5,6])
		
		for nb in self.num_box_list_ab:
			self.assertEqual(nb.cand, [7,8,9])
	
		
if __name__ == '__main__':
	unittest.main(verbosity=2)
