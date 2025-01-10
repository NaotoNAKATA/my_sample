from .params import *
scene_dir = [
	'36-イーヴ-ラケシス',
	'37-アグスティ制圧',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]

files = [
]

title = 'Phase4 : アグスティ制圧'

a = 1
fld = 0.5
bat = 0.75

scene = [
	['', a, [
	'三兄弟生還',
	]],
	['001', a, [
	'ラケシス様',
	'私達はノディオンに帰りますが、',
	'姫様にお渡ししたいものがあります',
	
	'これはナイトリングといって、',
	'騎士以外の者でも再移動ができるようになる魔法の腕輪',
	
	'きっと姫様のお役に立つでしょう',
	'では、どうかお元気で',
	
	'',
	'(ナイトリング)',
	]],
	
	['', a, [
	'アグスティ制圧',
	]],
	['041', a, [
	'シグルド様',
	'シャガール王は重傷ですが、まだ生きておられるようです',
	'王宮の司祭が手当をしているとのことです',
	]],
	['042', a, [
	'戦場からシャガール王を救出した者がいたと聞いたが、',
	'いったい誰なのだろう',
	]],
	['051', a, [
	'俺だ、シグルド',
	'・・・俺が王を助け出した',
	'アグスティの王族は、もはや彼しかいない',
	
	'たとえどんな人間だろうと、',
	'俺にとっては主君であることには違いない',
	'死なすわけにはいかぬ',
	]],
	['062', a, [
	'エルトシャン！？',
	'無事だったのか！',
	
	'よかった',
	'捕らえられたと聞いたから探していたんだ',
	]],
	['081', a, [
	'ああ、何とかな',
	'',
	'しかしシグルド、これはどういう事だ？',
	
	'王都アグスティは貴様の軍によって制圧され、',
	
	'聞くところによると、',
	'各地の城はグランベルから役人が派遣されて、',
	'まるで属国扱いだという',
	
	'アグストリアは、俺の知らぬ間に',
	'グランベルによって占領されたのか？',
	
	'シグルド、',
	'返答次第ではお前とて容赦はしないぞ！',
	]],
	['122', a, [
	'すまない、エルトシャン',
	'その事については、私も腑に落ちないんだ',
	
	'だが国王は、君を除くアグストリアの諸公が、',
	'我が国に敵対した事は事実だから、',
	
	'治安維持のためにも',
	'しばらくこの地にとどまるよう私に命じられた',
	
	'エルトシャン、',
	'頼む、一年だけ待ってくれ',
	
	'一年あれば平和も回復され、',
	'アグストリアとの関係も修復されるだろう',
	
	'そうすれば我らは国に戻る',
	'国王も私にそう約束された',
	]],
	
	['改ページ', -1, ['']],
	
	['181', a, [
	'そうか・・・貴様がそこまで言うなら信用するしかなかろう',
	'わかった・・・一年だな',
	
	'よし、それまでは北のマディノ城で、',
	'シャガール王をお守りしよう',
	
	'俺のクロスナイツも、',
	'ちょうどシルベールの砦に駐留しているし、',
	
	'その気になれば、',
	'グランベル軍など何時でも撃破できる',
	
	'もし貴様が約束を破れば、',
	'その時は俺も本気で戦うぞ！',
	'わかっているだろうな、シグルド！',
	]],
	['222', a, [
	'無論だ、私は君を裏切りはしない',
	'信用してくれ、エルトシャン',
	]],
	
	# 0 フィールド
	# 人物1,2(屋内)
	# 人物3,4(屋外)
	# 人物5(戦闘)
	# 6 戦闘
	# 7 戦闘(屋外)
	#['003', a, [
	#'',
	#]],
	#['060', fld,[]],
	#['改ページ', -1, ['']],
	#['016', bat,[]],
]