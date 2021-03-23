# -*- coding: utf-8 -*-

import unittest

from numbers_solver import num_box

class Test_num_box(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def test1(self):
		self.assertEqual('foo'.upper(), 'FOO')
	def test2(self):
		self.assertTrue('foo'.isupper())
		self.assertFalse('foo'.isupper())

if __name__ == '__main__':
	unittest.main()


