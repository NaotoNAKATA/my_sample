from .params import *
scene_dir = [
	'14-シレジア侵攻/',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]

files = [
]

title = 'Phase2 : シレジア侵攻'

a = 1
fld = 0.5
bat = 0.75

scene = [
	['', a, [
	'シレジア侵攻',
	]],
	
	['000', fld,[]],
	
	['011', a, [
	'トーヴェが落ちたか・・・ふっ、バカな弟め',
	'わしの捨てゴマになったとも知らず哀れな奴よ',
	
	'よし、パメラ、今がチャンスだ',
	'天馬騎士団を率いて出撃せよ',

	'シグルドが援軍として駆けつけるまでに、'
	'シレジア城を攻略するのだ',
	]],
	['032', a, [
	'はっ、おまかせを！',
	]],
	
	#['040', fld,[]],
	['050', fld,[]],
	['060', fld,[]],
	
	['071', a, [
	'ラーナ様、',
	'ザクソンからパメラ隊が出ました',
	'この城に向かっております！',
	]],
	['072', a, [
	'え！？　それは本当ですか！',
	'・・・ダッカー公が、ついに本性をあらわしたのですね',
	]],
	['081', a, [
	'ご安心ください、',
	'パメラ隊は、わが隊がおさえます'
	]],
	['082', a, [
	'マーニャ、大丈夫ですか',
	'パメラは恐ろしい天馬騎士だと聞きいていますが',
	]],
	['091', a, [
	'はい、確かに侮れぬ力を持っています',

	'しかし、私とてシレジア四天馬騎士の一人',
	'決して無様な戦いはしません',
	]],
	['102', a, [
	'ごめんなさいね、マーニャ',
	'あなたの気持ちを知りながら・・・',
	'私は・・・',
	]],
	['111', a, [
	'私はこういう生き方しかできないのです',
	'・・・・・ラーナ様、',
	'どうか気になさらないで下さい',
	
 	'では、行ってまいります',
 	'',
	'マーニャ隊、出撃せよ！',
	]],
	
	#['130', fld,[]],
	['140', fld,[]],
	
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
