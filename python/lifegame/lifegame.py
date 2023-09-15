# -*- coding: utf-8 -*-

import os
from PIL import Image, ImageFilter, ImageDraw
import random

class box(object):
	"""個々の箱クラス"""
	def __init__(self, _da=False):
		"""初期化"""
		self.da = _da
		self.next = False
		
	def set_neighborhood(self,_nb):
		"""近傍の設定"""
		self.nb = _nb
	
	def judge(self):
		"""生死の判定"""
		f = lambda x:x.da==True
		n = len( tuple(filter(f, self.nb)) )
		if self.da:
			if n==2 or n==3:
				self.next = True
			else:
				self.next = False
		else:
			if n==3:
				self.next = True
			else:
				self.next = False
		
	def update(self):
		"""生死の更新"""
		self.da = self.next
		
class lifegame(object):
	"""ライフゲームクラス"""
	def __init__(self, filepath=None):
		"""初期化"""
		# 1個のピクセルサイズ
		self.pix = 16
		
		# 画像リスト
		self.life_img = []
		
		# 初期値の読み込み
		self.life = []
		if filepath!=None:
			self.load(filepath)
			self.savepath = os.path.splitext(filepath)[0] + '.gif'
		else:
			# 初期値の指定が無いときは乱数で
			self.h, self.v = (64, 64)
			self.savepath = './rand.gif'
			for y in range(self.v):
				a = [ box(True) if random.randint(0,1)==1 else box(False) for x in range(self.h) ]
				self.life.append(a)
		
		# 近傍の設定
		self.set_neighborhood()
		
	def load(self, filepath):
		"""初期値ファイルの読み込み"""
		with open(filepath, 'r') as f:
			for i,row in enumerate(f):
				if i==0:
					self.h, self.v = ( int(j) for j in row.split(',') )
				else:
					self.life.append(
						[ box(True) if int(j)==1 else box(False) for j in row.split(',') ]
					)
	
	def set_neighborhood(self):
		"""近傍の設定"""
		for y in range(self.v):
			for x in range(self.h):
				# 近傍のインデックスの設定
				if y==0:
					if x==0:
						nb_idx = [
							                 
							                               [x+1, y],
							                 [x, y+1],[x+1, y+1],
						]
					elif x==(self.h-1):
						nb_idx = [
							
							[x-1, y],                  
							[x-1, y+1],[x, y+1],
						]
					else:
						nb_idx = [
							
							[x-1, y],                  [x+1, y],
							[x-1, y+1],[x, y+1],[x+1, y+1],
						]
				elif y==(self.v-1):
					if x==0:
						nb_idx = [
							                 [x, y-1], [x+1, y-1],
							                               [x+1, y],
							                 
						]
					elif x==(self.h-1):
						nb_idx = [
							[x-1, y-1], [x, y-1],
							[x-1, y],                  
							
						]
					else:
						nb_idx = [
							[x-1, y-1], [x, y-1], [x+1, y-1],
							[x-1, y],                  [x+1, y],
							
						]
				else:
					if x==0:
						nb_idx = [
							                 [x, y-1], [x+1, y-1],
							                               [x+1, y],
							                 [x, y+1],[x+1, y+1],
						]
					elif x==(self.h-1):
						nb_idx = [
							[x-1, y-1], [x, y-1],
							[x-1, y],                  
							[x-1, y+1],[x, y+1],
						]
					else:
						nb_idx = [
							[x-1, y-1], [x, y-1], [x+1, y-1],
							[x-1, y],                  [x+1, y],
							[x-1, y+1],[x, y+1],[x+1, y+1],
						]
				
				# 近傍のセルの参照を渡す
				nb = []
				for [xi, yi] in nb_idx:
					nb.append(self.life[yi][xi])
				self.life[y][x].set_neighborhood(nb)
		
	def run(self, num):
		"""実行"""
		# 初期画面の作成
		self.make_img()
		
		# 実行する
		for n in range(num):
			print(n)
			# 各セルの判定
			for y in range(self.v):
				for x in range(self.h):
					self.life[y][x].judge()
			
			# 各セルの更新
			for y in range(self.v):
				for x in range(self.h):
					self.life[y][x].update()
					
			self.make_img()
					
		# 保存する
		self.save()
	
	def make_img(self):
		"""PILイメージを作成する"""
		# 空のファイルを白ベタで作成
		size = (self.h*self.pix, self.v*self.pix)
		pil = Image.new('L', size, color=255)
		
		# 矩形描画用
		draw = ImageDraw.Draw(pil)
		
		# 生の箇所は黒く塗る
		for y in range(self.v):
			for x in range(self.h):
				if self.life[y][x].da:
					block = (x*self.pix, y*self.pix, (x+1)*self.pix, (y+1)*self.pix)
					draw.rectangle(block, fill=0, outline=None)
		
		# 画像を保持する
		self.life_img.append(pil)
		
	def save(self):
		"""ファイルを保存する"""
		
		# アニメーションgifのフレームレート
		f = 5 # fps
		d = 1000 / f
		
		# 保存する
		self.life_img[0].save(
			self.savepath,
			save_all=True,
			append_images=self.life_img[1:],
			duration=d, loop=0)
		
if __name__ == '__main__':
	#l = lifegame('./test.csv')
	
	#l = lifegame('./glider_gun.csv')
	l = lifegame()
	l.run(90)
	