base_dir = '/storage/43E3-332A/others/test/work/ROM/SNES/ファイアーエムブレム 聖戦の系譜 (J)/'
#base_dir = './test/'
chaper_dir = '00-序章-聖騎士誕生/'
scene_dir1 = '82-ユングヴィ軍/'
scene_dir2 = '91-エバンズ軍(ガンドルフ)/'
scene_dir3 = '92-エバンズ軍(デマジオ)'

title = 'Phase1 : ミデェールvsガンドルフ' 

dirs = [
	base_dir + chaper_dir + scene_dir1,
	base_dir + chaper_dir + scene_dir2,
	base_dir + chaper_dir + scene_dir3,
]

persons = {
	'ミデェール' : '00',
	'ガンドルフ'  : '01',
}

organization = {
	'左' : {
		'名' : 'ユングヴィ軍(1)',
		'指揮官' : persons['ミデェール'],
		'編成' : [],
	},
	'右' : {
		'名' : 'ガンドルフ軍(31)',
		'指揮官' : persons['ガンドルフ'],
		'編成' : [
			['デマジオ', [2]],
			['バーバリアン(21)', [3,4,5,6,7,8,11,12]],
			['', [13,14,15,16,17,18,19,23]],
			['', [24,26,27,30,31]],
			['ハンター(3)', [9,10,28]],
			['マウンテンシーフ(5)', [20,21,22,25,29]],
		],
	},
}
