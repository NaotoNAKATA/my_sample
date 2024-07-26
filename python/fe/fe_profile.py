# -*- coding: utf-8 -*-

import os
import glob
import shutil

from fe_pil import fe_pil
from fe_compose import fe_compose
	
class fe_pil_prof(fe_pil):
	"""プロフィール画像(img)"""
	def __init__(self, path):
		"""初期化"""
		super().__init__(path, bsize=1)
		
		self.init_local()
		
	def init_local(self):
		""" 各派生クラスの初期化 """
		# オリジナルは256,224
		# 48x64+ mergin
		pix = (98-1, 12-1, 256-110+1, 224-148+1)
		pil = self.pil.crop(pix)
		self.set_pil(pil, bsize=self.bsize)

class fe_profile(fe_compose):
	""" フィールドマップクラス( 結合) """
	def __init__(self):
		"""初期化"""
		super().__init__(fe_pil_prof)
	
	def add_dir(self, dir):
		"""画像ディレクトリの追加"""
		# ディレクトリの確認
		if not os.path.exists(dir):
			return
		
		# ファイルリストの作成
		# 2つ飛ばし
		for i, f in enumerate(sorted( glob.glob(dir + '/*.png') )):
			if i%3==0:
				self.file_paths.append(f)
	
	def save_temp_file(self):
		""" 保存 """
		for i, fe in enumerate(self.fe):
			filename = self.TEMP_DIR + '/{0:0>2}.png'.format(i)
			fe.save(filename)
	
	def save_all(self):
		"""  """
		
		pass
	
	
	def run(self):
		""" 実行 """
		self.del_temp()
		self.read()
		self.save_temp_file()
		
if __name__ == '__main__':
	
	import fe_param_00.profile02 as p
	
	fe = fe_profile()
	fe.configure(p)
	fe.run()
	