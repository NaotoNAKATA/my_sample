from .params import *
scene_dir = [
	'18-vsピサール',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]

files = [
]

title = 'Phase3 : vsピサール'

a = 1
fld = 0.5
bat = 0.75

scene = [
	['006', bat,[]],
	
	['005', a, [
	'グランベル軍がなんだ！'
	'オーガヒルの海賊の恐ろしさ',
	'たっぷり楽しませてやるぜ！',
	]],
	['016', bat,[]],
	['026', bat,[]],
	['035', a, [
	'くそ・・・',
	'オーガヒルの海賊が負けるはずが・・・',
	]],
	# 0 フィールド
	# 人物1,2(屋内)
	# 人物3,4(屋外)
	# 人物5(戦闘)
	# 6 戦闘
	#['003', a, [
	#'',
	#]],
	#['060', fld,[]],
	#['改ページ', -1, ['']],
	#['016', bat,[]],
]
