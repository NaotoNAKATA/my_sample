# -*- coding: utf-8 -*-

import os
import time
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
		self.down_save(self.save)
		
	def run2(self, list_file):
		"""全体"""
		self.read(list_file)
		self.down_save(self.save2)
		
	def read(self, list_file):
		"""リストファイルの読み込み"""
		self.down_lists = {}
		with open(list_file, 'r') as f:
			for row in f:
				row = row.strip()
				if row == '':
					pass
				elif row[0:4]=='http':
					self.down_lists[now_key].append(row)
				else:
					now_key = row
					self.down_lists[now_key] = []
		
	def download(self, url):
		"""ファイルダウンロード本体"""
		req = urllib.request.Request(url, headers={'User-Agent': self.ua})
		time.sleep(1)
		web = urllib.request.urlopen(req)
		return web.read()
		
	def save(self, binary, dat):
		"""ファイルを保存"""
		[key, url] = dat
		file_path = os.path.join(key, os.path.basename(url))
		with open(file_path, 'wb') as fw:
			fw.write(binary)
		
	def save2(self, binary, dat):
		"""ファイルを連番で保存"""
		pass
	
	def down_save(self, save):
		"""リストに従ってダウンロードし保存"""
		for key, lists in self.down_lists.items():
			if not os.path.exists(key):
				os.mkdir(key)
			
			for url in lists:
				# バイト列を取得
				binary = self.download(url)
				
				# 保存する
				save(binary, [key, url])
	
if __name__ == "__main__":
	u = myurl()
	u.run('list.txt')
	