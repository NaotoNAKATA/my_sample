base_dir = '/storage/43E3-332A/others/test/work/ROM/SNES/ファイアーエムブレム 聖戦の系譜 (J)/'
#base_dir = './test/'
chaper_dir = '00-序章-聖騎士誕生/'
scene_dir1 = '81-シグルド軍'
scene_dir2 = '93-エバンズ軍(ゲラルド)/'

title = 'Phase3 : vsゲラルド' 

dirs = [
	base_dir + chaper_dir + scene_dir1,
	base_dir + chaper_dir + scene_dir2,
]

persons = {
	'シグルド'  : '00',
	'ゲラルド'  : '10',
}

organization = {
	'左' : {
		'名' : 'シグルド軍(10)',
		'指揮官' : persons['シグルド'],
		'編成' : [
			['', [1,2,3,4]],
			['', [5,6,7,8]],
			['', [9]],
		],
	},
	'右' : {
		'名' : 'ゲラルド軍(16)',
		'指揮官' : persons['ゲラルド'],
		'編成' : [
			['バーバリアン(10)', [16,17,18,19,20,21,22,23]],
			['', [24,25]],
			['ハンター(5)', [11,12,13,24,15]],
		],
	},
}
