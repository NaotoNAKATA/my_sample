# -*- coding: utf-8 -*-

from threading import Thread
import time

class MyThread(Thread):
	def __init__(self):
		super().__init__(target=self.main)
		
	def main(self):
		while True:
			print('Theading test1')
			time.sleep(1)

if __name__ == '__main__':
	my_th = MyThread()
	my_th.start()
	
	def f():
		while True:
			print('Theading test2')
			time.sleep(2)
	
	th = Thread(target=f)
	th.start()
	th.join()
