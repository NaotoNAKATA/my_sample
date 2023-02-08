# -*- coding: utf-8 -*-

import os
import glob
import shutil
from PIL import Image, ImageFilter, ImageDraw

class my_pil(object):
	"""PIL動作クラス"""
	def __init__(self, img):
		"""初期化"""
		self.img = img
		
	def get(self, block):
		"""1ブロック切り出す"""
		pix = [ block[0] * 32,
				block[1] * 32,
				block[0] * 32+32,
				block[1] * 32+32]
		return self.img.crop(pix)
		
	def crop(self, block):
		"""クロップする"""
		b = list(block)
		b[2] += 1
		b[3] += 1
		pix = tuple(map(lambda x:x*32, b))
		self.img = self.img.crop(pix)
	
	def paste(self, img, block, alpha=False):
		"""上書きする"""
		pix = tuple(map(lambda x:x*32, block))
		if not alpha:
			self.img.paste(img, pix)
		else:
			self.img.paste(img, pix, img)
		
	def save(self, path):
		"""保存"""
		self.img.save(path)
		
	def save_draw_line(self, path):
		"""ブロック区切りの線を描いて保存"""
		# 元画像は残す
		img = self.img.copy()
		draw = ImageDraw.Draw(img)
		
		w, h = self.img.size
		for x in range(0, w, 32):
			draw.line(((x,0), (x,h-1)),fill=(255,255,0), width=2)
			
		for y in range(0, h, 32):
			draw.line(((0,y), (w-1,y)),fill=(255,255,0), width=2)
		
		for x in range(0, w, 32):
			for y in range(0, h, 32):
				draw.text((x+3,y+1), '{0},{1}'.format(int(x/32),int(y/32)), 'yellow')
		
		img.save(path)

class my_img(my_pil):
	"""個別画像用"""
	def __init__(self, path, trim=True):
		"""初期化"""
		if trim:
			# (左,上, 右, 下)
			# 512x448 -> 480x384 = 15x12 (block)
			# 左側は16ピクセル余分にあるらしい
			roi = (16+16, 16, 512, 448-16-32)
			img = Image.open(path).crop(roi)
		else:
			img = Image.open(path)
		
		super().__init__(img)
		#print(self.img.format, self.img.size, self.img.mode)

class merge_img(my_pil):
	"""画像統合用"""
	def __init__(self, block):
		"""初期化"""
		pix = tuple(map(lambda x:x*32, block))
		img = Image.new('RGB', pix, (128, 0, 128))
		
		super().__init__(img)

