#base_dir = '/storage/43E3-332A/others/test/work/ROM/SNES/ファイアーエムブレム 聖戦の系譜 (J)/'
base_dir = './test/'
chaper_dir = '00-序章-聖騎士誕生/'
scene_dir = '00-プロローグ/'
scene_dir_add = '00-プロローグ追加画像/'

out_file = '序章-聖騎士誕生-プロローグ.png'

dirs = [
	base_dir + chaper_dir + scene_dir,
	base_dir + chaper_dir + scene_dir_add,
]

TEST_RUN_FIRST = False
TEST_RUN = False
RUN = True



comp = [
		[26, (0,0)],
		[1, (176,112)],
		[26, (0,0)],
		[40, (96, 176)],
		[28,(-16,208)],
		[18, (384, 0)],
		
		[41, (295, 9)],
		[42, (310, 0)],
		[43, (384, 0)],
		
		[45, (367, 17)],
		[46, (347, 37)],
		[47, (285, 99)],
		[48, (258, 112)],
		
		[49, (55, 0)],
		[51, (0, 26)],
		[53, (0, 77)],
	]
