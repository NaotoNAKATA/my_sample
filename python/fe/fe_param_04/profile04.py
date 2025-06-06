from .params import *
scene_dir = [
	#'81-シグルド軍',
	'88-マーニャ軍',
	#'86-ダッカー軍',
	'87-パメラ軍',
	#'89-バイゲリッター',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]

files = [
]

title = 'Phase2 : マーニャ軍vsパメラ軍' 

persons = {
	'マーニャ'  : '00',
	'パメラ'  : '12',
}

organization = {
	'左' : {
		'名' : 'マーニャ軍(12)',
		'指揮官' : persons['マーニャ'],
		'編成' : [
			['ペガサスナイト(11)', [1,2,3,4]],
			['', [5,6,7,8]],
			['', [9,10,11]],
		],
	},
	'右' : {
		'名' : 'パメラ軍(12)',
		'指揮官' : persons['パメラ'],
		'編成' : [
			['ペガサスナイト(12)', [13,14,15,16,17,18,19,20]],
			['', [21,22,23]],
		],
	},
}
