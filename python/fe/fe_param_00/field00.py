from .params import *
scene_dir = '00-フィールドマップ/'
scene_dir2 = '00-フィールドマップ追加画像/'

dirs = [
	base_dir + chaper_dir + scene_dir,
	base_dir + chaper_dir + scene_dir2,
]

out_file = '序章-聖戦士誕生-フィールド.png'

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
		
		[4, (47,6,9,1,11,2)],
		[29, (51,4,3,0,13,12)],
		[30, (30,20,4,3,9,8)],
		
		[36, (23,3,0,3,13,12)],
		[41, (32,7,4,0,13,12)],
		[44, (41,9,0,0,9,12)],
		
		[34, (5,3,0,3,13,12)],
		[48, (2,10,0,0,4,5)],
		[49, (23,7,5,0,9,12)],
		[50, (18,16,0,1,9,12)],
		[52, (34,23,7,5,13,10)],
		[52, (29,26,2,8,9,12)],
		[53, (41,18,0,0,9,12)],
		
	]
