from .params import *
scene_dir = [
	'81-セリス軍',
	'81-セリス軍2',
	'81-セリス軍3',
	'87-ダナン軍',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]

files = [
]

title = 'Phase3 : vsダナン軍' 

persons = {
	'セリス'  : '00',
	'ダナン'  : '10',
}

organization = {
	'左' : {
		'名' : 'セリス軍(10)',
		'指揮官' : persons['セリス'],
		'編成' : [
			['', [1,2,3]],
			['', [4,5,6]],
			['', [7,8,9]],
		],
	},
	'右' : {
		'名' : 'ダナン軍(1)',
		'指揮官' : persons['ダナン'],
		'編成' : [
		
		],
	},
}
