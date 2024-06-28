# -*- coding: utf-8 -*-

from fe_pil import fe_pil
from fe_compose import fe_compose

class fe_battle(fe_compose):
	""" バトルクラス(GIF) """
	def read10(self):
		""" 画像の読み込み """
		self.fe = []
		# フレームを間引く(60->10fps)
		for i, f in enumerate(self.file_paths):
			if i%6==0:
				fe = self.img_class(f)
				self.fe.append(fe)
				

if __name__ == '__main__':
	
	import battle00_2 as p
	
	fe = fe_battle()
	
	if 'dirs' in dir(p):
		for d in p.dirs:
			fe.add_dir(d)
	if 'files' in dir(p):
		fe.add_files(p.files)
		
	fe.set_out_file(p.out_file)
	fe.read()
	fe.save_gif(fps=50)
	
	#fe.set_out_file(p.out_file2)
	#fe.read10()
	#fe.save_gif(fps=10)
	