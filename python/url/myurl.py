# -*- coding: utf-8 -*-

import os
import time
import glob
import urllib.request

class myurl(object):
	"""ファイルダウンロード"""
	def __init__(self):
		"""初期化"""
		self.ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '\
				'AppleWebKit/537.36 (KHTML, like Gecko) '\
				'Chrome/116.0.0.0 Safari/537.36'
	
	def run(self, list_file):
		"""全体"""
		self.read(list_file)
		self.down_save()
		
	def read(self, list_file):
		"""リストファイルの読み込み"""
		self.down_lists = {}
		with open(list_file, 'r') as f:
			for row in f:
				row = row.strip()
				if row == '':
					pass
				elif row[0]=='#':
					continue
				elif row[0:4]=='http':
					self.down_lists[now_key].append(row)
				else:
					now_key = row
					if not now_key in self.down_lists.keys():
						self.down_lists[now_key] = []
		
	def download(self, url):
		"""ファイルダウンロード本体"""
		req = urllib.request.Request(url, headers={'User-Agent': self.ua})
		time.sleep(1)
		print(os.path.basename(url))
		web = urllib.request.urlopen(req)
		return web.read()
		
	def save(self, binary, dat):
		"""ファイルを保存"""
		[key, url] = dat
		file_path = os.path.join(key, os.path.basename(url))
		with open(file_path, 'wb') as fw:
			fw.write(binary)
	
	def down_save(self):
		"""リストに従ってダウンロードし保存"""
		for key, lists in self.down_lists.items():
			print(key)
			if not os.path.exists(key):
				os.mkdir(key)
			
			for url in lists:
				# バイト列を取得
				binary = self.download(url)
				
				# 保存する
				self.save(binary, [key, url])
	
class myurl_fu_img(myurl):
	"""ファイルダウンロード(連番)"""
	def save(self, binary, dat):
		"""ファイルを連番で保存"""
		[key, url] = dat
		
		# ファイルの拡張子の取得
		file_name, ext = os.path.splitext(os.path.basename(url))
		
		# 現在の保存ディレクトリにあるファイル数
		num = len(glob.glob(os.path.join(key, '*')))
		
		# 保存ファイル名の作成
		file_path = os.path.join(key, '{0:0>2}.{1}'.format(num, ext))
		
		# 保存
		with open(file_path, 'wb') as fw:
			fw.write(binary)

if __name__ == "__main__":
	#u = myurl()
	u = myurl_fu_img()
	u.run('list.txt')
	
