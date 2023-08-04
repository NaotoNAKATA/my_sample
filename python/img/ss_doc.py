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
                                ('‥','・'),
				('-','・'),
                                ('・・・・・・・・・','・・・・・・'),
                                ('・・・・。','・・・。'),
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
				('つっ','っ'),
				('つて','って'),
				('つた','った'),
				('やゃ','ゃ'),
				('ゃや','ゃ'),
				('大立夫','大丈夫'),
				('女斉','女子寮'),
				('女喜','女子寮'),
                                ('ちやん','ちゃん'),
                                ('有ゃん','ちゃん'),
                                ('有やん','ちゃん'),
                                ('台ゃん','ちゃん'),
                                ('台やん','ちゃん'),
                                ('吉ゃん','ちゃん'),
                                ('吉やん','ちゃん'),
                                ('有ゃう','ちゃう'),
                                ('有やう','ちゃう'),
                                ('台ゃう','ちゃう'),
                                ('台やう','ちゃう'),
                                ('吉ゃう','ちゃう'),
                                ('吉やう','ちゃう'),
                                ('ふうん','ふぅん'),
                                ('ババ','パパ'),

				('真紀子','真弥子'),
				('真断子','真弥子'),
				('真聞子','真弥子'),
				('真新子','真弥子'),
				('真綿子','真弥子'),
				('真絢子','真弥子'),
				('真郊子','真弥子'),
				('真線子','真弥子'),
				('真引子','真弥子'),
				('真交子','真弥子'),
				('真閑子','真弥子'),
				('真導子','真弥子'),
				('真邊子','真弥子'),

				('真弥二','真弥子'),
				('真紀二','真弥子'),
				('真断二','真弥子'),
				('真聞二','真弥子'),
				('真新二','真弥子'),
				('真綿二','真弥子'),
				('真絢二','真弥子'),
				('真郊二','真弥子'),
				('真線二','真弥子'),
				('真引二','真弥子'),
				('真交二','真弥子'),
				('真閑二','真弥子'),
				('真導二','真弥子'),
				('真邊二','真弥子'),

				('真弥才','真弥子'),
				('真紀才','真弥子'),
				('真断才','真弥子'),
				('真聞才','真弥子'),
				('真新才','真弥子'),
				('真綿才','真弥子'),
				('真絢才','真弥子'),
				('真郊才','真弥子'),
				('真線才','真弥子'),
				('真引才','真弥子'),
				('真交才','真弥子'),
				('真閑才','真弥子'),
				('真導才','真弥子'),
				('真邊才','真弥子'),

				('真弥す','真弥子'),
				('真紀す','真弥子'),
				('真断す','真弥子'),
				('真聞す','真弥子'),
				('真新す','真弥子'),
				('真綿す','真弥子'),
				('真絢す','真弥子'),
				('真郊す','真弥子'),
				('真線す','真弥子'),
				('真引す','真弥子'),
				('真交す','真弥子'),
				('真閑す','真弥子'),
				('真導す','真弥子'),
				('真邊す','真弥子'),

				('真弥地','真弥子'),
				('真紀地','真弥子'),
				('真断地','真弥子'),
				('真聞地','真弥子'),
				('真新地','真弥子'),
				('真綿地','真弥子'),
				('真絢地','真弥子'),
				('真郊地','真弥子'),
				('真線地','真弥子'),
				('真引地','真弥子'),
				('真交地','真弥子'),
				('真閑地','真弥子'),
				('真導地','真弥子'),
				('真邊地','真弥子'),

				('真弥了','真弥子'),
				('真紀了','真弥子'),
				('真断了','真弥子'),
				('真聞了','真弥子'),
				('真新了','真弥子'),
				('真綿了','真弥子'),
				('真絢了','真弥子'),
				('真郊了','真弥子'),
				('真線了','真弥子'),
				('真引了','真弥子'),
				('真交了','真弥子'),
				('真閑了','真弥子'),
				('真導了','真弥子'),
				('真邊了','真弥子'),

				('真弥十','真弥子'),
				('真紀十','真弥子'),
				('真断十','真弥子'),
				('真聞十','真弥子'),
				('真新十','真弥子'),
				('真綿十','真弥子'),
				('真絢十','真弥子'),
				('真郊十','真弥子'),
				('真線十','真弥子'),
				('真引十','真弥子'),
				('真交十','真弥子'),
				('真閑十','真弥子'),
				('真導十','真弥子'),
				('真邊十','真弥子'),

				('真弥耳','真弥子'),
				('真紀耳','真弥子'),
				('真断耳','真弥子'),
				('真聞耳','真弥子'),
				('真新耳','真弥子'),
				('真綿耳','真弥子'),
				('真絢耳','真弥子'),
				('真郊耳','真弥子'),
				('真線耳','真弥子'),
				('真引耳','真弥子'),
				('真交耳','真弥子'),
				('真閑耳','真弥子'),
				('真導耳','真弥子'),
				('真邊耳','真弥子'),

				('真弥寺','真弥子'),
				('真紀寺','真弥子'),
				('真断寺','真弥子'),
				('真聞寺','真弥子'),
				('真新寺','真弥子'),
				('真綿寺','真弥子'),
				('真絢寺','真弥子'),
				('真郊寺','真弥子'),
				('真線寺','真弥子'),
				('真引寺','真弥子'),
				('真交寺','真弥子'),
				('真閑寺','真弥子'),
				('真導寺','真弥子'),
				('真邊寺','真弥子'),
				
				('真弥隔','真弥子'),
				('真紀隔','真弥子'),
				('真断隔','真弥子'),
				('真聞隔','真弥子'),
				('真新隔','真弥子'),
				('真綿隔','真弥子'),
				('真絢隔','真弥子'),
				('真郊隔','真弥子'),
				('真線隔','真弥子'),
				('真引隔','真弥子'),
				('真交隔','真弥子'),
				('真閑隔','真弥子'),
				('真導隔','真弥子'),
				('真邊隔','真弥子'),

				('真弥豆','真弥子'),
				('真紀豆','真弥子'),
				('真断豆','真弥子'),
				('真聞豆','真弥子'),
				('真新豆','真弥子'),
				('真綿豆','真弥子'),
				('真絢豆','真弥子'),
				('真郊豆','真弥子'),
				('真線豆','真弥子'),
				('真引豆','真弥子'),
				('真交豆','真弥子'),
				('真閑豆','真弥子'),
				('真導豆','真弥子'),
				('真邊豆','真弥子'),

				('真弥考','真弥子'),
				('真紀考','真弥子'),
				('真断考','真弥子'),
				('真聞考','真弥子'),
				('真新考','真弥子'),
				('真綿考','真弥子'),
				('真絢考','真弥子'),
				('真郊考','真弥子'),
				('真線考','真弥子'),
				('真引考','真弥子'),
				('真交考','真弥子'),
				('真閑考','真弥子'),
				('真導考','真弥子'),
				('真邊考','真弥子'),

				('真弥直','真弥子'),
				('真紀直','真弥子'),
				('真断直','真弥子'),
				('真聞直','真弥子'),
				('真新直','真弥子'),
				('真綿直','真弥子'),
				('真絢直','真弥子'),
				('真郊直','真弥子'),
				('真線直','真弥子'),
				('真引直','真弥子'),
				('真交直','真弥子'),
				('真閑直','真弥子'),
				('真導直','真弥子'),
				('真邊直','真弥子'),

				('真弥ゴ','真弥子'),
				('真紀ゴ','真弥子'),
				('真断ゴ','真弥子'),
				('真聞ゴ','真弥子'),
				('真新ゴ','真弥子'),
				('真綿ゴ','真弥子'),
				('真絢ゴ','真弥子'),
				('真郊ゴ','真弥子'),
				('真線ゴ','真弥子'),
				('真引ゴ','真弥子'),
				('真交ゴ','真弥子'),
				('真閑ゴ','真弥子'),
				('真導ゴ','真弥子'),
				('真邊ゴ','真弥子'),

				('真弥耶','真弥子'),
				('真紀耶','真弥子'),
				('真断耶','真弥子'),
				('真聞耶','真弥子'),
				('真新耶','真弥子'),
				('真綿耶','真弥子'),
				('真絢耶','真弥子'),
				('真郊耶','真弥子'),
				('真線耶','真弥子'),
				('真引耶','真弥子'),
				('真交耶','真弥子'),
				('真閑耶','真弥子'),
				('真導耶','真弥子'),
				('真邊耶','真弥子'),

				('真弥ず','真弥子'),
				('真紀ず','真弥子'),
				('真断ず','真弥子'),
				('真聞ず','真弥子'),
				('真新ず','真弥子'),
				('真綿ず','真弥子'),
				('真絢ず','真弥子'),
				('真郊ず','真弥子'),
				('真線ず','真弥子'),
				('真引ず','真弥子'),
				('真交ず','真弥子'),
				('真閑ず','真弥子'),
				('真導ず','真弥子'),
				('真邊ず','真弥子'),

				('真紀','真弥子'),
				('真断','真弥子'),
				('真聞','真弥子'),
				('真新','真弥子'),
				('真綿','真弥子'),
				('真絢','真弥子'),
				('真郊','真弥子'),
				('真線','真弥子'),
				('真引','真弥子'),
				('真交','真弥子'),
				('真閑','真弥子'),
				('真導','真弥子'),
				('真邊','真弥子'),

				('【真弥】','【真弥子】'),

				('法築','法条'),
				('法生','法条'),
				('法桑','法条'),

				('折堂','御堂'),
				('補堂','御堂'),
				('制堂','御堂'),
				('接堂','御堂'),

				('三階堂','二階堂'),
				('三隊堂','二階堂'),
				('三隊営','二階堂'),
				('三障堂','二階堂'),
				('三障営','二階堂'),
				('三陽堂','二階堂'),
				('三陽営','二階堂'),
				('二階営','二階堂'),
				('二隊堂','二階堂'),
				('二隊営','二階堂'),
				('二障堂','二階堂'),
				('二障営','二階堂'),
				('二陽営','二階堂'),
				('二陽堂','二階堂'),
				
				('小次朗','小次郎'),
				('小次帥','小次郎'),
				('小次序','小次郎'),
				('小次雇','小次郎'),
				('小次似','小次郎'),
				('小次部','小次郎'),
				('小次計','小次郎'),
				
				('小光郎','小次郎'),
				('小光朗','小次郎'),
				('小光帥','小次郎'),
				('小光序','小次郎'),
				('小光雇','小次郎'),
				('小光似','小次郎'),
				('小光部','小次郎'),
				('小光計','小次郎'),
				
				('Eh次郎','【小次郎'),
				('Eh次朗','【小次郎'),
				('Eh次帥','【小次郎'),
				('Eh次序','【小次郎'),
				('Eh次雇','【小次郎'),
				('Eh次似','【小次郎'),
				('Eh次部','【小次郎'),
				('Eh次計','【小次郎'),

				('Eh光郎','【小次郎'),
				('Eh光朗','【小次郎'),
				('Eh光帥','【小次郎'),
				('Eh光序','【小次郎'),
				('Eh光雇','【小次郎'),
				('Eh光似','【小次郎'),
				('Eh光部','【小次郎'),
				('Eh光計','【小次郎'),

                                ('h次郎','小次郎'),
                                ('h次朗','小次郎'),
                                ('h次帥','小次郎'),
                                ('h次序','小次郎'),
                                ('h次雇','小次郎'),
                                ('h次似','小次郎'),
                                ('h次部','小次郎'),
                                ('h次計','小次郎'),

                                ('h光郎','小次郎'),
                                ('h光朗','小次郎'),
                                ('h光帥','小次郎'),
                                ('h光序','小次郎'),
                                ('h光雇','小次郎'),
                                ('h光似','小次郎'),
                                ('h光部','小次郎'),
                                ('h光計','小次郎'),

				('【芋】','【茜】'),
				('【再】','【茜】'),
				('【繭】','【茜】'),
				
				('女のず】','女の子】'),
				('女のゴ】','女の子】'),
				('女のそ】','女の子】'),
				('女の】','女の子】'),
				
				('新生','弥生'),
				('紀生','弥生'),
				('交生','弥生'),
				('訂生','弥生'),
				('閑生','弥生'),
				('強生','弥生'),
				('絢生','弥生'),
				('引生','弥生'),
				('郊生','弥生'),
				('邊生','弥生'),
				('綿生','弥生'),
				('郊生','弥生'),

				('【乳】','【孔】'),
				('【了乳】','【孔】'),
				('【礼】','【孔】'),
				('【攻】','【孔】'),
				('【防】','【孔】'),
				('【基】','【孔】'),

				#('松乃','松乃'),
				('松妃','松乃'),
				('松狂','松乃'),
				('松肪','松乃'),
				('松考','松乃'),
				('松夕','松乃'),
				('松用','松乃'),

				('要乃','松乃'),
				('要妃','松乃'),
				('要狂','松乃'),
				('要肪','松乃'),
				('要考','松乃'),
				('要夕','松乃'),
				('要用','松乃'),

				('禄乃','松乃'),
				('禄妃','松乃'),
				('禄狂','松乃'),
				('禄肪','松乃'),
				('禄考','松乃'),
				('禄夕','松乃'),
				('禄用','松乃'),

				('和乃','松乃'),
				('和妃','松乃'),
				('和狂','松乃'),
				('和肪','松乃'),
				('和考','松乃'),
				('和夕','松乃'),
				('和用','松乃'),

				('栓乃','松乃'),
				('栓妃','松乃'),
				('栓狂','松乃'),
				('栓肪','松乃'),
				('栓考','松乃'),
				('栓夕','松乃'),
				('栓用','松乃'),

				('税乃','松乃'),
				('税妃','松乃'),
				('税狂','松乃'),
				('税肪','松乃'),
				('税考','松乃'),
				('税夕','松乃'),
				('税用','松乃'),

				('初乃','松乃'),
				('初妃','松乃'),
				('初狂','松乃'),
				('初肪','松乃'),
				('初考','松乃'),
				('初夕','松乃'),
				('初用','松乃'),

				('補乃','松乃'),
				('補妃','松乃'),
				('補狂','松乃'),
				('補肪','松乃'),
				('補考','松乃'),
				('補夕','松乃'),
				('補用','松乃'),

				('究乃','松乃'),
				('究妃','松乃'),
				('究狂','松乃'),
				('究肪','松乃'),
				('究考','松乃'),
				('究夕','松乃'),
				('究用','松乃'),

				('各乃','松乃'),
				('各妃','松乃'),
				('各狂','松乃'),
				('各肪','松乃'),
				('各考','松乃'),
				('各夕','松乃'),
				('各用','松乃'),

				('窟乃','松乃'),
				('窟妃','松乃'),
				('窟狂','松乃'),
				('窟肪','松乃'),
				('窟考','松乃'),
				('窟夕','松乃'),
				('窟用','松乃'),

				('柚乃','松乃'),
				('柚妃','松乃'),
				('柚狂','松乃'),
				('柚肪','松乃'),
				('柚考','松乃'),
				('柚夕','松乃'),
				('柚用','松乃'),

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
	
