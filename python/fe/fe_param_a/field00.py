base_dir = '/storage/43E3-332A/others/test/work/ROM/SNES/ファイアーエムブレム 聖戦の系譜 (J)/'
#base_dir = './test/'
chaper_dir00 = '00-序章-聖騎士誕生/'
chaper_dir01 = '01-第一章-精霊の森の少女/'
chaper_dir02 = '02-第二章-アグストリアの動乱/'
chaper_dir03 = '03-第三章-獅子王エルトシャン/'
chaper_dir04 = '04-第四章-空に舞う/'

scene_file00 = '序章-聖戦士誕生-フィールド.png'
scene_file01 = '第一章-精霊の森の少女-フィールド.png'
scene_file02 = '第二章-アグストリアの動乱-フィールド.png'
scene_file03 = '第三章-獅子王エルトシャン-フィールド.png'
scene_file04 = '第四章-空に舞う-フィールド.png'


dirs = [
]

files = [
	base_dir + chaper_dir00 + scene_file00,
	base_dir + chaper_dir01 + scene_file01,
	base_dir + chaper_dir02 + scene_file02,
	base_dir + chaper_dir03 + scene_file03,
	base_dir + chaper_dir04 + scene_file04,
	
]

out_file = '全体フィールド.png'

TEST_RUN_FIRST = False
TEST_RUN = True
RUN = False

#super().__init__(fe_pil) これにする

comp = [
		[0, (0,0)],
		[1, (4-45,15-13)],
		[2, (45-56,15-61)],
		#[3, (52-35,8-61)],
		[3, (52-35,8-61-1)],
		
		# TBD
		[4, (90,0)],
	]
