from .params import *
scene_dir = '00-フィールドマップ/'
scene_dir2 = '00-フィールドマップ追加画像/'

dirs = [
	base_dir + chaper_dir + scene_dir,
	base_dir + chaper_dir + scene_dir2,
]

out_file = '序章-聖戦士誕生-フィールド-Phase2(vsデマジオ).png'

TEST_RUN_FIRST = False
TEST_RUN = False
RUN = True

comp = [
		[0, (0,0)],
		[1, (0,7)],
		[2, (0,14)],
		[3, (0,18)],
		
		[4, (9,0)],
		[5, (9,7)],
		[6, (9,14)],
		[7, (9,18)],
		
		[8, (18,0)],
		[9, (18,7)],
		[10, (18,14)],
		[11, (18,18)],
		
		[12, (27,0)],
		[13, (27,7)],
		[14, (27,14)],
		[15, (27,18)],
		
		[16, (36,0)],
		[17, (36,7)],
		[18, (36,14)],
		[19, (36,18)],
		
		[20, (45,0)],
		[21, (45,7)],
		[22, (45,14)],
		[23, (45,18)],
		
		[24, (48,0)],
		[25, (48,7)],
		[26, (48,14)],
		[27, (48,18)],
		[28, (53,23,5,5,13,12)],
		
		[59, (30,22,6,7,9,11)]
	]
