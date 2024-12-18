from .params import *
scene_dir = [
	'01-エバンス出撃/',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]

files = [
]

title = 'Phase1 : エバンス出撃'

a = 1
fld = 0.5
bat = 0.75

scene = [
	['000', fld,[]],
	['010', fld,[]],
	['020', fld,[]],
	['033', a, [
	'ごくろうだな、',
	'国境の守りは頼んだぞ',
	]],
	['034', a, [
	'はっ、エルトシャン様',
	]],
	['040', fld,[]],
	['050', fld,[]],
	['060', fld,[]],
	['071', a, [
	'シグルド、久しぶりだな',
	'エバンスを制圧するとは、どういうわけだ？',
	'ヴェルダンに攻め込もうとでもいうのか？',
	]],
	['072', a, [
	'エルトシャン、よく来てくれた',
	'ユングヴィのエーディン公女が連れ去られた',
	'ヴェルダンがどうしても公女を返さないのなら、',
	'戦うより他に仕方ないのだ',
	]],
	['071', a, [
	'なるほど、そういうことか',
	'しかし、今エバンス城を空ければ、',
	'アグストリアの諸侯が',
	'いらぬ野心を起こしかねんな・・・',
	'わかった、お前の背後は僕が守ろう',
	]],
	['072', a, [
	'すまない、エルトシャン',
	'戦いが終わったら、また会おう',
	'昔のように、お前とワインでも',
	'酌み交わしたいものだ',
	]],
	['071', a, [
	'楽しみにしてるぞ、シグルド',
	'武運を祈っている！',
	]],
	
	['改ページ', -1, ['']],
	
	['140', fld,[]],
	['150', fld,[]],
	['161', a, [
	'アイラよ、わかっているだろうな',
	'俺が城を留守にする間、しっかり守れよ',
	
	'もし、おかしなマネをすれば',
	'ガキの命はないと思え',
	]],
	['181', a, [
	'アイラ、僕は大丈夫だ',
	'だからこんな奴等の',
	'いいなりになっちゃ駄目だよ！',
	]],
	['182', a, [
	'シャナン・・・',
	]],
	['192', a, [
	'キンボイス、約束は守る',
	'だからシャナンには手出しはするな',
	
	'だが、この戦いが終われば',
	'本当にこの子を返してくれるのだろうな',
	]],
	['211', a, [
	'ああ、心配するな、エバンスの城さえ',
	'取り戻せば返してやるよ',
	]],
	['212', a, [
	'わかった',
	'しかし、もし約束を破れば、ただではおかない',
	
	'地獄の底でも追いかけて',
	'お前の首をたたき落としてやる',
	'その事、忘れるな！',
	]],
	['231', a, [
	'おお、怖ええ！',
	'可愛い顔して恐ろしい事を言う女だぜ',
	
	'まあしかし、剣の腕は確かにすげぇからな',
	'敵にするつもりはねけよ、安心しな',
	]],
	['252', a, [
	'シャナン、待っててね',
	'少しの間だけ辛抱して',
	]],
	['261', a, [
	'アイラ、駄目だよ、行っちゃ駄目だ！',
	]],
	['270', fld,[]],
	['284', a, [
	'よしっ、てめぇら、出かけるぜ',
	'エバンスを取り戻すんだよ！',
	]],
	['290', fld,[]],
	
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
