from .params import *
scene_dir = [
	'92-シビリアン',
	'93-市民追討',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]

files = [
]

title = 'Phase2 : 市民逃亡' 

persons = {
	'シビリアン'  : '00',
	'追討軍'  : '06',
}

organization = {
	'左' : {
		'名' : 'シビリアン(6)',
		'指揮官' : persons['シビリアン'],
		'編成' : [
			['シビリアン(6)', [1,2,3,4]],
			['', [5]],
		],
	},
	'右' : {
		'名' : '追討軍(8)',
		'指揮官' : persons['追討軍'],
		'編成' : [
			['アクスファイター(8)', [6,7,8,9,10,11,12,13]],
		],
	},
}
