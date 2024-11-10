from .params import *
scene_dir = [
	'00-プロローグ/',
	'00-プロローグ追加画像/',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]
#files = []

out_file = '第一章-精霊の森の少女-プロローグ.png'

TEST_RUN_FIRST = False
TEST_RUN = False
RUN = True

comp = [
		[1, (0,0)],
		[0, (112,-32)],
		
		[40, (80,32)],
		
		[32, (101,11)],
		
	]

