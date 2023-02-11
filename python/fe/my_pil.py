# -*- coding: utf-8 -*-

import os
import glob
import shutil
from PIL import Image, ImageFilter, ImageDraw

class my_pil(object):
	"""PIL動作クラス"""
	def __init__(self, pil):
		"""初期化"""
		self.pil = pil
		self.update_size()
	
	def update_size(self):
		"""ブロックサイズの更新"""
		self.size = tuple(map( lambda x:int(x/32), self.pil.size ))
	
	def get(self, block):
		"""1ブロック切り出す"""
		b = list(block*2)
		b[2] += 1
		b[3] += 1
		pix = tuple(map(lambda x:x*32, b))
		pil = self.pil.crop(pix)
		return my_pil(pil)
		
	def crop(self, block):
		"""クロップする"""
		b = list(block)
		b[2] += 1
		b[3] += 1
		pix = tuple(map(lambda x:x*32, b))
		self.pil = self.pil.crop(pix)
		self.update_size()
	
	def paste(self, img, block):
		"""上書きする"""
		pix = tuple(map(lambda x:x*32, block))
		if img.pil.mode=='RGBA':
			self.pil.paste(img.pil, pix, img.pil)
		else:
			self.pil.paste(img.pil, pix)
		self.update_size()
		
	def add_alpha(self, blocks):
		"""アルファチャンネルを追加する"""
		# アルファチャンネル画像
		g = Image.new('L', self.pil.size, 255)
		dg = ImageDraw.Draw(g)
		
		# 1Blockずつ設定する
		for block in blocks:
			x = block[0] * 32
			y = block[1] * 32
			
			# rectの右下座標は？とりあえずこれで
			pix = (x, y, x+32-1, y+32-1)
			dg.rectangle(pix, fill=0, outline=None)
		
		# アルファチャンネルを追加
		self.pil.putalpha(g)
		
	def save(self, path):
		"""保存"""
		self.pil.save(path)
		
	def save_draw_line(self, path):
		"""ブロック区切りの線を描いて保存"""
		# 元画像は残す
		pil = self.pil.copy()
		draw = ImageDraw.Draw(pil)
		
		w, h = self.pil.size
		for x in range(0, w, 32):
			draw.line(((x,0), (x,h-1)),fill=(255,255,0), width=2)
			
		for y in range(0, h, 32):
			draw.line(((0,y), (w-1,y)),fill=(255,255,0), width=2)
		
		for x in range(0, w, 32):
			for y in range(0, h, 32):
				draw.text((x+3,y+1), '{0},{1}'.format(int(x/32),int(y/32)), 'yellow')
		
		pil.save(path)

class trim_img(my_pil):
	"""トリミングしたイメージ"""
	def __init__(self, path):
		"""初期化"""
		# (左,上, 右, 下)
		# 512x448 -> 480x384 = 15x12 (block)
		# 左側は16ピクセル余分にあるらしい
		roi = (16+16, 16, 512, 448-16-32)
		pil = Image.open(path).crop(roi)
		super().__init__(pil)

class norm_img(my_pil):
	"""通常イメージ(トリミング済みイメージ)"""
	def __init__(self, path):
		"""初期化"""
		pil = Image.open(path)
		super().__init__(pil)
		
class blank_img(my_pil):
	"""ブランクイメージ"""
	pix_val = (128, 0, 128)
	def __init__(self, block):
		"""初期化"""
		size = tuple(map(lambda x:x*32, block))
		pil = Image.new('RGB', size, blank_img.pix_val)
		super().__init__(pil)

class alpha_img(my_pil):
	"""アルファチャンネル付きのイメージ"""
	def __init__(self, path):
		"""初期化"""
		pil = Image.open(path)
		
		# アルファチャンネル画像
		g = Image.new('L', pil.size, 255)
		dg = ImageDraw.Draw(g)
		
		# 無効部分の判定
		w, h = pil.size
		for y in range(0,h,32):
			for x in range(0,w,32):
				# とりあえず２点くらいみとく
				p0 = pil.getpixel((x,y))
				p1 = pil.getpixel((x+16,y+16))
				if p0==p1 and p0==blank_img.pix_val:
					# rectの右下座標は？とりあえずこれで
					pix = (x, y, x+32-1, y+32-1)
					dg.rectangle(pix, fill=0)
					
		# アルファチャンネルの設定
		pil.putalpha(g)
		super().__init__(pil)

