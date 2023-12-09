# -*- coding: utf-8 -*-

import unittest

from num_box import num_box

class TestNumBox(unittest.TestCase):
	""" 未確定初期化時のテスト """
	def setUp(self):
		self.nb = num_box()
		
	def tearDown(self):
		pass
		
	def test_init(self):
		# 未確定で初期化
		self.assertEqual(self.nb.num, -1)
		self.assertEqual(self.nb.cand, list(range(1,10)) )
		self.assertEqual(self.nb.cand_len(), 9)
		self.assertFalse(self.nb.init)
		self.assertFalse(self.nb.is_ok())
		
	def test_is_ok(self):
		# 未確定なのでFalse
		self.assertFalse(self.nb.is_ok())
		
	def test_set(self):
		# 値を確定
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
		
	def test_cand_len(self):
		# 候補の数
		self.assertEqual(self.nb.cand_len(), 9)
	
	def test_solve(self):
		# 一つを残して候補を削除させておく
		cand = [i for i in range(1,10) if i!=5]
		self.nb.del_cand(cand)
		
		# 実行
		self.nb.solve()
		self.assertEqual(self.nb.num, 5)
		self.assertEqual(self.nb.cand, [])
		self.assertTrue(self.nb.is_ok())
		self.assertEqual(self.nb.cand_len(), 0)

class TestNumBoxDet(unittest.TestCase):
	""" 確定初期化時のテスト """
	def setUp(self):
		self.nb = [ num_box(_num=i) for i in range(1,10) ]
	
	def tearDown(self):
		pass
	
	def test_init(self):
		for i, nb in enumerate(self.nb):
			# 確定で初期化
			self.assertEqual(nb.num, i+1)
			self.assertEqual(nb.cand, [] )
			self.assertEqual(nb.cand_len(), 0)
			self.assertTrue(nb.init)
			self.assertTrue(nb.is_ok())

if __name__ == '__main__':
	unittest.main(verbosity=2)
