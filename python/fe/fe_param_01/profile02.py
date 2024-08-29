base_dir = '/storage/43E3-332A/others/test/work/ROM/SNES/ファイアーエムブレム 聖戦の系譜 (J)/'
#base_dir = './test/'
chaper_dir = '01-第一章-精霊の森の少女/'
#scene_dir1 = '81-シグルド軍/'
#scene_dir2 = '82-ジェノア軍/'
#scene_dir3 = '84-ヴェルダン軍/'
#scene_dir4 = '83-マーファ軍/'
scene_dir5 = '87-ノディオン軍/'
scene_dir6 = '86-ハイライン軍/'

title = 'Phase2 : ノディオン軍vsハイライン軍' 

dirs = [
	#base_dir + chaper_dir + scene_dir1,
	#base_dir + chaper_dir + scene_dir2,
	#base_dir + chaper_dir + scene_dir3,
	#base_dir + chaper_dir + scene_dir4,
	base_dir + chaper_dir + scene_dir5,
	base_dir + chaper_dir + scene_dir6,
]

persons = {
	'ノディオン'  : '00',
	'ハイライン'  : '10',
}

organization = {
	'左' : {
		'名' : 'エルトシャン軍(10)',
		'指揮官' : persons['ノディオン'],
		'編成' : [
			['ソシアルナイト(9)', [1,2,3,4,5,6,7,8]],
			['', [9]],
		],
		'倍率' : 0.375,
	},
	'右' : {
		'名' : 'エリオット軍(12)',
		'指揮官' : persons['ハイライン'],
		'編成' : [
			['ランスナイト(11)', [11,12,13,14,15,16,17,18]],
			['', [19,20,21]],
		],
	},
}
