from .params import *
scene_dir = [
	#'00-プロローグ/',
	'00-プロローグ追加画像/',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]
#files = []

out_file = '10-第十章-光と闇と-プロローグ.png'

TEST_RUN_FIRST = False
TEST_RUN = True
RUN = False

comp = [
		[0, (0,0)],
		[1, (30,30)],
		[2, (60,35)],
		[3, (67,35)],
		[4, (38,51)],
		[5, (0,51)],
		[6, (-32,51)],
		[7, (-35,51)],
		[8, (-29,51)],
		[9, (-23,51)],
		[10, (-19,51)],
	]

