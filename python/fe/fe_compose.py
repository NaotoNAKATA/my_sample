# -*- coding: utf-8 -*-

import os
import glob
import shutil

from fe_pil import fe_pil
from fe_pil import fe_blank
	
class fe_compose(object):
	""" 結合クラス """
	TEMP_DIR = 'temp'
	def __init__(self, img_class=fe_pil):
		"""初期化"""
		# 画像のリスト
		self.fe = []
		
		# 処理する画像ファイルパスのリスト
		self.file_paths = []
		
		# 画像クラス
		self.img_class = img_class
		
		# 結合のベース画像
		self.base = None
		
		# 結合リスト
		self.comp = []
		
		# 途中経過
		self.save_temp = True
		
		# 出力ファイル名
		self.out_file = './base.png'
		
	def del_temp(self):
		""" tempの削除 """
		if os.path.exists(self.TEMP_DIR):
			shutil.rmtree(self.TEMP_DIR)
		os.mkdir(self.TEMP_DIR)
		
	def add_dir(self, dir):
		"""画像ディレクトリの追加"""
		# ディレクトリの確認
		if not os.path.exists(dir):
			return
		
		# ファイルリストの作成
		for f in sorted( glob.glob(dir + '/*.png') ):
			self.file_paths.append(f)
	
	def add_file(self, paths):
		"""画像ファイルの追加"""
		self.file_paths += paths
	
	def test_run_first(self):
		""" テスト実行 """
		self.del_temp()
		self.read()
	
	def test_run(self):
		""" テスト実行 """
		self.read()
		
		self.save_temp = True
		self.compose_list()
	
	def run(self):
		""" 実行 """
		self.del_temp()
		self.read()
		
		self.save_temp = False
		self.compose_list()
		
		self.save( self.out_file )
	
	def read(self):
		""" 画像の読み込み """
		for f in self.file_paths:
			fe = self.img_class(f)
			self.fe.append(fe)
	
	def compose(self, upper, xy):
		""" 画像の合成 """
		if self.base==None:
			self.base = upper
			return
		
		# xy: baseに対するupperの位置
		x, y = xy
		lw, lh = self.base.size
		uw, uh = upper.size
		
		# 合成後の画像サイズの計算
		def calc_w(x, lw, uw):
			if x>=0:
				if lw<=(x+uw):
					w = x+uw
				else:
					w = lw
			else:
				if (-x+lw)>=uw:
					w = -x+lw
				else:
					w = uw
			return w
		
		w = calc_w(x, lw, uw)
		h = calc_w(y, lh, uh)
		
		# 画像貼り付け位置の計算
		def calc_x(x):
			if x>=0:
				lx = 0
				ux = 0+x
			else:
				lx = 0+(-x)
				ux = 0
			return lx, ux
		
		lx, ux = calc_x(x)
		ly, uy = calc_x(y)
		
		# ベース画像の作成
		base= fe_blank((w,h), bsize=self.base.bsize)
		
		# 画像の貼り付け
		base.paste(self.base, (lx, ly))
		base.paste(upper, (ux, uy))
		
		# ベース画像の更新
		self.base = base
		
	def save(self, path):
		""" 画像の保存 """
		self.base.save(path)
		
	def save_draw_line(self, path):
		""" 画像の保存 """
		self.base.save_draw_line(path)
	
	def save_gif(self, fps=10):
		""" アニメーションgifの保存 """
		self.fe[0].save_gif(self.out_file, self.fe[1:], fps=fps)
	
	def set_compose(self, comp):
		""" 合成リストのセット """
		self.comp = comp
	
	def set_out_file(self, filename):
		""" 出力ファイル名 """
		self.out_file = filename
	
	def compose_list(self):
		""" リストの画像を合成 """
		pass
