from .params import *
scene_dir = [
	'01-シャガール反攻/',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]

files = [
]

title = 'Phase1 : シャガール反攻'

a = 1
fld = 0.5
bat = 0.75

scene = [
	['000', fld,[]],
	
	['012', a, [
		'軍の配備は終わったか',
		'ヤツらに気付かれてはいないだろうな',
		'よし、ならば手はず通りに進撃せよ',

		'アグスティを取り戻す最後のチャンスだぞ',

		'ヤツら、わしの国にのうのうといすわりおって',

		'・・・今にみておれよ',
		'吠え面をかかせてやるからな',

		'ジャコバン！',
		'剣士ジャコバンはいるか！！',
	]],
	['061', a, [
		'俺に用か・・・',
	]],
	['062', a, [
		'その腕、見せてもらう時がきた',
		'この城を守ってくれ',
	]],
	['071', a, [
		'承知した・・・つまらぬ仕事だが金の為だ',
		'このいかずちの剣の恐ろしさ',
		'・・・たっぷりとみせてやろう',
	]],
	['072', a, [
		'それは心強い、頼んだぞジャコバン',
	]],
	['081', a, [
		'',
	]],
	['082', a, [
		'あとはシルベールにいるエルトシャンか',
		'・・・奴め、どう動くか・・・',
	]],
	
	['090', fld,[]],
	
	['101', a, [
		'エルトシャン様、大変です',
		'マディノ城が兵をあげました！',
	]],
	['102', a, [
		'なに、シャガール陛下が！？',
		'くそっ・・・なんと早まったことを！',
		'王都に帰れる日も近いというのに・・・',
		
		'くっ・・・俺はシグルドとは戦うわけにはいかぬ',
		'いったいどうすれば・・・',
	]],
	
	['120', fld,[]],
	
	['131', a, [
		'おかしら、南の方で戦が始まるようですぜ',
		'こりゃあ、おもしろくなってきた',
		
		'このスキに俺達は村をいただきましょう',

		'今までは、アグストリアの軍隊がいて、',
		'手も足も出せなかったが、今ならちょろいもんです',
	]],
	['152', a, [
		'お黙り、ドバール！',
		'こそ泥のまねなんかしたら、あたしが承知しないよ！',
		
		'あたしは、そんなケチな仕事はしない信条なんだ',

		'義賊でならしたオーガヒルの海賊の名が泣くよ！',
	]],
	
	['', a, [
		'',
	]],

	['181', a, [
		'ちくしょう、せっかくのお宝を、',
		'指をくわえて見てろってのか！',
		'おかしらはあまいぜ！',
	]],
	['182', a, [
		'まあ、落ちつけ、ドバール',
		'俺に考えがある',

		'あの女はな、',
		'死んだおかしらのホントの娘じゃねぇんだ',

		'ガキのころに拾われて、',
		'この島でおかしらに育てられたんだよ',

		'ヤツはそれも知らずに後を継いだつもりでいるが、',
		'なに、気にするこたぁない',
		
		'俺達だけで、お宝をいただこうぜ',
	]],

	#['230', fld,[]],
	['240', fld,[]],

	['251', a, [
		'シグルド様！　大変です！！',
		'シャガール王の軍がこの城を包囲しています',
	]],
	['252', a, [
		'なに！　ばかな・・・',
		'もうすぐ我々も国に帰るというのに',
		'なぜ戦う必要があるのだ',
		'',
		
		'エルトシャンはいったい・・・',
	]],
	['271', a, [
		'そのうえ、混乱に乗じて',
		'オーガヒルの海賊まで動き出しました',
	]],
	['272', a, [
		'そうか・・・やむをえない',
		'出陣しよう',
	]],
	['281', a, [
		'あなた・・・また戦いなのですか',
	]],
	['282', a, [
		'うむ、ディアドラ',
		'すまないが、今度ばかりは君をつれて行けない',
		
		'生まれたばかりのセリスを、',
		'おいてはいけないからね',
	]],
	['301', a, [
		'はい・・・',
	]],
	['302', a, [
		'そんな不安そうな顔をするな',
		'ぼくはすぐに戻る、約束するよ',

		'そうだ、シャナン、おまえに頼む',
		'ディアドラとセリスを守ってやってくれ',
	]],
	['321', a, [
		'うん！　大丈夫だよ',
		'ぼくがディアドラを守ってあげるから',
		'シグルドは安心して行っていいよ',
	]],
	['322', a, [
		'はは、シャナンはいつも元気がいいな',
	]],
	['331', a, [
		'',
	]],
	['332', a, [
		'ディアドラ、これでおまえも少しは気がまぎれるだろう',
		
		'心配するな',
		'これが永久の別れじゃないだろう',
	]],
	['351', a, [
		'シグルド様・・・・・',
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
