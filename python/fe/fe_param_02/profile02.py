from .params import *
scene_dir = [
	'81-シグルド軍',
	#'82-ノディオン軍',
	#'83-ハイライン軍',
	'83-ハイライン軍2',
	#'83-ハイライン軍3',
	#'84-アンフォニー軍',
	#'85-アンフォニー軍',
	#'86-傭兵軍',
	#'87-シグルド軍',
	#'88-シグルド軍',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]

files = [
]

title = 'Phase1 : vsフィリップ' 

persons = {
	'シグルド'  : '00',
	'フィリップ'  : '17',
}

organization = {
	'左' : {
		'名' : 'シグルド軍(17)',
		'指揮官' : persons['シグルド'],
		'編成' : [
			['', [1,2,3,4]],
			['', [5,6,7,8]],
			['', [9,10,11,12]],
			['', [13,14]],
			['闘技場Lv7クリアで加入', [15]],
			['シグルドと会話で加入', [16]],
		],
	},
	'右' : {
		'名' : 'フィリップ軍(12)',
		'指揮官' : persons['フィリップ'],
		'編成' : [
			['プリースト(1)', [18]],
			['アクスアーマー(2)', [19,20]],
			['ソードアーマー(2)', [21,22]],
			['アーマー(4)', [23,24,25,26]],
			['ロングアーチャー(2)', [27,28]],
		],
	},
}
