from .params import *
scene_dir = [
	'12-ユングヴィ城制圧/',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]
#files = []

title = 'Phase2 : ユングヴィ城制圧'

a = 1
fld = 0.5
bat = 0.75

scene = [
	['001', a, [
	'シグルド様、',
	'若い騎士が倒れています！',
	]],
	['012', a, [
	'ん・・・？',
	'あっ、君はミデェールじゃないか',
	'どうした、しっかりしろ！',
	]],
	['021', a, [
	'うう・・・あなたは・・・',
	'・・・シグルド様',
	]],
	['022', a, [
	'ミデェール、大丈夫か！？',
	'エーディンはどうしたんだ？',
	'',
	]],
	['021', a, [
	'わかりません、たぶんガンドルフに・・・',
	]],
	['022', a, [
	'そうか・・・心配するなミデェール',
	'エーディンは、私が取り返す',
	'君は安心して体を癒せ',
	]],
	['021', a, [
	'いえ、シグルド様、私も行きます',
	'エーディン様が気がかりで',
	'とても休んでなどおれません！',
	]],
]
