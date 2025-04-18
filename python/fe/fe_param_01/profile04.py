from .params import *
scene_dir = [
	'81-シグルド軍/',
	'88-ジャムカ軍/',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]

files = [
]

title = 'Phase3 : vsジャムカ' 

persons = {
	'シグルド'  : '00',
	'ジャムカ'  : '12',
}

organization = {
	'左' : {
		'名' : 'シグルド軍(12)',
		'指揮官' : persons['シグルド'],
		'編成' : [
			['', [1,2,8,9]],
			['', [3,4,7,5]],
			['', [6,10,11]],
		],
	},
	'右' : {
		'名' : 'ジャムカ軍(12)',
		'指揮官' : persons['ジャムカ'],
		'編成' : [
			['バーバリアン(11)', [13,14,15,16,17,18,19,20]],
			['', [21,22,23]],
			
		],
	},
}
