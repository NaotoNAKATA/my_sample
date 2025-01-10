from .params import *
scene_dir = [
	'81-シグルド軍',
	#'82-ノディオン軍',
	#'83-ハイライン軍',
	#'83-ハイライン軍2',
	#'83-ハイライン軍3',
	#'84-アンフォニー軍',
	'85-アンフォニー軍',
	#'86-傭兵軍',
	'87-シグルド軍',
	#'88-シグルド軍',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]

files = [
]

title = 'Phase2 : vsアンフォニー軍' 

persons = {
	'シグルド'  : '00',
	'マクベス'  : '17',
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
			['アンフォニー軍出撃後に加入', [35,36]],
		],
	},
	'右' : {
		'名' : 'マクベス軍(18)',
		'指揮官' : persons['マクベス'],
		'編成' : [
			['アクスアーマー(3)', [18,19,20]],
			['ソードアーマー(4)', [21,22,23,24]],
			['ボウアーマー(3)', [25,26,27]],
			['デュークナイト(1)', [28]],
			['ランスナイト(2)', [29,30]],
			['マウンテンシーフ(4)', [31,32,33,34]],
		],
	},
}