base_dir = '/storage/43E3-332A/others/test/work/ROM/SNES/ファイアーエムブレム 聖戦の系譜 (J)/'
#base_dir = './test/'
chaper_dir = '01-第一章-精霊の森の少女/'
scene_dir1 = '81-シグルド軍/'
#scene_dir2 = '82-ジェノア軍/'
#scene_dir3 = '84-ヴェルダン軍/'
scene_dir4 = '83-マーファ軍/'
#scene_dir5 = '85-ノディオン軍/'

title = 'Phase3 : vsガンドルフ' 

dirs = [
	base_dir + chaper_dir + scene_dir1,
	#base_dir + chaper_dir + scene_dir2,
	#base_dir + chaper_dir + scene_dir3,
	base_dir + chaper_dir + scene_dir4,
]

persons = {
	'シグルド'  : '00',
	'ガンドルフ'  : '12',
}

organization = {
	'左' : {
		'名' : 'シグルド軍(10)',
		'指揮官' : persons['シグルド'],
		'編成' : [
			['', [1,2,8,9]],
			['', [3,4,7]],
			['', [5,6]],
			['(2ターン目に加入)', [10,11]],
		],
	},
	'右' : {
		'名' : 'ガンドルフ軍(21)',
		'指揮官' : persons['ガンドルフ'],
		'編成' : [
			['アクスファイター(1)', [13]],
			['バーバリアン(16)', [14,15,16,17,18,19,20,21]],
			['', [22,23,24,25,26,27,28,29]],
			['ハンター(3)', [30,31,32]],
			
			
		],
	},
}
