# -*- coding: utf-8 -*-

from ss_crop import ss_crop

from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH


import numpy as np

import os
import glob

class ss_doc(object):
	""" Document作成クラス """
	def __init__(self, _dir='./scene'):
		""" 初期化 """
		self.doc = Document()
		
		# 処理するディレクトリ
		#date/編/シーン/xxx-com-com
		self.dir = _dir
		
	def add_header(self, _text):
		""" 見出しの挿入 """
		p = self.doc.add_paragraph(_text, style='Heading 1')
		p.style.font.bold = False
		p.style.font.size = Pt(12)
		p.style.font.color.rgb = RGBColor(0,0,0)
	
	def add_img_main(self):
		""" メイン画像の挿入 """
		# 一つ前の画像と比較する
		if self.ss_pre!=None:
			pre = np.asarray( self.ss_pre.img_y0 ).copy()
			now = np.asarray( self.ss.img_y0 ).copy()
			
			if np.array_equal(pre, now):
				return
		
		p = self.doc.add_paragraph()
		r = p.add_run()
		p.line_spacing = Pt(10)
		p.alignment = WD_ALIGN_PARAGRAPH.CENTER
		r.add_picture( self.ss.get_y0(), width=Cm(9.42) )
		
	def add_img_text(self):
		""" セリフ画像の挿入 """
		p = self.doc.add_paragraph()
		r = p.add_run()
		p.line_spacing = Pt(10)
		r.add_picture( self.ss.get_y1(), width=Cm(6.3) )
	
	def add_ocr(self):
		""" OCRする """
		if True:
			# Androidではやり方わからず
			import pyocr
			tools = pyocr.get_available_tools()
			tool = tools[0]
			builder = pyocr.builders.TextBuilder(tesseract_layout=6)
			#text = tool.image_to_string(self.ss.img_y1, lang="Japanese", builder=builder)
			text = tool.image_to_string(self.ss.img_y1, lang="tessdata/jpn", builder=builder)
			
			# ある程度置換しておく
			replace_list = (
				(' ',''),
				('\r',''),
				('\n',''),
				('?','？'),
				('!','！'),
				('1','１'),('2','２'),('3','３'),('4','４'),('5','５'),
				('6','６'),('7','７'),('8','８'),('9','９'),('0','０'),
				('…','・・'),
				('-','・'),
				('(','（'),
				(')','）'),
				(']】','】'),
				('】]','】'),
				('[【','【'),
				('【[','【'),
				(']','】'),
				('[','【'),
				('|',''),
				('きん','さん'),
				('っつ','っ'),
				('大立夫','大丈夫'),
				('真紀子','真弥子'),
				('真断子','真弥子'),
				('真聞子','真弥子'),
				('真新子','真弥子'),
				('真綿子','真弥子'),
				('真絢子','真弥子'),

				('真紀二','真弥子'),
				('真断二','真弥子'),
				('真聞二','真弥子'),
				('真新二','真弥子'),
				('真綿二','真弥子'),
				('真絢二','真弥子'),

				('真紀才','真弥子'),
				('真断才','真弥子'),
				('真聞才','真弥子'),
				('真新才','真弥子'),
				('真綿才','真弥子'),
				('真絢才','真弥子'),

				('真紀す','真弥子'),
				('真断す','真弥子'),
				('真聞す','真弥子'),
				('真新す','真弥子'),
				('真綿す','真弥子'),
				('真絢す','真弥子'),

				('真紀地','真弥子'),
				('真断地','真弥子'),
				('真聞地','真弥子'),
				('真新地','真弥子'),
				('真綿地','真弥子'),
				('真絢地','真弥子'),

				('真紀了','真弥子'),
				('真断了','真弥子'),
				('真聞了','真弥子'),
				('真新了','真弥子'),
				('真綿了','真弥子'),
				('真絢了','真弥子'),

				('真紀十','真弥子'),
				('真断十','真弥子'),
				('真聞十','真弥子'),
				('真新十','真弥子'),
				('真綿十','真弥子'),
				('真絢十','真弥子'),

				('真紀','真弥子'),
				('真断','真弥子'),
				('真聞','真弥子'),
				('真新','真弥子'),
				('真綿','真弥子'),
				('真絢','真弥子'),

				('法築','法条'),
				('折堂','御堂'),
				('三階堂','二階堂'),
				('三隊堂','二階堂'),
				('三隊営','二階堂'),
				('三障堂','二階堂'),
				('三障営','二階堂'),
				('三陽堂','二階堂'),
				('三陽営','二階堂'),
				('二隊堂','二階堂'),
				('二隊営','二階堂'),
				('二障堂','二階堂'),
				('二障営','二階堂'),
				('二陽営','二階堂'),
				('二陽堂','二階堂'),
				('小次帥','小次郎'),
				('小光郎','小次郎'),
				('小光序','小次郎'),
				('小光雇','小次郎'),
				('Eh次朗','【小次郎'),
				('新生','弥生'),
				('紀生','弥生'),
				('交生','弥生'),
				('訂生','弥生'),
				('閑生','弥生'),
				('強生','弥生'),
				('絢生','弥生'),
				('引生','弥生'),
				('【乳】','【孔】'),
				('【了乳】','【孔】'),
				('【礼】','【孔】'),
				('【攻】','【孔】'),
				('【防】','【孔】'),
				('【基】','【孔】'),
			)
			for (s, t) in replace_list:
				text = text.replace (s, t)
			self.add_text( text )
	
	def add_brakets(self):
		""" 段落の挿入(括弧のみ) """
		self.add_text('【】')
		
	def add_command(self, s):
		""" 段落の挿入(コマンド) """
		if len(s)>1:
			com = ''
			for c in s[1:]:
				com += c +'>'
			self.add_text(com[:-1])
				
	def add_text(self, _text):
		""" 段落の挿入 """
		p = self.doc.add_paragraph(_text, style='Body Text')
		p.paragraph_format.line_spacing = Pt(10)
		p.style.font.size = Pt(10)
	
	def run(self):
		""" 実行 """
		filename = os.path.basename( self.dir ) + '.docx'
		print(filename)
		
		# シーン毎に段落を作成する
		scene = os.path.basename( self.dir ).split('-')[1]
		self.add_header(scene)
		
		# 
		self.ss_pre = None
		
		for g in sorted(glob.glob( self.dir + '/*')):
			# シーン内のディレクトリを検索
			s = os.path.basename(g).split('-')
			
			# コマンドの書き込み
			self.add_command(s)
			
			# 各画像の検索
			for f in sorted(glob.glob(g + '/*.png')):
				self.ss = ss_crop(f)
				
				# 画像の挿入
				self.add_img_main()
				
				# セリフ画像の挿入
				self.add_img_text()
				
				# セリフ用のカッコを挿入しておく
				#self.add_brakets()
				
				# OCRする
				self.add_ocr()
				
				# 1つ前の画像を保持
				self.ss_pre = self.ss
		
		# ファイルを保存する
		self.doc.save(filename)
		
if __name__ == '__main__':
	ss_doc('./01-本部').run()
	