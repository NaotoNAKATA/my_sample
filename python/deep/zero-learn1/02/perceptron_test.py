# -*- coding: utf-8 -*-

import unittest

from perceptron import AND
from perceptron import NAND
from perceptron import OR
from perceptron import XOR

class TestPerceptron(unittest.TestCase):
	def setUp(self):
		pass
		
	def tearDown(self):
		pass
		
	def testAND(self):
		self.assertEqual(0, AND(0,0)) 
		self.assertEqual(0, AND(0,1)) 
		self.assertEqual(0, AND(1,0)) 
		self.assertEqual(1, AND(1,1)) 
		
	def testNAND(self):
		self.assertEqual(1, NAND(0,0)) 
		self.assertEqual(1, NAND(0,1)) 
		self.assertEqual(1, NAND(1,0)) 
		self.assertEqual(0, NAND(1,1)) 
		
	def testOR(self):
		self.assertEqual(0, OR(0,0)) 
		self.assertEqual(1, OR(0,1)) 
		self.assertEqual(1, OR(1,0)) 
		self.assertEqual(1, OR(1,1)) 
		
	def testXOR(self):
		self.assertEqual(0, XOR(0,0)) 
		self.assertEqual(1, XOR(0,1)) 
		self.assertEqual(1, XOR(1,0)) 
		self.assertEqual(0, XOR(1,1)) 
		
if __name__ == '__main__':
	unittest.main(verbosity=2)
	
	
	