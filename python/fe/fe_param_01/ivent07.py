from .params import *
scene_dir = [
	'18-マーファ援軍/',
	'12-デュー-エーディン/',
	'13-シグルド-エーディン/',
	'14-ミデェール-エーディン/',
	'15-アゼル-エーディン/',
	'16-アイラ-キュアン/',
	'17-エーディン-エスリン/',
	'72-村解放/',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]

files = [
]

title = 'Phase3 : 会話イベント'

a = 1
fld = 0.5
bat = 0.75

scene = [
	['', a, [
	'マーファ軍の攻撃範囲内侵入',
	]],
	['004', a, [
	'おらおら、何をしてやがる！',
	'準備の出来たヤツからドンドン出撃するんだ！',
	'奴等をこの城に近づけてはならんぞ！！',
	]],
	
	['', a, [
	'会話：デュー→エーディン',
	]],
	['033', a, [
	'やあっ、エーディンさん',
	'いいものあげるよ',
	'ほら、こんな杖を手に入れたんだ',
	
	'おいらが持ってても仕方ないからね',
	]],
	['044', a, [
	'まあ、デュー',
	'これはワープの杖よ',
	'何処で手に入れたの？',
	]],
	['053', a, [
	'えっ・・・えーとね・・・',
	'そこらへんで拾ったんだよ！',
	
	'きっとエーディンさんのために',
	'神様が落としておいてくれたんだ',
	]],
	['064', a, [
	'まあ、デューったら・・・',
	'でもこれで皆さんの戦いも楽になるわ',
	'ありがとう、大事に使うわね',
	
	'(ワープの杖)',
	]],
	
	['', a, [
	'会話：シグルド→エーディン',
	]],
	['083', a, [
	'エーディン、無事だったのか',
	'よかった！',
	]],
	['084', a, [
	'シグルド様！',
	'助けに来てくださったのですね',
	
	'ごめんなさい',
	'シアルフィの方々まで危険な目にあわせてしまって・・・',
	]],
	['103', a, [
	'そんな事はいいんだ',
	'みんなも君が無事だと知れば、喜んでくれる',
	
	'もう何も心配はいらない',
	'君は国に帰るといい',
	]],
	['114', a, [
	'いえ、私はここに残ります',
	'戦争は多くの人達を傷つけます',
	
	'私は神に仕える者として',
	'人々を助けたいのです',
	]],
	['133', a, [
	'エーディン・・・',
	'君は騎士になるのが嫌で',
	'シスターになったという',
	
	'君が多くの人達から慕われるのは',
	'その優しさにあるのだろうな',
	'私も見習わねばと思う',
	]],
	['144', a, [
	'いいえ、シグルド様',
	
	'私がシスターになったのは',
	'失われた姉を取り戻すため、',
	'ただ、それだけです・・・',
	]],
	['163', a, [
	'ブリギットのことか・・・',
	'幼い時に行方不明になったと聞いたけど',
	
	'エーディンは彼女のために',
	'祈っているのか・・・',
	]],
	['174', a, [
	'はい、何としても姉に再会して',
	'この聖弓イチイバルを渡さねばなりません！',
	]],
	
	['', a, [
	'会話：ミデェール→エーディン',
	]],
	['183', a, [
	'姫様、ご無事だったのですね',
	'ああ・・・よかった・・・！',
	
	'申し訳ありません',
	'もっと私に力があれば、こんなことには',
	]],
	['194', a, [
	'ミデェール、あなたこそ',
	'元気な顔を見て安心しました',
	
	'もういいのよ、',
	'あなたのせいではないのですから',
	'私の為に、よく戦ってくれましたね',
	
	'ミデェール、',
	'これからもシグルド様の力になってあげてね',
	]],
	['223', a, [
	'はい、もちろんです',
	
	'ユングヴィ城とエーディン様を',
	'救っていただいたご恩を',
	'私は決して忘れません！',
	]],
	
	['', a, [
	'会話：アゼル→エーディン',
	]],
	['243', a, [
	'ああっ、エーディン様！',
	'ご無事だったのですね・・・',
	]],
	['244', a, [
	'まあ、アゼル公子！',
	'あなたまでユングヴィの為に',
	'戦ってくださったのね',
	]],
	['253', a, [
	'エーディン様が敵に連れ去られたと聞いて',
	'居ても立ってもいられず、',
	
	'駆けつけてしまいました',
	]],
	['264', a, [
	'でも、あなたのお兄様は',
	'ヴェルトマーのアルヴィス卿でしょう',
	'お許しがあったの？',
	]],
	['273', a, [
	'いえ、兄には無断で・・・',
	'きっと怒っているでしょう',
	]],
	['274', a, [
	'何故そんなムチャをしたの？',
	'アゼルは戦争は嫌いだったはずなのに・・・',
	]],
	['283', a, [
	'それは・・・',
	]],
	['284', a, [
	'え？',
	'・・・なあにアゼル？',
	]],
	['293', a, [
	'いえ・・・何でもありません・・・',
	]],
	
	['改ページ', -1, ['']],
	
	['', a, [
	'会話：アイラ→キュアン',
	]],
	['303', a, [
	'君がイザークのアイラ王女か',
	'シグルドから話は聞いた',
	'私はレンスターのキュアンだ',
	]],
	['304', a, [
	'・・・よろしく頼む',
	]],
	['313', a, [
	'ひとつ、君に聞きたいことがある',
	'どうしてイザークは、ダーナの街に攻め込んだのだ？',
	
	'あの街に手を出せば、',
	'グランベルの報復を受けることは',
	'わかっていたはずだ',
	
	'マナナン王ほどの方が',
	'そんな無謀な事をされるとは、信じ難い・・・',
	]],
	['334', a, [
	'キュアン殿は、我が父上をご存知なのか！？',
	]],
	['343', a, [
	'いや、私自身は知らないが、',
	'我が父がマナナン王を知っていて',
	'立派な方だと聞かされていた',
	
	'マリクル王子、あなたの兄上のことも',
	'とても優れた若者だと、父は何度も言っていた',
	]],
	['354', a, [
	'そうか・・・嬉しいことだな',
	
	'確かに父も兄も立派な武人だ',
	'無抵抗の街を襲うなど絶対に許さない',
	
	'ダーナの一件は、',
	'リボーの族長が勝手にやったことだ・・・',
	]],
	['383', a, [
	'何！？',
	'では何故、グランベルに弁明をしないのだ？',
	
	'マナナン王が真相を話されれば、',
	'クルト様はわかって下さるはずだ',
	]],
	['394', a, [
	'父上もそう考えられた・・・',
	
	'事実を知った父上は、リボーの族長を殺し、',
	'その首を持って',
	'グランベルの陣地へ詫びに行ったのだ',
	
	'',
	'だが・・・',
	]],
	['423', a, [
	'だが・・・？',
	]],
	['424', a, [
	'父上は、',
	'それきり帰ってはこられなかった',
	
	'イザークの民は、',
	'父上が殺された事を知って逆上し、',
	
	'マリクル兄様も',
	'グランベルとの全面戦争を決意された',
	]],
	['453', a, [
	'クルト王子が平和の求めを拒絶するとは',
	'とても考えられない',
	
	'この話をシグルドは知っているのか？',
	]],
	['464', a, [
	'いや、シグルド殿には言わないでくれ',
	'公子にはこれ以上の負担をかけたくない',
	'それに兄上はもう・・・',
	]],
	['473', a, [
	'マリクル王子は死を覚悟されていたのか・・・',
	]],
	['474', a, [
	'兄上はシャナンさえ生きていれば、',
	'イザークは再び甦るとおっしゃられた',
	
	'私の役目は、シャナンの成長を',
	'見届けることなのだと・・・',
	]],
	['493', a, [
	'そうか・・・アイラ王女、',
	'いずれ真相もわかるだろう',
	'それまでは我慢してほしい',
	
	'私もできるだけ力になろう',
	]],
	['504', a, [
	'キュアン殿、感謝する',
	]],
	
	['', a, [
	'会話：エーディン→エスリン',
	]],
	['513', a, [
	'エーディン、大丈夫？',
	'敵に連れ去られたと聞いて',
	'心配していたのよ',
	]],
	['514', a, [
	'エスリン、あなたまで戦ってくれたのね',
	'ありがとう・・・ごめんなさいね',
	
	'お礼といってはなんですが、',
	'この杖を差し上げます',
	
	'私よりあなたの方が、',
	'役に立つはずですから',
	]],
	['543', a, [
	'これはリターンの杖！？',
	'ありがとう、エーディン',
	'これでみんなを助けられます',
	
	'(リターンの杖)',
	]],
	
	['改ページ', -1, ['']],
	
	['', a, [
	'村2解放',
	]],
	['564', a, [
	'この国の王様は優しい方で',
	'決して自分から戦争など仕掛ける方では',
	'ありませんでした',
	
	'こんなことになったのは',
	'すべてあのサンディマという',
	'魔法使いのせいです',
	
	'あの男が来てから',
	'この国は住みにくくなる一方で、',
	
	'王子達も、末っ子のジャムカ様を除いては',
	'皆サンディマのいいなりなのです',
	
	'どうか、おねがいです',
	'この国をお救い下さい',
	
	'(2000ゴールド)',
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
