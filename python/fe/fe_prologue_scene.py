# -*- coding: utf-8 -*-

from fe_pil import fe_pil
from fe_prologue import fe_prologue
	
class fe_prologue_scene(fe_prologue):
	""" プロローグクラス(スライド) """
	def save(self):
		""" メイン画像の保存 """
		for i, fe in enumerate(self.fe):
			filename = self.TEMP_DIR + '/{0:0>2}.png'.format(i)
			fe.save(filename)
	
	def configure(self, param):
		""" 一括設定 """
		super().configure(param)
		
		if 'org_im' in dir(param):
			self.org_im = param.org_im
	
	def save_main_temp(self):
		""" メイン画像の保存 """
		for i, fe in enumerate(self.fe):
			filename = self.TEMP_DIR + '/{0:0>2}.png'.format(i)
			if i in self.org_im:
				fe.save(filename)
			else:
				fe.save_main(filename)

	def run(self):
		""" 実行 """
		self.del_temp()
		self.read()
		self.save_main_temp()
		
if __name__ == '__main__':
	
	import fe_param_00.prologue_scene as p
	
	fe = fe_prologue_scene()
	fe.configure(p)
	fe.run()
	
