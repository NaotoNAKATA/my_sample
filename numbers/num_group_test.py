# -*- coding: utf-8 -*-

import unittest

from num_box import num_box
from num_group import num_group

class TestNumGroup(unittest.TestCase):
	def setUp(self):
		# 初期化時には参照を渡す。以下、参照元を更新する
		self.num_box_list = [ num_box() for i in range(9) ]
		self.num_group = num_group( self.num_box_list )
		
	def tearDown(self):
		pass
		
	def test_init(self):
		# 初期化テスト
		self.assertEqual(self.num_group.len, 9)
		self.assertEqual(self.num_group.det_num, [] )
		self.assertEqual(self.num_group.not_det_num, list(range(1,10)) )
	
	def test_is_ok(self):
		# 初期化後はFalse
		self.assertFalse( self.num_group.is_ok() )
		
		# 一つだけ確定でもFalse
		self.num_box_list[0].set(1)
		self.assertFalse( self.num_group.is_ok() )
		
		# 全て確定でTrue
		for nb, i in zip(self.num_box_list, range(1,10)):
			nb.set(i)
		self.assertTrue( self.num_group.is_ok() )
		
	def test_update_det(self):
		# 一つだけ確定
		self.num_box_list[0].set(1)
		self.num_group.update_det()
		self.assertEqual(self.num_group.det_num, [1] )
		self.assertEqual(self.num_group.not_det_num, list(range(2,10)) )
		
		# 追加で確定させる
		self.num_box_list[1].set(2)
		self.num_box_list[2].set(3)
		self.num_group.update_det()
		self.assertEqual(self.num_group.det_num, [1,2,3] )
		self.assertEqual(self.num_group.not_det_num, list(range(4,10)) )
		
	def test_solve1(self):
		# 一つだけ確定させ、他から正しく候補を削除できるか確認
		self.num_box_list[0].set(1)
		
		# 実行
		self.num_group.solve1()
		
		self.assertEqual(self.num_group.det_num, [1] )
		self.assertEqual(self.num_group.not_det_num, list(range(2,10)) )
		
		self.assertEqual( self.num_group.nb_list[0].num, 1)
		self.assertEqual( self.num_group.nb_list[0].cand, [])
		self.assertTrue( self.num_group.nb_list[0].is_ok())
		for i in range(2,10):
			self.assertEqual( self.num_group.nb_list[i-1].cand, list(range(2,10)) )
			self.assertFalse( self.num_group.nb_list[i-1].is_ok())
	
	def test_solve2(self):
		# 一つだけ、候補を一つにしておく
		cand = [i for i in range(1,10) if i!=5]
		self.num_box_list[0].del_cand( cand )
			
		# 実行
		self.num_group.solve2()
			
		self.assertEqual( self.num_group.nb_list[0].num, 5)
		self.assertEqual( self.num_group.nb_list[0].cand, [])
		self.assertTrue( self.num_group.nb_list[0].is_ok())
			
		for i in range(2,10):
			self.assertEqual( self.num_group.nb_list[i-1].cand, list(range(1,10)) )
			self.assertFalse( self.num_group.nb_list[i-1].is_ok())
			
	def test_solve3(self):
		# 一つ以外の候補から、候補を一つ削除
		for i in range(2,10):
			self.num_group.nb_list[i-1].del_cand([5])
			
		# 実行
		self.num_group.solve3()
			
		self.assertEqual( self.num_group.nb_list[0].num, 5)
		self.assertEqual( self.num_group.nb_list[0].cand, [])
		self.assertTrue( self.num_group.nb_list[0].is_ok())
			
		exp = [i for i in range(1,10) if i!=5]
		for i in range(2,10):
			self.assertEqual( self.num_group.nb_list[i-1].cand, exp)
			self.assertFalse( self.num_group.nb_list[i-1].is_ok())

	def test_solve4(self):
		# ペアをつくる
		self.num_box_list[0].cand = [3, 4]
		self.num_box_list[1].cand = [3, 4]
		
		# 実行
		self.num_group.solve4()
		
		self.assertEqual( self.num_group.nb_list[0].cand, [3, 4])
		self.assertEqual( self.num_group.nb_list[1].cand, [3, 4])
		exp = [1,2,5,6,7,8,9]
		for i in range(3,10):
			self.assertEqual( self.num_group.nb_list[i-1].cand, exp)
			self.assertFalse( self.num_group.nb_list[i-1].is_ok())

	def test_solve5(self):
		# ペアをつくる
		self.num_box_list[0].cand = [3, 4]
		self.num_box_list[1].cand = [4, 6]
		self.num_box_list[2].cand = [3, 6]
		
		# 実行
		self.num_group.solve5()
		
		self.assertEqual( self.num_group.nb_list[0].cand, [3, 4])
		self.assertEqual( self.num_group.nb_list[1].cand, [4, 6])
		self.assertEqual( self.num_group.nb_list[2].cand, [3, 6])
		exp = [1,2,5,7,8,9]
		for i in range(4,10):
			self.assertEqual( self.num_group.nb_list[i-1].cand, exp)
			self.assertFalse( self.num_group.nb_list[i-1].is_ok())
		
if __name__ == '__main__':
	unittest.main(verbosity=2)
