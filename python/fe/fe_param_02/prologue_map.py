from .params import *
scene_dir = [
	'00-プロローグ/',
	'00-プロローグ追加画像/',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]
#files = []

out_file = '第二章-アグストリアの動乱-プロローグ.png'

TEST_RUN_FIRST = False
TEST_RUN = False
RUN = True

comp = [
		[23, (0,0)],
		#[24, (00,26)],
		#[25, (0,48)],
		#[26, (0,64)],
		[15, (0,127)],
		#[12, (0,163)],
		#[11, (0,176)],
		
		[0, (-16,208)],
		[11, (16,176)],
		
	]

