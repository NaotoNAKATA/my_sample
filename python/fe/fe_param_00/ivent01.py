# シアルフィ出撃
base_dir = '/storage/43E3-332A/others/test/work/ROM/SNES/ファイアーエムブレム 聖戦の系譜 (J)/'
#base_dir = './test/'
chaper_dir = '00-序章-聖騎士誕生/'
ivent_dir = '01-シアルフィ出撃/'

title = 'Phase1 : シアルフィ出撃'

#dirs = [
	#base_dir + chaper_dir + ivent_dir,
#]

files = [
	base_dir + chaper_dir + ivent_dir + '2024-06-07 午後11.32.44.png',
	base_dir + chaper_dir + ivent_dir + '2024-06-07 午後11.33.56.png',
	base_dir + chaper_dir + ivent_dir + '2024-06-07 午後11.33.13.png',
	base_dir + chaper_dir + ivent_dir + '2024-06-07 午後11.34.06.png',
	base_dir + chaper_dir + ivent_dir + '2024-06-07 午後11.35.12.png',
	base_dir + chaper_dir + ivent_dir + '2024-06-07 午後11.33.56.png',
	base_dir + chaper_dir + ivent_dir + '2024-06-07 午後11.36.17.png',
	base_dir + chaper_dir + ivent_dir + '2024-06-07 午後11.37.32.png',
]

persons = {
	'ミデェール' : '021',
	'エーディン'  : '022',
	'シグルド' : '031',
	'ノイッシュ' : '032',
	'アレク' : '042',
	'オイフェ' : '062',
	'アーダン' : '072',
}

a = 1

scene = [
	['000', 0.5,[]],
	[persons['ミデェール'], a, [
	'エーディン様、敵に城を包囲されました',
	'姫様をお守りすべき我々が、',
	'不甲斐ないばかりに・・・',
	]],
	[persons['エーディン'], a, [
	'よいのです、ミデェール',
	'・・・皆よく戦ってくれました',
	'私のことは、もういいのです',
	'今は一人でも多く、生き延びて下さい',
	]],
	[persons['ミデェール'], a, [
	'いいえ、エーディン様',
	'皆、最後まで姫様をお守りする覚悟です',
	'命にかえても、お守りいたします',
	]],
	[persons['エーディン'], a, [
	'ありがとう、ミデェール',
	'・・・ごめんなさい',
	]],
	
	['050', 0.5,[]],
	[persons['シグルド'], a, [
	'ユングヴィの城がガンドルフ軍に包囲された',
	'このままではエーディンが危ない',
	'ノイッシュ、私は彼女を助けに行く',
	'あとのことは頼んだぞ！',
	]],
	[persons['ノイッシュ'], a, [
	'待ってください、シグルド様',
	'まさか一人で行かれるつもりでは？',
	]],
	[persons['シグルド'], a, [
	'我が軍の主力は',
	'父上とともにイザークへ遠征して',
	'ここに残っているのはわずかしかいない',
	'ヴェルダン軍は蛮族とはいえ大軍だ',
	'死ぬことがわかっている戦いに',
	'お前達を巻き込めない',
	]],
	[persons['ノイッシュ'], a, [
	'バカなこと言わないで下さい',
	'騎士として生まれた以上',
	'戦いで死ぬのは当たり前',
	'主君一人を死なせて',
	'おめおめと生きてはおれません',
	'私たちも共にまいります',
	'アレク、お前も同じ考えだろ',
	]],
	[persons['アレク'], a, [
	'ああ、もちろんだ',
	'しかしユングヴィの城も大事だが',
	'村を助けるのが先じゃないかな',
	'蛮族どもは行く先々の村を襲って',
	'奪い、殺し、焼き尽くしているという',
	'手遅れにならないうちに',
	'村々をまわって、守りを固めるように',
	'言わなければならないだろう',
	]],
	[persons['シグルド'], a, [
	'確かにそうだ',
	'民を守ることは我ら騎士の義務だ',
	'アレク、よく言ってくれた',
	]],
	[persons['アレク'], a, [
	'いや、本当はオイフェの意見なんです',
	'さすがは名軍師といわれたスサール卿の孫',
	'まだ子供なのに',
	'いろんなことに気がつきます',
	]],
	[persons['シグルド'], a, [
	'オイフェが王宮に来ているのか？',
	'オイフェ、いるなら来なさい',
	]],
	[persons['オイフェ'], a, [
	'シグルド様、勝手に来てごめんなさい',
	'でも出撃されるなら、',
	'ぼくも一緒に連れていって下さい',
	'城で留守番なんてイヤです',
	]],
	[persons['シグルド'], a, [
	'しかし、お前はまだ子供だ',
	'大丈夫なのか？',
	]],
	[persons['オイフェ'], a, [
	'ぼくも、もう十四才になりました',
	'まだ戦うことはできませんが',
	'シグルド様のお世話くらいならできます',
	'おねがいです',
	'どうか、おそばにおいてください',
	]],
	[persons['シグルド'], a, [
	'わかったよ、オイフェ',
	'お前が騎士見習いとして',
	'私のところに来てから、もう二年になる',
	'そろそろ戦場を経験するのも悪くはないだろう',
	'ただし、戦うのはまだ早い',
	'しばらくは私のそばにいて',
	'相談相手になってくれ',
	]],
	[persons['オイフェ'], a, [
	'はい！ありがとうございます',
	]],
	[persons['ノイッシュ'], a, [
	'シグルド様、この城の守りはどうしますか？',
	'誰か一人は守備に上がらないと危険です',
	'もし本拠地であるこの城が敵に奪われたら',
	'我らは全滅します',
	]],
	[persons['アレク'], a, [
	'ノイッシュ、城の守りなら',
	'コイツしかいないぜ！なっ、アーダン！',
	]],
	[persons['アーダン'], a, [
	'アレクっ、なんで俺なんだよ',
	]],
	[persons['アレク'], a, [
	'固い、強い、遅い！',
	'三拍子そろっているのは',
	'お前しかいないだろう',
	]],
	[persons['アーダン'], a, [
	'固い、強いってのはいいけど',
	'遅いってのは気にいらねぇな',
	]],
	[persons['シグルド'], a, [
	'いや、アーダン、私からも頼む',
	'城の守りを任せられるのはお前だけだ',
	]],
	[persons['アーダン'], a, [
	'はぁ、わかりました',
	'そんなら、とりあえず守備に上がります',
	'でもたまには私も出陣させて下さいよ',
	]],
	[persons['シグルド'], a, [
	'よし、それでは行こう',
	'とりあえず村を助ける',
	'そしてユングヴィへ！',
	]],
	
]
