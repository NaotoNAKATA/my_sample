from .params import *
scene_dir = [
	'26-ヴェルダン制圧/',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]

files = [
]

title = 'Phase3 : ヴェルダン城制圧'

a = 1
fld = 0.5
bat = 0.75

scene = [
	['001', a, [
	'シグルド様、王宮にバトゥ王らしき方が',
	'倒れていたと報告がありました',
	
	'酷いお怪我で、',
	'もはや手の施しようがないそうです',
	]],
	['021', a, [
	'',
	]],
	['022', a, [
	'バトゥ王・・・いったいどうされたのです！',
	'どうかお気を確かに',
	]],
	['031', a, [
	'うう・・・シグルド殿か',
	'・・・この度のこと、すまぬ・・・',
	'わしはサンディマに騙されていた',
	
	'あやつは息子達を取り込み、',
	'わしを欺いて国を乗っ取ろうとしたのだ・・・',
	'',
	]],
	['042', a, [
	'バトゥ王、わかっています',
	'無理をされると、お体にさわります',
	'もうお休み下さい',
	]],
	['051', a, [
	'いや、わしはもう駄目だ',
	'だが死ぬ前にこれだけは話しておかねばならぬ',
	
	'この世界に起こりつつある邪悪な出来事は、',
	'全て暗黒教団の意思によるものなのだ',
	
	'奴等は世界のことわりを破壊して',
	'暗黒神ロプトウスの復活を早めようとしておる・・・',
	
	'サンディマはそのために、',
	'わしらをそそのかして',
	'グランベルに攻め込ませたのじゃ',
	
	'奴等は世界中でうごめいておる・・・',
	'シグルド殿・・・惑わされてはならぬぞ',
	
	'どうか我が無念を晴らし、',
	'この国の人々を守って下され・・・',
	'・・・た、たのんだぞシグルドどの・・・',
	]],
	['112', a, [
	'あっ、バトゥ王・・・',
	]],
	['111', a, [
	'',
	]],
	['112', a, [
	'・・・なんと哀れな・・・',
	'しかし、暗黒教団とはいったい・・・',
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
