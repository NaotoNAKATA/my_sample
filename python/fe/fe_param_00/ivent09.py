from .params import *
scene_dir = [
	'22-アルヴィス登場/',
	'23-(アルヴィス-シグルド)/',
	'27-(アルヴィス-シグルド)/',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]
#files = []

title = 'Phase3 : 会話イベント'

a = 1
fld = 0.5
bat = 0.75

scene = [
	['', a, [
	'ユングヴィ城制圧後',
	]],
	['020', fld,[]],
	['004', a, [
	'国王陛下から',
	'様子をみてくるように言われたが',
	'蛮族相手に、こうも手こずるとはな',
	'シグルド・・・',
	'貴様も所詮はその程度の男か・・・',
	]],
	
	['', a, [
	'会話：アルヴィス←→シグルド',
	]],
	['033', a, [
	'シグルド公子、久しぶりだな',
	]],
	['034', a, [
	'アルヴィス卿！？どうしてあなたが・・・',
	]],
	['033', a, [
	'陛下が心配されてな',
	'私に見てくるよう命じられた',
	'それと、これは陛下からくだされた物だ',
	'受け取ってくれ',
	]],
	['034', a, [
	'これは銀の剣！',
	'・・・陛下がこれを私に・・・',
	'ああ、何と名誉なことだ',
	'アルヴィス卿、陛下には',
	'シグルドが感謝していたと',
	'お伝えしてください',
	]],
	['033', a, [
	'承知した',
	'ところでシグルド、',
	'弟のアゼルが君の軍に',
	'加わっていると聞いたが本当なのか？',
	]],
	['034', a, [
	'すみません、黙って来たようでしたが',
	'追い返せなかった',
	'できればしばらく',
	'我が軍にいて欲しいのですが',
	]],
	['033', a, [
	'そうか・・・いや、無事ならいいんだ',
	'アゼルは母親こそ違うが',
	'私にとって、たった一人の大事な弟',
	'できれば側にいてほしいが、',
	'やむを得ぬだろう・・・',
	'シグルド、アゼルの事を頼む',
	'いろいろと教えてやってくれ',
	]],
	['034', a, [
	'お任せ下さい',
	'この戦いが終われば',
	'私からも、戻るように説得してみます',
	]],
	['033', a, [
	'それを聞いて安心した',
	'では私は王都バーハラに戻る',
	'陛下をお守りせねばならぬからな',
	'シグルド、後は頼んだぞ',
	]],
	['034', a, [
	'(ぎんの剣)',
	]],
	
	['', a, [
	'(アゼルが戦死しているとき)',
	]],
	['033', a, [
	'承知した',
	'ところでシグルド、',
	'弟のアゼルが君の軍に',
	'加わっていると聞いたが無事でいるか？',
	]],
	['034', a, [
	'それが・・・アゼルは・・・',
	]],
	['033', a, [
	'戦死したということか',
	]],
	['034', a, [
	'すみません',
	'私の力が足りないばかりに・・・',
	]],
	['033', a, [
	'アゼル・・・馬鹿な弟だ・・・',
	]],
	['034', a, [
	'(ぎんの剣)',
	]],
	
]
