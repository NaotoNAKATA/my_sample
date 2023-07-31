# -*- coding: utf-8 -*-

from ss_doc import ss_doc

import os
import glob
if __name__ == '__main__':
	# テスト
	#root_dir = 'C:\Users\NAKATANAOTO\work\game\EVE_burst_error\Dec.2\01-まりな編\'
	#p_list = (
	#	#root_dir + '01-本部',
	#	#root_dir + '02-403号室',
	#	#root_dir + '03-本部',
	#	#root_dir + '04-403号室',
	#	#root_dir + '05-外国人学校',
	#	#root_dir + '06-本部',
	#	#root_dir + '07-403号室',
        #        #'01-外国人学校前',
        #        '12-ディレクタールーム',
	#)
	
	root_dir = './??-*'
	p_list = sorted(glob.glob(root_dir))
	for p in p_list:
		p0 = p.replace('.\\','')
		ss_doc(p0).run()

