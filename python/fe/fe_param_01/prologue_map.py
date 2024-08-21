base_dir = '/storage/43E3-332A/others/test/work/ROM/SNES/ファイアーエムブレム 聖戦の系譜 (J)/'
#base_dir = './test/'
chaper_dir = '01-第一章-精霊の森の少女/'
scene_dir = '00-プロローグ/'
scene_dir_add = '00-プロローグ追加画像/'

out_file = '第一章-精霊の森の少女-プロローグ.png'

dirs = [
	base_dir + chaper_dir + scene_dir,
	base_dir + chaper_dir + scene_dir_add,
]

TEST_RUN_FIRST = False
TEST_RUN = False
RUN = True

comp = [
		[1, (0,0)],
		[0, (112,-32)],
		
		[40, (80,32)],
		
		[32, (101,11)],
		
	]

