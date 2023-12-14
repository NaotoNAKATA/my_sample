# -*- coding: utf-8 -*-

import unittest

from num_box import num_box
from num_special import num_joint

class TestNumJoint(unittest.TestCase):
	def setUp(self):
		self.num_box_list = [ num_box() for i in range(2) ]
		self.num_joint = num_joint( self.num_box_list )
		
	def tearDown(self):
		pass
		
	def test_init(self):
		# 初期化テスト
		self.assertEqual(self.num_joint.len, 2)
		self.assertEqual(self.num_joint.max_num, 9)
		self.assertEqual(self.num_joint.det_num, [] )
		self.assertFalse(self.num_joint.is_ok())
	
	def test_solve3(self):
		#
		for i in range(2):
			for j in range(9):
				# 毎ループ初期化
				self.num_box_list = [ num_box() for i in range(2) ]
				self.num_joint = num_joint( self.num_box_list )

				# 片方を確定
				self.num_box_list[i].set( j+1 )
				
				# 実行前
				self.assertEqual(self.num_box_list[1-i].cand, [1,2,3,4,5,6,7,8,9] )
				
				# 実行
				self.num_joint.solve3()
				
				# 実行後
				exp = [ k for k in range(1,10) if k==(j+1-1) or k==(j+1+1) ]
				self.assertEqual(self.num_box_list[1-i].cand,  exp)
				self.assertEqual(self.num_box_list[i].cand,  [])
	
	def test_solve4(self):
		self.num_box_list[0].del_cand([1,2,3,5,6,9])
		
		# 実行
		self.num_joint.solve4()
		
		# 実行後
		self.assertEqual(self.num_box_list[0].cand,  [4,7,8])
		self.assertEqual(self.num_box_list[1].cand,  [3,5,6,7,8,9])
	
	def test_solve4_1(self):
		# 実行
		self.num_joint.solve4()
		
		# 実行後
		self.assertEqual(self.num_box_list[0].cand,  [1,2,3,4,5,6,7,8,9])
		self.assertEqual(self.num_box_list[1].cand,  [1,2,3,4,5,6,7,8,9])
			
		
		
	
if __name__ == '__main__':
	unittest.main(verbosity=2)
