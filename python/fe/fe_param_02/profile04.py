from .params import *
scene_dir = [
	'81-シグルド軍',
	#'82-ノディオン軍',
	#'83-ハイライン軍',
	#'83-ハイライン軍2',
	#'83-ハイライン軍3',
	'84-アンフォニー軍',
	#'85-アンフォニー軍',
	#'86-傭兵軍',
	#'87-シグルド軍',
	#'88-シグルド軍',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]

files = [
]

title = 'Phase1 : vsアンフォニー軍(中立)' 

persons = {
	'シグルド'  : '00',
	'隊長'  : '21',
}

organization = {
	'左' : {
		'名' : 'シグルド軍',
		'指揮官' : persons['シグルド'],
		'編成' : [
			['', []],
		],
	},
	'右' : {
		'名' : 'アンフォニー軍(中立)(7)',
		'指揮官' : persons['隊長'],
		'編成' : [
			['ランスナイト(2)', [22,23]],
			['マウンテンシーフ(4)', [17,18,19,20]],
		],
	},
}
