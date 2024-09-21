base_dir = '/storage/43E3-332A/others/test/work/ROM/SNES/ファイアーエムブレム 聖戦の系譜 (J)/'
#base_dir = './test/'
chaper_dir = '01-第一章-精霊の森の少女/'
scene_dir1 = '81-シグルド軍/'
#scene_dir2 = '82-ジェノア軍/'
#scene_dir3 = '84-ヴェルダン軍/'
#scene_dir4 = '83-マーファ軍/'
#scene_dir5 = '85-ノディオン軍/'
scene_dir6 = '88-ジャムカ軍/'
#scene_dir7 = '89-サンディマ軍/'

title = 'Phase4 : vsジャムカ' 

dirs = [
	base_dir + chaper_dir + scene_dir1,
	#base_dir + chaper_dir + scene_dir2,
	#base_dir + chaper_dir + scene_dir3,
	#base_dir + chaper_dir + scene_dir4,
	base_dir + chaper_dir + scene_dir6,
	#base_dir + chaper_dir + scene_dir7,
]

persons = {
	'シグルド'  : '00',
	'ジャムカ'  : '12',
}

organization = {
	'左' : {
		'名' : 'シグルド軍(12)',
		'指揮官' : persons['シグルド'],
		'編成' : [
			['', [1,2,8,9]],
			['', [3,4,7,5]],
			['', [6,10,11]],
		],
	},
	'右' : {
		'名' : 'ジャムカ軍(12)',
		'指揮官' : persons['ジャムカ'],
		'編成' : [
			['バーバリアン(11)', [13,14,15,16,17,18,19,20]],
			['', [21,22,23]],
			
		],
	},
}
