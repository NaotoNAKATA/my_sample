base_dir = '/storage/43E3-332A/others/test/work/ROM/SNES/ファイアーエムブレム 聖戦の系譜 (J)/'
#base_dir = './test/'
chaper_dir = '01-第一章-精霊の森の少女/'
scene_dir1 = '81-シグルド軍/'
scene_dir2 = '82-ジェノア軍/'
scene_dir3 = '84-ヴェルダン軍/'
#scene_dir4 = '83-マーファ軍/'
#scene_dir5 = '85-ノディオン軍/'

title = 'Phase1 : vsキンボイス' 

dirs = [
	base_dir + chaper_dir + scene_dir1,
	base_dir + chaper_dir + scene_dir2,
	base_dir + chaper_dir + scene_dir3,
	#base_dir + chaper_dir + scene_dir4,
]

persons = {
	'シグルド'  : '00',
	'キンボイス'  : '12',
}

organization = {
	'左' : {
		'名' : 'シグルド軍(10)',
		'指揮官' : persons['シグルド'],
		'編成' : [
			['', [1,2,8,9]],
			['', [3,4,7]],
			['', [5,6]],
		],
	},
	'右' : {
		'名' : 'キンボイス軍(20)',
		'指揮官' : persons['キンボイス'],
		'編成' : [
			['ウォーリア(1)', [13]],
			['アクスファイター(6)', [14,15,16,17,18,19]],
			['バーバリアン(5)', [20,21,22,23,24]],
			['ハンター(4)', [25,26,27,28]],
			['アイラ', [29]],
			['マウンテンシーフ(2)', [30,31]],
		],
	},
}
