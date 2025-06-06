# -*- coding: utf-8 -*-

import os
import glob
import shutil

from fe_pil import fe_pil
from fe_compose import fe_compose
	
class fe_pil_fld(fe_pil):
	"""フィールドマップクラス(img) """
	def __init__(self, path):
		"""初期化"""
		super().__init__(path, bsize=16)
		
		self.init_local()
		
	def init_local(self):
		""" 各派生クラスの初期化 """
		# オリジナルは256,224
		
		# 左8,右8,下8は黒
		# キリをよくする+左8,右8,下8
		# 244,208
		pix = (8+8, 0, 256-8-8, 224-8-8)
		pil = self.pil.crop(pix)
		self.set_pil(pil, bsize=self.bsize)

class fe_field(fe_compose):
	""" フィールドマップクラス(結合) """
	def __init__(self, img_class=fe_pil_fld):
		"""初期化"""
		super().__init__(img_class)
	
	def test_run_first(self):
		""" テスト実行 """
		super().test_run_first()
		
		self.save_line_temp()
		
	def save_line_temp(self):
		""" ブロックライン付きで保存 """
		for i, fe in enumerate(self.fe):
			filename = self.TEMP_DIR + '/{0:0>2}.png'.format(i)
			fe.save_draw_line(filename)
		
	def compose_list(self):
		""" リストの画像を合成 """
		for i, (n, r) in enumerate(self.comp):
			x, y = r[:2]
			if len(r)>2:
				f = self.fe[n].get(r[2:])
			else:
				f = self.fe[n]
			
			self.compose(f, (x,y))
			
			# 途中経過
			if self.save_temp:
				filename = self.TEMP_DIR + '/field_{0:0>2}.png'.format(i)
				self.save(filename)
				
				filename = self.TEMP_DIR + '/line_field_{0:0>2}.png'.format(i)
				self.save_draw_line(filename)
		
class fe_field_a(fe_field):
	""" フィールドマップクラス(章間結合) """
	def __init__(self):
		"""初期化"""
		super().__init__(fe_pil)

if __name__ == '__main__':
	
	#import fe_param_03.field00 as p
	#fe = fe_field()
	
	import fe_param_a.field00 as p
	fe = fe_field_a()
	
	fe.configure(p)
	
	if p.TEST_RUN_FIRST:
		fe.test_run_first()
	if p.TEST_RUN:
		fe.test_run()
	if p.RUN:
		fe.run()
	
