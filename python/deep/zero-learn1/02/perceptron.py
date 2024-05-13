# -*- coding: utf-8 -*-

import numpy as np

def gate(x, w, b):
	tmp = sum(x*w) + b
	if tmp<=0:
		return 0
	else:
		return 1

def f_and(x):
	w = np.array([0.5,0.5])
	b = -0.7
	return -(x*w[0]+b)/w[1]
	
def f_nand(x):
	w = np.array([-0.5,-0.5])
	b = 0.7
	return -(x*w[0]+b)/w[1]

def f_or(x):
	w = np.array([0.5,0.5])
	b = -0.2
	return -(x*w[0]+b)/w[1]

def AND(x1, x2):
	""" ANDゲート """
	x = np.array([x1,x2])
	w = np.array([0.5,0.5])
	b = -0.7
	return gate(x, w, b)
		
def NAND(x1, x2):
	""" NANDゲート """
	x = np.array([x1,x2])
	w = np.array([-0.5,-0.5])
	b = 0.7
	return gate(x, w, b)

def OR(x1, x2):
	""" ORゲート """
	x = np.array([x1,x2])
	w = np.array([0.5,0.5])
	b = -0.2
	return gate(x, w, b)
	
def XOR(x1, x2):
	""" XORゲート """
	s1 = NAND(x1, x2)
	s2 = OR(x1, x2)
	return AND(s1, s2)
	
if __name__ == '__main__':
	
	import matplotlib.pyplot as plt
	
	# ANDゲートの可視化
	and_x_false = np.array([0, 1, 0])
	and_y_false = np.array([0, 0, 1])
	and_x_true = np.array([1])
	and_y_true = np.array([1])
	
	fig =plt.figure()
	ax1=fig.add_subplot(1,1,1)
	#ax2=ax1.twinx()
	ax1.scatter(and_x_false, and_y_false, label='False', marker='^', color='r')
	ax1.scatter(and_x_true, and_y_true, label='True', marker='o', color='g')
	
	x = np.linspace(-4.0, 4.0, 100)
	ax1.plot(x, f_and(x))
	
	y2 = -4.0
	ax1.fill_between(x, f_and(x), y2, color='y', alpha=0.5)
	
	ax1.set_xlim(-4.0, 4.0)
	ax1.set_ylim(-4.0, 4.0)
	ax1.set_xticks(np.arange(-3.0, 4.0, 1.0))
	ax1.set_yticks(np.arange(-3.0, 4.0, 1.0))
	#ax1.set_xtickslabels([],fontsize=6)
	ax1.grid()
	
	ax1.set_title('AND')
	ax1.set_xlabel('x1')
	ax1.set_ylabel('x2')
	
	fig.savefig('AND.png')
	plt.close()
	
	# NANDゲートの可視化
	nand_x_false = np.array([1])
	nand_y_false = np.array([1])
	nand_x_true = np.array([0, 1, 0])
	nand_y_true = np.array([0, 0, 1])
	
	fig =plt.figure()
	ax1=fig.add_subplot(1,1,1)
	ax1.scatter(nand_x_false, nand_y_false, label='False', marker='^', color='r')
	ax1.scatter(nand_x_true, nand_y_true, label='True', marker='o', color='g')
	
	x = np.linspace(-4.0, 4.0, 100)
	ax1.plot(x, f_nand(x))
	
	y2 = 4.0
	ax1.fill_between(x, f_nand(x), y2, color='y', alpha=0.5)
	
	ax1.set_xlim(-4.0, 4.0)
	ax1.set_ylim(-4.0, 4.0)
	ax1.set_xticks(np.arange(-3.0, 4.0, 1.0))
	ax1.set_yticks(np.arange(-3.0, 4.0, 1.0))
	ax1.grid()
	
	ax1.set_title('NAND')
	ax1.set_xlabel('x1')
	ax1.set_ylabel('x2')
	
	fig.savefig('NAND.png')
	plt.close()
	
	# ORゲートの可視化
	or_x_false = np.array([0])
	or_y_false = np.array([0])
	or_x_true = np.array([1, 0, 1])
	or_y_true = np.array([0, 1, 1])
	
	fig =plt.figure()
	ax1=fig.add_subplot(1,1,1)
	ax1.scatter(or_x_false, or_y_false, label='False', marker='^', color='r')
	ax1.scatter(or_x_true, or_y_true, label='True', marker='o', color='g')
	
	x = np.linspace(-4.0, 4.0, 100)
	ax1.plot(x, f_or(x))
	
	y2 = -4.0
	ax1.fill_between(x, f_or(x), y2, color='y', alpha=0.5)
	
	ax1.set_xlim(-4.0, 4.0)
	ax1.set_ylim(-4.0, 4.0)
	ax1.set_xticks(np.arange(-3.0, 4.0, 1.0))
	ax1.set_yticks(np.arange(-3.0, 4.0, 1.0))
	ax1.grid()
	
	ax1.set_title('OR')
	ax1.set_xlabel('x1')
	ax1.set_ylabel('x2')
	
	fig.savefig('OR.png')
	plt.close()
	
	# XORゲートの可視化
	xor_x_false = np.array([0, 1])
	xor_y_false = np.array([0, 1])
	xor_x_true = np.array([1, 0])
	xor_y_true = np.array([0, 1])
	
	fig =plt.figure()
	ax1=fig.add_subplot(1,1,1)
	ax1.scatter(xor_x_false, xor_y_false, label='False', marker='^', color='r')
	ax1.scatter(xor_x_true, xor_y_true, label='True', marker='o', color='g')
	
	#x = np.linspace(-4.0, 4.0, 100)
	#ax1.plot(x, f_or(x))
	
	#y2 = -4.0
	#ax1.fill_between(x, f_or(x), y2, color='y', alpha=0.5)
	
	ax1.set_xlim(-4.0, 4.0)
	ax1.set_ylim(-4.0, 4.0)
	ax1.set_xticks(np.arange(-3.0, 4.0, 1.0))
	ax1.set_yticks(np.arange(-3.0, 4.0, 1.0))
	ax1.grid()
	
	ax1.set_title('XOR')
	ax1.set_xlabel('x1')
	ax1.set_ylabel('x2')
	
	fig.savefig('XOR.png')
	plt.close()
	