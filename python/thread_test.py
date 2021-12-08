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

from twisted.internet import reactor
from twisted.internet.task import LoopingCall

class MyLoop(LoopingCall):
	def __init__(self):
		super().__init__(f=self.main, a=('MyLoop',) )
	
	def start(self):
		interval = 1
		super().start(interval, now=False)
		reactor.run()
		
	def main(self, a):
		print(a[0])

if __name__ == '__main__':
	my_th = MyThread()
	my_th.start()
	
	def f():
		while True:
			print('Theading test2')
			time.sleep(2)
	
	th = Thread(target=f)
	th.start()
	#th.join()
	
	my_lp = MyLoop()
	my_lp.start()
