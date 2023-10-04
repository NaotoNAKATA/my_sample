# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter, ImageDraw

class ss_crop(object):
	"""PIL動作クラス"""
	def __init__(self, path,
		#crop= [6, 106, 1074, 826], split_y=500):
		crop= [4, 59, 716, 556], split_y=356, _mask_sel=0):
		"""初期化"""
		self.img_main = Image.open(path)
		
		# x0,y0,x1,y1
		self.crop = crop
		
		# y0
		self.split_y = split_y
		
		# 画像のマスク
		self.mask_sel = _mask_sel
		
		self.clop_main()
		self.split_img()
		
	def clop_main(self):
		""" 画面のみ切り出し """
		self.img_main = self.img_main.crop( self.crop )
		
	def split_img(self):
		""" 画面分割 """
		x1, y1 = self.img_main.size
		self.img_y0 = self.img_main.crop( [0, 0, x1, self.split_y] )
		# 画像の右端は削除
		#self.img_y1 = self.img_main.crop( [0, self.split_y+1, x1-71, y1] )

		# 画像の右下のアイコンを塗りつぶし
		self.img_y1 = self.img_main.crop( [0, self.split_y+1, x1, y1] )
		#pix_val = (0, 0, 0)
		#size = (35, 35)
		#pil = Image.new('RGB', size, pix_val)
		if self.mask_sel==0:
			pil = Image.open('./ss_sample.bmp')
		else:
			pil = Image.open('./ss_sample2.bmp')
		pix= (641, 88)
		self.img_y1.paste(pil, pix)
		
	def crop_letter(self):
		""" 一文字ずつ切り出す """
		self.img_let = []
		for j in range(3):
			for i in range(18):
				y0, x0 = j * 35 + 14, int(i * 35.5) + 35
				y1, x1 = y0 + 37, x0 + 37
				img_let = self.img_y1.crop([x0, y0, x1, y1])
				
				# 明らかに文字がないときは無視する
				if False:
					continue
					
				#img_let.save('./test{0:0>2}_{1:0>2}.png'.format(j,i))
				self.img_let.append( img_let )
		
	def get(self, img):
		""" バイトストリームを返す """
		import io
		img_io = io.BytesIO()
		img.save(img_io, 'PNG')
		return img_io
	
	def get_main(self):
		return self.get( self.img_main )
	
	def get_y0(self):
		return self.get( self.img_y0 )
		
	def get_y1(self):
		return self.get( self.img_y1 )
		
	def save_main(self, path):
		""" 全体を保存する """
		self.img_main.save(path)
		
	def save_y0(self, path):
		""" y0を保存する """
		self.img_y0.save(path)
		
	def save_y1(self, path):
		""" y1を保存する """
		self.img_y1.save(path)
		
if __name__ == '__main__':
	s = ss_crop('./test.png')
	
	s.save_main('./test1_main.png')
	s.save_y0('./test1_y0.png')
	s.save_y1('./test1_y1.png')
	
	#s.crop_letter()
	
