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
		
		# フィールド
		pix = [8, 0, 256-8, 224-8-1]
		self.field = self.get(pix)
		
		# 48x64+ mergin
		
		# 人物1,2(屋内)
		pix = [32-1,96-1,32+48,96+64]
		self.person1 = self.get(pix)
		
		pix = [160-1,96-1,160+48,96+64]
		self.person2 = self.get(pix)
		
		
		# 人物3,4(屋外)
		pix = [40-1,88-1,40+48,88+64]
		self.person3 = self.get(pix)
		
		pix = [168-1,88-1,168+48,88+64]
		self.person4 = self.get(pix)
		
		# 人物5(戦闘)
		pix = [8-1,136-1,8+48,136+64]
		self.person5 = self.get(pix)
		
		# 戦闘
		#pix = [8, 0, 256-8, 134-8-1]
		pix = [8, 16, 256-8, 127-1]
		self.battle = self.get(pix)
		
		# 戦闘(屋外)
		pix = [8, 16, 256-8, 127-1]
		self.battle7 = self.get(pix)
		
class fe_ivent(fe_compose):
	""" 会話シーンクラス( 結合) """
	TEMP_DIR='temp'
	def __init__(self):
		"""初期化"""
		super().__init__(fe_pil_talk)
	
	def save_temp_file(self):
		""" 保存 """
		for i, fe in enumerate(self.fe):
			filename = self.TEMP_DIR + '/{0:0>2}0.png'.format(i)
			fe.field.save(filename)
	
			filename = self.TEMP_DIR + '/{0:0>2}1.png'.format(i)
			fe.person1.save(filename)
			
			filename = self.TEMP_DIR + '/{0:0>2}2.png'.format(i)
			fe.person2.save(filename)
			
			filename = self.TEMP_DIR + '/{0:0>2}3.png'.format(i)
			fe.person3.save(filename)
			
			filename = self.TEMP_DIR + '/{0:0>2}4.png'.format(i)
			fe.person4.save(filename)
			
			filename = self.TEMP_DIR + '/{0:0>2}5.png'.format(i)
			fe.person5.save(filename)
			
			filename = self.TEMP_DIR + '/{0:0>2}6.png'.format(i)
			fe.battle.save(filename)
			
			filename = self.TEMP_DIR + '/{0:0>2}7.png'.format(i)
			fe.battle7.save(filename)
			
			
			
	def run(self):
		""" 実行 """
		self.del_temp()
		self.read()
		self.save_temp_file()
		
if __name__ == '__main__':
	
	import fe_param_00.ivent06 as p
	
	fe = fe_ivent()
	fe.configure(p)
	fe.run()
	
