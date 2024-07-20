# -*- coding: utf-8 -*-

import os
import glob
import shutil

from fe_pil import fe_pil
from fe_compose import fe_compose
	
class fe_pil_talk(fe_pil):
	"""会話シーン画像(img)"""
	def __init__(self, path):
		"""初期化"""
		super().__init__(path, bsize=1)
		
		self.init_local()
		
	def init_local(self):
		""" 各派生クラスの初期化 """
		# オリジナルは256,224
		# 48x64+ mergin
		
		# 人物1,2
		pix = [40-1,88-1,40+48,88+64]
		self.person1 = self.get(pix)
		
		pix = [168-1,88-1,168+48,88+64]
		self.person2 = self.get(pix)
		
	
		
		

class fe_talk(fe_compose):
	""" 会話シーンクラス( 結合) """
	TEMP_DIR='temp2'
	def __init__(self):
		"""初期化"""
		super().__init__(fe_pil_talk)
	
	def save_temp_file(self):
		""" 保存 """
		for i, fe in enumerate(self.fe):
			filename = self.TEMP_DIR + '/{0:0>2}1.png'.format(i)
			fe.person1.save(filename)
			
			filename = self.TEMP_DIR + '/{0:0>2}2.png'.format(i)
			fe.person2.save(filename)
	
	
	
	def run(self):
		""" 実行 """
		self.del_temp()
		self.read()
		self.save_temp_file()
		
		
		
if __name__ == '__main__':
	
	
	import talk00_1 as p
	
	fe = fe_talk()
	
	if 'dirs' in dir(p):
		for d in p.dirs:
			fe.add_dir(d)
	if 'files' in dir(p):
		fe.add_files(p.files)
	if 'out_file' in dir(p):
		fe.set_out_file(p.out_file)
	if 'comp' in dir(p):
		fe.set_compose(p.comp)
	
	if p.TEST_RUN_FIRST:
		fe.test_run_first()
	if p.TEST_RUN:
		fe.test_run()
	if p.RUN:
		fe.run()
