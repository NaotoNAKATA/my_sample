# -*- coding: utf-8 -*-

from fe_pil import fe_pil
from fe_compose import fe_compose
	
class fe_gif(fe_compose):
	""" アニメーションGIF作成 """
	def configure(self, param):
		""" 一括設定 """
		super().configure(param)
		
		if 'fps' in dir(param):
			self.fps = param.fps
			
	def run(self):
		""" 実行 """
		self.del_temp()
		self.read()
		self.save_gif(fps=self.fps)


if __name__ == '__main__':
	
	#import fe_param_00.prologue_gif as p
	import fe_param_01.battle02 as p
	
	# バトルシーン
	# 最初のバトルコマンド入力待ちが60フレーム
	# 会話入力待ちは三角が消えるまで
	# フィールドからバトルシーンへは、黒20フレーム
	# バトルからバトルへは黒10フレーム

	fe = fe_gif()
	fe.configure(p)
	fe.run()
	
