# -*- coding: utf-8 -*-

from fe_pil import fe_pil
from fe_compose import fe_compose
	
class fe_pil_prlg(fe_pil):
	"""プロローグクラス(img) """
	def __init__(self, path):
		"""初期化"""
		super().__init__(path, bsize=1)
		
		self.init_local()
		
	def init_local(self):
		""" 各派生クラスの初期化 """
		# オリジナルは256,224
		
		# 画像部分の切り出し
		# 241,153
		self.img_main = self.get([8,9,255-7,161])
		
		# テキスト部分の切り出し
		# 241,46
		self.img_text = self.get([8,169,255-7,214])
	
	def save_main(self, path):
		""" 画像部分の保存 """
		self.img_main.save(path)
	
	def save_text(self, path):
		""" テキスト部分の保存 """
		self.img_text.save(path)

class fe_prologue(fe_compose):
	""" プロローグクラス( 結合) """
	def __init__(self):
		"""初期化"""
		super().__init__(fe_pil_prlg)
		
	def test_run_first(self):
		""" テスト実行 """
		super().test_run_first()
		
		self.save_main_temp()
	
	def save_main_temp(self):
		""" メイン画像の保存 """
		for i, fe in enumerate(self.fe):
			filename = self.TEMP_DIR + '/{0:0>2}.png'.format(i)
			fe.save_main(filename)
	
	def compose_list(self):
		""" リストの画像を合成 """
		for i, (n, (x,y)) in enumerate(self.comp):
			f = self.fe[n].img_main
			self.compose(f, (x,y))
			
			# 途中経過
			if self.save_temp:
				filename = self.TEMP_DIR + '/prlg_{0:0>2}.png'.format(i)
				self.save(filename)
		
if __name__ == '__main__':
	
	import fe_param_06.prologue_map as p
	
	fe = fe_prologue()
	fe.configure(p)
	
	if p.TEST_RUN_FIRST:
		fe.test_run_first()
	if p.TEST_RUN:
		fe.test_run()
	if p.RUN:
		fe.run()
	
	if 'GIF' in dir(p):
		if p.GIF:
			fe.read()
			fe.save_gif(fps=0.5)
	