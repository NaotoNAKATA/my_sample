# -*- coding: utf-8 -*-

import os
import glob
import shutil

from fe_pil import fe_pil
from fe_compose import fe_compose
	
class fe_pil_ivent(fe_pil):
	"""イベントシーン人物画像(img)"""
	def __init__(self, path):
		"""初期化"""
		super().__init__(path, bsize=1)
		
		self.init_local()
		
	def init_local(self):
		""" 各派生クラスの初期化 """
		# オリジナルは256,224
		# 48x64+ mergin
		
		# 人物1,2(会話、イベント)
		pix = [40-1,88-1,40+48,88+64]
		self.person1 = self.get(pix)
		
		pix = [168-1,88-1,168+48,88+64]
		self.person2 = self.get(pix)
		
		# 人物3(戦闘)
		
		
	def save1(self, path):
		""" 人物1の保存 """
		self.person1.save(path)
	
	def save2(self, path):
		""" 人物2の保存 """
		self.person2.save(path)
		
	
		
		

class fe_ivent(fe_compose):
	""" 会話シーンクラス """
	TEMP_DIR='temp'
	def __init__(self):
		"""初期化"""
		super().__init__(fe_pil_ivent)
	
	def save_temp_file(self):
		""" 保存 """
		for i, fe in enumerate(self.fe):
			filename = self.TEMP_DIR + '/{0:0>2}1.png'.format(i)
			fe.person1.save(filename)
			
			filename = self.TEMP_DIR + '/{0:0>2}2.png'.format(i)
			fe.person2.save(filename)
	
	def set(self, persons):
		""" 処理するリスト """
		self.persons = persons
		
	def save_persons(self):
		""" 人物画像の保存 """
		
		for name, no, pos in self.persons:
			if pos=='L':
				self.fe[no].person1.save(TEMP_DIR + '/' + name + '.png'
			
			pass
	
		
	
	def run(self):
		""" 実行 """
		self.del_temp()
		self.read()
		
		#self.save_temp_file()
		
		
		
if __name__ == '__main__':
	
	import fe_param_00.fe_ivent as ivt
	
	fe = fe_ivent()
	#fe.TEMP_DIR = ivt.out_dir
	fe.set(ivt.persons)
	fe.run()
	
	