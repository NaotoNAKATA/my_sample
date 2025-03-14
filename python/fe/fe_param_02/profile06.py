from .params import *
scene_dir = [
	'81-シグルド軍',
	#'82-ノディオン軍',
	#'83-ハイライン軍',
	#'83-ハイライン軍2',
	#'83-ハイライン軍3',
	#'84-アンフォニー軍',
	#'85-アンフォニー軍',
	'86-傭兵軍',
	'87-シグルド軍',
	'88-シグルド軍',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]

files = [
]

title = 'Phase2 : vs傭兵軍' 

persons = {
	'シグルド'  : '00',
	'ヴォルツ'  : '17',
}

organization = {
	'左' : {
		'名' : 'シグルド軍',
		'指揮官' : persons['シグルド'],
		'編成' : [
			['', [1,2,3,4]],
			['', [5,6,7,8]],
			['', [9,10,11,12]],
			['', [13,14,15,16]],
			['', [30,31]],
			['10000Gで加入', [32]],
		],
	},
	'右' : {
		'名' : 'ヴォルツ軍(13)',
		'指揮官' : persons['ヴォルツ'],
		'編成' : [
			['ベオウルフ', [18]],
			['フリーナイト(11)', [19,20,21,22,23,24,25,26]],
			['', [27,28,29]],
		],
	},
}
