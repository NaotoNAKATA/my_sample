base_dir = '/storage/43E3-332A/others/test/work/ROM/SNES/ファイアーエムブレム 聖戦の系譜 (J)/'
#base_dir = './test/'
chaper_dir = '01-第一章-精霊の森の少女/'
ivent_dir = '19-vsガンドルフ/'

title = 'Phase3 : vsガンドルフ'

dirs = [
	base_dir + chaper_dir + ivent_dir,
]

#files = [
#]

a = 1
fld = 0.5
bat = 0.75

scene = [
	['006', bat,[]],
	['005', a, [
	'ちくしょう、',
	'女には逃げられるし',
	'城は攻められるし',
	
	'俺はなんて不幸なんだ！',
	]],
	['026', bat,[]],
	['036', bat,[]],
	['046', bat,[]],
	['045', a, [
	'・・・な・・・なんてことだ',
	'・・・グフッ',
	]],
	
	# 0 フィールド
	# 人物1,2(屋内)
	# 人物3,4(屋外)
	# 人物5(戦闘)
	# 6 戦闘(屋内)
	# 7 戦闘(屋外)
	#['003', a, [
	#'',
	#]],
	#['060', fld,[]],
	#['改ページ', -1, ['']],
	#['016', bat,[]],
]
