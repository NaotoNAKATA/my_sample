# -*- coding: utf-8 -*-

from ss_doc import ss_doc

if __name__ == '__main__':
	
	root_dir = '/storage/43E3-332A/others/test/EVE/Dec.2/01-まりな編/'
	p_list = (
		#root_dir + '01-本部',
		#root_dir + '02-403号室',
		#root_dir + '03-本部',
		#root_dir + '04-403号室',
		#root_dir + '05-外国人学校',
		#root_dir + '06-本部',
		#root_dir + '07-403号室',
		
	)
	
	for p in p_list:
		ss_doc(p).run()