class proc_img(object):
	"""一括処理クラス"""
	def __init__(self, path):
		"""初期化"""
		# 処理するディレクトリ
		self.path = path
		
		# 一括処理するイメージ
		self.img = []
		
		# 画像の有効範囲 { i : (bx0, by0, bx1, by1) }
		self.roi = {}
		
		# 画像を置換 { i : ( (name, (bx0, by0)), ..., ) } 
		self.paste = {}
		
		# 画像をマージ { name :[(i, (bx0,by0), ..., ]}
		self.merge_list = {}
		
		# 置換用サンプルリスト
		self.sample_path = './sample'
		self.sample = {} # 読み込んだ画像
		self.sample_imgs = {} # 保存するリスト
		
		# 一時保存用ディレクトリ
		self.tmp = './tmp'
		
		# 一時ディレクトリは毎回削除する
		for d in [self.tmp]:
			if os.path.exists(d):
				shutil.rmtree(d)
			os.mkdir(d)
		
	def run(self):
		"""一括実行"""
		self.rename()
		self.load()
		self.crop()
		self.get_sample()
		self.gen_sample()
		self.replace()
		self.merge()
		
	def rename(self):
		"""画像をリネーム"""
		# 既に連番ファイルがあれば続きにする
		n = len( glob.glob(self.path+'/???.png') )
		
		# 日付ソートが上手くできないのでファイル名でソート
		paths =  sorted(glob.glob(self.path+'/*t.png'))
		paths+=  sorted(glob.glob(self.path+'/*t(?).png'))
		paths+=  sorted(glob.glob(self.path+'/*t(??).png'))
		paths+=  sorted(glob.glob(self.path+'/*t(???).png'))
		
		# 連番になるようにリネーム実行
		for i, f in enumerate(paths):
			dirname = os.path.dirname(f)
			os.rename(f, dirname + '/{0:0>3}.png'.format(i+n))
			
	def load(self):
		"""画像の読み込み"""
		for f in sorted( glob.glob(self.path+'/*.png') ):
			img = trim_img(f)
			self.img.append(img)
			
			# 確認用にライン画像を保存
			filename = os.path.basename(f)
			img.save_draw_line(self.tmp + '/' + filename)
			
	def crop(self):
		"""画像の不要部分を切り落とす"""
		for i, b in self.roi.items():
			self.img[i].crop(b)
			
			# 確認用にライン画像を上書き
			self.img[i].save_draw_line(self.tmp + '/' + '{0:0>3}.png'.format(i))
	
	def gen_sample(self):
		"""置換用サンプルリスト作成"""
		for f in sorted( glob.glob(self.sample_path+'/*.png') ):
			key = os.path.splitext( os.path.basename(f) )[0]
			self.sample[key] = norm_img(f)
			
	def get_sample(self):
		"""サンプルイメージを保存する"""
		for i, s in self.sample_imgs.items():
			for name, block in s:
				path = self.sample_path + '/' + name + '.png'
				self.img[i].get(block).save(path)
	
	def replace(self):
		"""画像の置換"""
		# １ブロックずつ画像を置換
		for i, p in self.paste.items():
			for name, block in p:
				sample = self.sample[name]
				self.img[i].paste(sample, block)
			
			# 確認用にライン画像を上書き
			self.img[i].save_draw_line(self.tmp + '/' + '{0:0>3}.png'.format(i))
	
	def merge(self):
		"""リストの先頭からマージする"""
		for name , mlist in self.merge_list.items():
			for i, (m,(bx,by)) in enumerate(mlist):
				if i==0:
					# 最初はそのまま貼り付け
					buf = blank_img( self.img[m].size )
					buf.paste( self.img[m], (0,0) )
				else:
					bw0, bh0 = buf.size
					bw1, bh1 = self.img[m].size
					
					# 貼り付けるベースの画像を作成
					bw = self.update_w(bw0, bx, bw1)
					bh = self.update_w(bh0, by, bh1)
					base = blank_img((bw, bh))
					
					# 座標の判定
					bx0, bx1 = (0, bx) if bx>=0 else (abs(bx), 0)
					by0, by1 = (0, by) if by>=0 else (abs(by), 0)
				
					# リストの前の画像の上に後の画像を貼り付ける
					base.paste( buf, (bx0, by0) )
					base.paste( self.img[m], (bx1, by1) )
					buf = base
			
				# 確認用に連番で保存
				buf.save_draw_line(self.tmp + '/merge{0:0>3}.png'.format(i))
			
			# 完成画像を保存する
			buf.save(self.tmp + '/' + name + '.png')
	
	def update_w(self, bw0, bx, bw1):
		"""マージ用に新しいブロックサイズを計算"""
		if bx>=0:
			if bx+bw1>=bw0:
				bw = bx+bw1
			else:
				bw = bw0
		else:
			if bx+bw1>=bw0:
				bw = bw1
			else:
				bw = abs(bx) + bw0
		return bw

class merge_alpha(proc_img):
	"""既に統合したもの同士を統合する"""
	def __init__(self, path):
		"""初期化"""
		super().__init__(path)
		
	def load(self):
		"""画像の読み込み"""
		for f in sorted( glob.glob(self.path+'/*.png') ):
			img = alpha_img(f)
			self.img.append(img)
			
			# 確認用にライン画像を保存
			filename = os.path.basename(f)
			img.save_draw_line(self.tmp + '/' + filename)
	
	def run(self):
		"""一括実行"""
		self.load()
		self.merge()
		
if __name__ == '__main__':
	# trim_img, norm_img, blank_imgクラスのテスト
	a = trim_img('./a.png')
	print('a.size', a.size, a.pil.size)
	a.save('./a01.png')
	a.save_draw_line('./a02.png')
	
	a90 = a.get((9,10))
	print('a90.size', a90.size, a90.pil.size)
	a90.save('./a90.png')
	
	a.crop((1,1,13,10))
	print('a.crop.size', a.size, a.pil.size)
	a.save('./a03.png')
	a.save_draw_line('./a04.png')
	
	a.paste(a90, (1,1))
	a.save('./a05.png')
	print('a.paste.size', a.size, a.pil.size)
	
	# 貼り付けられる側の範囲外は無視される
	a.paste(a90, (13,9))
	a.save('./a06.png')
	print('a.paste.size', a.size, a.pil.size)
	
	b = nrom_img('./b.png')
	a.paste(b, (10,5))
	a.save('./a07.png')
	print('a.paste.size', a.size, a.pil.size)
	
	d = blank_img((15,12))
	d.save_draw_line('./d0.png')
	print('d0.size', d.size, d.pil.size)
	
	
	