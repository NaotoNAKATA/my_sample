# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter, ImageDraw

class fe_pil(object):
	"""PIL動作クラス"""
	def __init__(self, path=None, bsize=16):
		"""初期化"""
		self.bsize = bsize
		if path==None:
			self.pil = None
		else:
			self.pil  = Image.open(path)
			self.update_size()
		
	def update_size(self):
		"""ブロックサイズの更新 """
		self.size = tuple(map( lambda x:int(x/self.bsize), self.pil.size ))
	
	def block_to_pix(self, block):
		""" ブロックをピクセルに変換 """
		b = list(block)
		if len(b)==4:
			b[2] += 1
			b[3] += 1
		pix = tuple(map(lambda x:x*self.bsize, b))
		
		return pix
		
	def set_pil(self, pil, bsize=16):
		""" 画像をセットする """
		self.pil = pil
		self.bsize = bsize
		self.update_size()
		
	def get(self, block):
		"""ブロックを切り出す"""
		pix = self.block_to_pix(block)
				
		# 新しいイメージを切り出す
		buf = fe_pil()
		buf.set_pil( self.pil.crop(pix), bsize=self.bsize)
		
		return buf
		
	def crop(self, block):
		"""クロップする"""
		pix = self.block_to_pix(block)
				
		# 元画像を編集する
		self.pil = self.pil.crop(pix)
		self.update_size()
	
	def paste(self, img, block):
		"""上書きする"""
		pix = self.block_to_pix(block)
		
		if img.pil.mode=='RGBA':
			self.pil.paste(img.pil, pix, img.pil)
		else:
			self.pil.paste(img.pil, pix)
		
		self.update_size()
	
	def save(self, path):
		"""保存"""
		self.pil.save(path)
		
	def save_draw_line(self, path):
		"""ブロック区切りの線を描いて保存"""
		# 元画像は残す
		pil = self.pil.copy()
		draw = ImageDraw.Draw(pil)
		
		w, h = self.pil.size
		for x in range(0, w, self.bsize):
			draw.line(((x,0), (x,h-1)),fill=(255,255,0), width=1)
			draw.text((x+3,1), '{0}'.format(int(x/self.bsize)), 'yellow')
			
		for y in range(0, h, self.bsize):
			draw.line(((0,y), (w-1,y)),fill=(255,255,0), width=1)
			draw.text((3,y+1), '{0}'.format(int(y/self.bsize)), 'yellow')
				
		pil.save(path)
	
class fe_blank(fe_pil):
	"""ブランクイメージ"""
	PIX_VAL = (128, 0, 128)
	
	def __init__(self, block, bsize=16):
		"""初期化"""
		self.bsize = bsize
		size = self.block_to_pix(block)
		self.pil = Image.new('RGB', size, self.PIX_VAL)
		self.update_size()

if __name__ == '__main__':
	
	#fe = fe_feild('./d.png')
	
	#print(fe.pil.size)
	#print(fe.size)
	
	#fe.save_draw_line('./d_temp.png')
	
	#fe.crop((3,2,5,5))
	#fe.save('./d2.png')
	
	
	pass
	