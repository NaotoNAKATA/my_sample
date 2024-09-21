base_dir = '/storage/43E3-332A/others/test/work/ROM/SNES/ファイアーエムブレム 聖戦の系譜 (J)/'
#base_dir = './test/'
chaper_dir = '01-第一章-精霊の森の少女/'
scene_dir1 = '81-シグルド軍/'
#scene_dir2 = '82-ジェノア軍/'
#scene_dir3 = '84-ヴェルダン軍/'
#scene_dir4 = '83-マーファ軍/'
#scene_dir5 = '85-ノディオン軍/'
scene_dir6 = '88-ジャムカ軍/'
scene_dir7 = '89-サンディマ軍/'

title = 'Phase5 : vsサンディマ' 

dirs = [
	base_dir + chaper_dir + scene_dir1,
	#base_dir + chaper_dir + scene_dir2,
	#base_dir + chaper_dir + scene_dir3,
	#base_dir + chaper_dir + scene_dir4,
	base_dir + chaper_dir + scene_dir6,
	base_dir + chaper_dir + scene_dir7,
]

persons = {
	'シグルド'  : '00',
	'サンディマ'  : '24',
}

organization = {
	'左' : {
		'名' : 'シグルド軍(13)',
		'指揮官' : persons['シグルド'],
		'編成' : [
			['', [1,2,8,9]],
			['', [3,4,7,5]],
			['', [6,10,11]],
			['(会話後加入)', [12]],
		],
	},
	'右' : {
		'名' : 'サンディマ軍(11)',
		'指揮官' : persons['サンディマ'],
		'編成' : [
			['アクスファイター(2)', [25,26]],
			['ハンター(8)', [27,28,29,30,31,32,33,34]],
		],
	},
}