class proc_img(object):
	"""処理クラス"""
	def __init__(self, path):
		"""初期化"""
		self.path = path
		self.img = []
		self.tmp = './tmp'
		self.sample = './sample'
		self.sample_dict = {}
		
		self.roi = {}
		self.paste_block = {}
		self.merge = []
		
		for d in [self.tmp]:
			if os.path.exists(d):
				shutil.rmtree(d)
			os.mkdir(d)
			
	def run(self):
		self.rename()
		self.load()
		self.crop()
		#self.merging()
	
	def rename(self):
		"""画像をリネーム"""
		path = self.path+'/000.png'
		if not os.path.exists(path):
			paths =  sorted(glob.glob(self.path+'/*t.png'))
			paths+=  sorted(glob.glob(self.path+'/*t(?).png'))
			paths+=  sorted(glob.glob(self.path+'/*t(??).png'))
			for i, f in enumerate(paths):
				dirname = os.path.dirname(f)
				os.rename(f, dirname + '/{0:0>3}.png'.format(i))
			
	def load(self):
		"""画像をクリップ"""
		for f in sorted( glob.glob(self.path+'/*.png') ):
			
			img = my_img(f)
			filename = os.path.basename(f)
			img.save_draw_line(self.tmp + '/' + filename)
			self.img.append(img)
	
	def crop(self):
		"""画像の切り出し"""
		for i, b in self.roi.items():
			self.img[i].crop(b)
			self.img[i].save_draw_line(self.tmp + '/' + '{0:0>3}.png'.format(i))
			
	def paste(self):
		"""画像の穴埋め"""
		for i, d in self.paste_block.items():
			for p,b in d:
				s = self.sample_dict[p]
				self.img[i].paste(s,b)
			self.img[i].save_draw_line(self.tmp + '/' + '{0:0>3}.png'.format(i))

	def get(self, i):
		"""イメージオブジェクトを取得"""
		return self.img[i]
		
	def gen_sample(self):
		"""サンプルリスト作成"""
		for f in sorted( glob.glob(self.sample+'/*.png') ):
			img = my_img(f, False)
			key = os.path.splitext( os.path.basename(f) )[0]
			self.sample_dict[key] = img.img
			
	def merging(self):
		"""リストの先頭からマージする"""
		for i, (m,(x,y)) in enumerate(self.merge):
			if i==0:
				merging_img = my_pil( self.img[m].img.copy() )
			else:
				w, h = merging_img.img.size
				xi, yi = x*32, y*32
				wi, hi = self.img[m].img.size
				
				def update_w(w, xi, wi):
					if xi>=0:
						if xi+wi>=w:
							w_new = xi+wi
						else:
							w_new = w
					else:
						if xi+wi>=w:
							w_new = wi
						else:
							w_new = abs(xi) + w
					return w_new
				
				w_new = update_w(w, xi, wi)
				h_new = update_w(h, yi, hi)
				
				block = (int(w_new/32), int(h_new/32))
				buf = merge_img(block)
				
				x0, x1 = (0, x) if x>=0 else (abs(x), 0)
				y0, y1 = (0, y) if y>=0 else (abs(y), 0)
					
				buf.paste(merging_img.img, (x0,y0))
				buf.paste(self.img[m].img, (x1,y1))
				merging_img = my_pil( buf.img.copy() )
				
			merging_img.save_draw_line(self.tmp + '/merge{0:0>3}.png'.format(i))
			merging_img.save(self.tmp + '/' + self.merge_name + '.png')
		
	def delete(self):
		"""終了"""
		pass

class my_img_a(my_pil):
	def __init__(self, path, alpha=False):
		img = Image.open(path)
		super().__init__(img)
		
		# アルファの設定
		if alpha:
			# 無効部分だけアルファ設定
			w, h = img.size
			
			g = Image.new('L', self.img.size, 255)
			dg = ImageDraw.Draw(g)
			
			for y in range(0,h,32):
				for x in range(0,w,32):
					p0 = img.getpixel((x,y))
					p1 = img.getpixel((x+16,y+16))
					if p0==p1 and p0==(128,0,128):
						pix = (x, y, x+32, y+32)
						dg.rectangle(pix, fill=0)
						
			self.img_a = self.img.copy()
			self.img_a.putalpha(g)
			
		else:
			# 全面アルファ(不透過)
			self.img_a = self.img.copy()
			self.img_a.putalpha(255)
		
	def save(self, path):
		super().save(path)
	
class merge_alpha(object):
	"""既に統合したもの同士を統合する"""
	def __init__(self):
		pass
	
	def set_u(self, path):
		# 上位の画像。アルファを設定する
		self.img_u = my_img_a(path, alpha=True)
		self.img_u.save_draw_line('./tmpu.png')
		
	def set_l(self, path):
		# 下位の画像。アルファはすべて不透過
		self.img_l = my_img_a(path, alpha=False)
		self.img_l.save_draw_line('./tmpl.png')
		
	def run(self, block):
		# 統合後の画像作成
		w, h = self.img_l.img.size
		bw = int(w/32) + block[0]
		bh = int(h/32) + block[1]
		
		m = merge_img((bw,bh))
		
		# 下位を貼り付け
		m.paste(self.img_l.img, (0,0))
		
		# 上位を貼り付け
		m.paste(self.img_u.img_a, block, alpha=True)
		
		m.save('./tmp.png')
		

if __name__ == '__main__':
	
	#p = proc_img('002-リザザ')
	#p.rename()
	
	#m = my_img_a('./全体マップ/Map001.png', alpha=True)
	m = merge_alpha()
	m.set_l('./全体マップ/Map001.png')
	
	m.set_u('./全体マップ/Map002.png')
	
	m.run((4,9))
	
	
	