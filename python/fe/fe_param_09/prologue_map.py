from .params import *
scene_dir = [
	#'00-プロローグ/',
	'00-プロローグ追加画像/',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]
#files = []

out_file = '09-第九章-誰がために-プロローグ.png'

TEST_RUN_FIRST = False
TEST_RUN = True
RUN = False

comp = [
		[0, (0,0)],
		[1, (24,24)],
		[2, (43,43)],
		[3, (69,69)],
		[4, (93,84)],
		[5, (116,84)],
		[6, (116,137)],
	
	]

