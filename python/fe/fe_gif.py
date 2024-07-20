# -*- coding: utf-8 -*-

from fe_pil import fe_pil
from fe_compose import fe_compose
	
class fe_gif(fe_compose):
	""" アニメーションGIF作成 """
	def run(self, fps=0.5):
		""" 実行 """
		self.del_temp()
		self.read()
		self.save_gif(fps=fps)


if __name__ == '__main__':
	
	import fe_param_00.prologue_scene as p

	fe = fe_gif()
	fe.configure(p)
	fe.run(fps=p.fps)
	
