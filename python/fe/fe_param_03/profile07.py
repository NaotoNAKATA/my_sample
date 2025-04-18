from .params import *
scene_dir = [
	'81-シグルド軍',
	#'82-マディノ軍',
	#'83-オーガヒル軍',
	#'84-エルトシャン軍',
	#'85-シャガール軍',
	#'86-パピヨン軍',
	'87-シグルド軍',
	#'88-ピサール軍',
	#'89-ドバール軍',
	'90-海賊',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]

files = [
]

title = 'Phase3 : vs海賊' 

persons = {
	'シグルド'  : '00',
	'海賊'  : '24',
}

organization = {
	'左' : {
		'名' : 'シグルド軍',
		'指揮官' : persons['シグルド'],
		'編成' : [
			['', [2,3,4,5]],
			['', [6,7,8,9]],
			['', [10,11,12,13]],
			['', [14,15,16,17]],
			['', [18,19,20]],
			['シルベール制圧後に加入', [21,22,23]],
		],
	},
	'右' : {
		'名' : '海賊軍(9)',
		'指揮官' : persons['海賊'],
		'編成' : [
			['パイレーツ(9)', [24,25,26,27,28,29,30,31,32]],
		],
	},
}
