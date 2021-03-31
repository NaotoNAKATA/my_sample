# -*- coding: utf-8 -*-

import unittest

from numbers_solver import num_box
from numbers_solver import num_set

class Test_num_box(unittest.TestCase):
	def setUp(self):
		self.nb = num_box()
		
	def tearDown(self):
		pass
		
	def test_init(self):
		""" 初期化テスト """
		self.assertEqual(self.nb.num, -1)
		self.assertEqual(self.nb.cand, list(range(1,10)) )
		self.assertEqual(self.nb.cand_len(), 9)
		self.assertFalse(self.nb.init)
		self.assertFalse(self.nb.is_ok())
		
		# 確定初期化
		for i in range(1,10):
			nb = num_box(_num=i)
			self.assertEqual(nb.num, i)
			self.assertEqual(nb.cand, [] )
			self.assertEqual(nb.cand_len(), 0)
			self.assertTrue(nb.init)
			self.assertTrue(nb.is_ok())
			
	def test_is_ok(self):
		# 未確定なのでFalse
		self.assertFalse(self.nb.is_ok())
		
	def test_set(self):
		# 値をセットして確認
		self.nb.set(1)
		self.assertTrue(self.nb.is_ok())
		self.assertEqual(self.nb.num, 1)
		self.assertEqual(self.nb.cand, [] )
		
	def test_del_cand(self):
		# 候補を削除
		cand = [3,6]
		self.nb.del_cand(cand)
		exp = [i for i in range(1,10) if i not in cand]
		self.assertEqual(self.nb.cand, exp )
		self.assertFalse(self.nb.is_ok())
		self.assertEqual(self.nb.cand_len(), 7)
		
		# 追加で削除
		cand2 = [2,6]
		self.nb.del_cand(cand2)
		exp2 = [i for i in range(1,10) if i not in cand2 and i not in cand]
		self.assertEqual(self.nb.cand, exp2 )
		self.assertFalse(self.nb.is_ok())
		self.assertEqual(self.nb.cand_len(), 6)
	
	def test_solve(self):
		# 一つを残して候補を削除させておく
		cand = [i for i in range(1,10) if i!=5]
		self.nb.del_cand(cand)
		self.assertEqual(self.nb.num, -1)
		self.assertEqual(self.nb.cand, [5])
		self.assertFalse(self.nb.is_ok())
		self.assertEqual(self.nb.cand_len(), 1)
		
		# 実行
		self.nb.solve()
		self.assertEqual(self.nb.num, 5)
		self.assertEqual(self.nb.cand, [])
		self.assertTrue(self.nb.is_ok())
		self.assertEqual(self.nb.cand_len(), 0)
		
class Test_num_set1(unittest.TestCase):
	def setUp(self):
		self.num_box_list = [ num_box() for i in range(9) ]
		self.num_set = num_set( self.num_box_list )
		
	def tearDown(self):
		pass
		
	def test_init(self):
		# 初期化テスト
		self.assertEqual(self.num_set.len, 9)
		self.assertEqual(self.num_set.det_num, [] )
		self.assertEqual(self.num_set.not_det_num, list(range(1,10)) )
		
	def test_is_ok(self):
		# 初期化後はFalse
		self.assertFalse( self.num_set.is_ok() )
		
		# 一つだけ確定でもFalse
		self.num_box_list[0].set(1)
		self.assertFalse( self.num_set.is_ok() )
		
		# 全て確定でTrue
		for nb, i in zip(self.num_box_list, range(1,10)):
			nb.set(i)
		self.assertTrue( self.num_set.is_ok() )
		
	def test_update_det(self):
		# 一つだけ確定
		self.num_box_list[0].set(1)
		self.num_set.update_det()
		self.assertEqual(self.num_set.det_num, [1] )
		self.assertEqual(self.num_set.not_det_num, list(range(2,10)) )
		
		# 追加で確定させる
		self.num_box_list[1].set(2)
		self.num_box_list[2].set(3)
		self.num_set.update_det()
		self.assertEqual(self.num_set.det_num, [1,2,3] )
		self.assertEqual(self.num_set.not_det_num, list(range(4,10)) )
		
	def test_solve1(self):
		# 一つだけ確定させ、他から正しく候補を削除できるか確認
		self.num_box_list[0].set(1)
		
		self.num_set.solve1()
		
		self.assertEqual(self.num_set.det_num, [1] )
		self.assertEqual(self.num_set.not_det_num, list(range(2,10)) )
		
		self.assertEqual( self.num_set.num_box[0].num, 1)
		self.assertEqual( self.num_set.num_box[0].cand, [])
		self.assertTrue( self.num_set.num_box[0].is_ok())
		for i in range(2,10):
			self.assertEqual( self.num_set.num_box[i-1].cand, list(range(2,10)) )
			self.assertFalse( self.num_set.num_box[i-1].is_ok())
		
	def test_solve2(self):
		# 一つだけ、候補を一つにしておく
		cand = [i for i in range(1,10) if i!=5]
		self.num_box_list[0].del_cand( cand )
			
		# 実行
		self.num_set.solve2()
			
		self.assertEqual( self.num_set.num_box[0].num, 5)
		self.assertEqual( self.num_set.num_box[0].cand, [])
		self.assertTrue( self.num_set.num_box[0].is_ok())
			
		for i in range(2,10):
			self.assertEqual( self.num_set.num_box[i-1].cand, list(range(1,10)) )
			self.assertFalse( self.num_set.num_box[i-1].is_ok())
			
	def test_solve3(self):
		# 一つ以外の候補から、候補を一つ削除
		for i in range(2,10):
			self.num_set.num_box[i-1].del_cand([5])
			
		# 実行
		self.num_set.solve3()
			
		self.assertEqual( self.num_set.num_box[0].num, 5)
		self.assertEqual( self.num_set.num_box[0].cand, [])
		self.assertTrue( self.num_set.num_box[0].is_ok())
			
		exp = [i for i in range(1,10) if i!=5]
		for i in range(2,10):
			self.assertEqual( self.num_set.num_box[i-1].cand, exp)
			self.assertFalse( self.num_set.num_box[i-1].is_ok())

	def test_solve4(self):
		# ペアをつくる
		self.num_box_list[0].cand = [3, 4]
		self.num_box_list[1].cand = [3, 4]
		
		# 実行
		self.num_set.solve4()
		
		self.assertEqual( self.num_set.num_box[0].cand, [3, 4])
		self.assertEqual( self.num_set.num_box[1].cand, [3, 4])
		exp = [1,2,5,6,7,8,9]
		for i in range(3,10):
			self.assertEqual( self.num_set.num_box[i-1].cand, exp)
			self.assertFalse( self.num_set.num_box[i-1].is_ok())

	def test_solve5(self):
		# ペアをつくる
		self.num_box_list[0].cand = [3, 4]
		self.num_box_list[1].cand = [4, 6]
		self.num_box_list[2].cand = [3, 6]
		
		# 実行
		self.num_set.solve5()
		
		self.assertEqual( self.num_set.num_box[0].cand, [3, 4])
		self.assertEqual( self.num_set.num_box[1].cand, [4, 6])
		self.assertEqual( self.num_set.num_box[2].cand, [3, 6])
		exp = [1,2,5,7,8,9]
		for i in range(4,10):
			self.assertEqual( self.num_set.num_box[i-1].cand, exp)
			self.assertFalse( self.num_set.num_box[i-1].is_ok())

		
		
if __name__ == '__main__':
	unittest.main()


