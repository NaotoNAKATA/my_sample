from .params import *
scene_dir = [
	'26-エバンズ城制圧/',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]
#files = []

title = 'Phase2 : エバンズ城制圧'

a = 1
fld = 0.5
bat = 0.75

scene = [
	['001', a, [
	'シグルド様、',
	'城内くまなく探したのですが',
	'エーディン様の姿は見当たりません',
	]],
	['002', a, [
	'なにっ・・・エーディンは一体どこに・・・',
	]],
	['001', a, [
	'おそらく城が落ちる前に',
	'ヴェルダンに連れ去られたのでしょう',
	'・・・ご無事だと良いのですが',
	]],
	['002', a, [
	'くっ・・・許せない・・・',
	'奴らがエーディンを返さない限り',
	'どこまでも追いかけるぞ',
	]],
	['020', fld,[]],
	['031', a, [
	'シグルド様',
	'バーハラから国王の使者が来られました',
	]],
	['041', a, [
	'シグルド殿',
	'この度の戦い見事でありました',
	'国王もいたく喜ばれ',
	'そなたに王国聖騎士の称号を下された',
	]],
	['042', a, [
	'身に余る光栄、',
	'陛下へのさらなる忠誠を誓います',
	]],
	['041', a, [
	'それと、これは重要なことですが、',
	'城を敵に奪われてはなりません',
	'最後まで城が残っていれば',
	'あなた達は軍用金を得られますが',
	'敵によって破壊されるごとに',
	'その額は少なくなってしまいます',
	'今後の戦いにおいても',
	'どうかお気をつけ下さい',
	]],
	
]
