from .params import *
scene_dir = [
	'13-キュアン-フィン',
	'16-アーダン追撃を得る',
	'17-傭兵ベオウルフを雇う',
	'19-シグルド-レヴィン',
	'70-村',
	'71-村',
	'72-村',
	'73-村',
	'74-村',
	'75-村',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]

files = [
]

title = 'Phase2 : 会話イベント'

a = 1
fld = 0.5
bat = 0.75

scene = [
	['', a, [
	'キュアン→フィン',
	]],
	['003', a, [
	'フィン、この戦いはアグストリアの騎士が相手だ',
	'今までのような蛮族とは違う',
	
	'これまでの武器では苦戦は免れぬだろう',
	'この槍をお前にやろう',
	]],
	['014', a, [
	'これは、勇者の槍・・・',
	'この槍を頂いてもよいのですか？',
	]],
	['023', a, [
	'おまえは私の部下であるだけでなく、',
	'レンスターに仕えてくれる大切な騎士だ',
	'この戦いで失うわけにはいかない',
	
	'私が今してやれるのはこれくらいだが、受け取ってほしい',
	]],
	['034', a, [
	'ありがとうございます',
	'キュアン様',
	'',
	
	'(ゆうしゃのやり)',
	]],
	
	['改ページ', -1, ['']],
	
	['', a, [
	'アーダンを湖畔へ',
	]],
	['050', fld,[]],
	['064', a, [
	'・・・ああ、さびしい・・・',
	'俺はこんなに固くて強いのに、',
	'みんなで俺をバカにして・・・',
	
	'せめてアレクみたいに再攻撃できれば、',
	'もう少しは働けるのになあ・・・',
	
	'そしたら俺にも彼女ができるかもしれんのになあ・・・',
	'ハァ・・・男はつらいぜ',
	
	'',
	'ん？何だ、この古びた腕輪は？',
	'何か魔法の腕輪みたいだが、ちょっと付けてみよう',
	
	'ん・・・むむ・・・！',
	'な、なんだこの感じは！',
	'おおっ、俺にも追撃の力が・・・！',
	
	'(ついげきリング)',
	]],
	
	['改ページ', -1, ['']],
	
	['', a, [
	'vsベオウルフ',
	]],
	['137', bat,[]],
	['135', a, [
	'お前に怨みはないが・・・これも生きていくためだ',
	]],
	
	['', a, [
	'(10000G)→ベオウルフ',
	]],
	['153', a, [
	'俺を雇いたいのか',
	'それなら10000ゴールドよこしな',
	]],
	['154', a, [
	'',
	]],
	['163', a, [
	'・・・よし、確かに受け取った',
	'もらった金の分ぐらいは働いてやるぜ',
	]],

	['', a, [
	'シグルド→レヴィン',
	]],
	['173', a, [
	'君がレヴィン？',
	'村人を助けてくれたそうだね',
	'ありがとう、礼を言う',
	
	'旅の吟遊詩人と聞いたが魔法が使えるとは驚きだね',
	]],
	['184', a, [
	'まあね、魔法も芸のうちさ',
	'',
	'ふーん、あんたがシグルド公子か',
	
	'わざわざ他所の国まで押しかけて戦争するとは',
	'よっぽどヒマらしいな',
	]],
	['203', a, [
	'君は怒っているようだね',
	]],
	['204', a, [
	'当たり前だ、ちょっとは働いてる者の身にもなってみろ',
	
	'ドンパチやるのは勝手だが俺達は迷惑なんだよ！',
	]],
	['223', a, [
	'すまない、確かにその通りだ',
	'この国の人々には申し訳ないと思っている',
	]],
	['224', a, [
	'口先だけなら何とでも言えるさ',
	'本当に悪いと思っているなら今すぐ国に帰ったらどうだ',
	]],
	['233', a, [
	'そうだな・・・わかった',
	'みんなに相談してみよう',
	]],
	['234', a, [
	'おいおい、本気なのか',
	]],
	['243', a, [
	'もちろんだ',
	'私もずっと考えていた',
	'君に言われてやっと決心がついたよ',
	
	'戦争はやめる',
	'シャガール王と話し合ってみるよ',
	]],
	['254', a, [
	'あの男に何を言ってもムダさ',
	
	'グランベルが兵を引き上げれば、',
	'協力した住民を片っ端から処刑するだろう',
	
	'あんたはそれでもいいのか',
	]],
	['283', a, [
	'それは・・・しかし・・・',
	]],
	['284', a, [
	'ははは、もういいよ',
	'やっぱりあんたは思っていた通りの人だ',
	'俺も協力させてもらうぜ',
	]],
	['293', a, [
	'え？君はいったい・・・',
	]],
	['294', a, [
	'俺はただの旅人・・・吟遊詩人さ',
	]],
	
	['改ページ', -1, ['']],
	
	['', a, [
	'村1',
	]],
	['304', a, [
	'アンフォニー領主のマクベスは金に汚い男でね',
	'今までも散々わしらを苦しめた',
	
	'あんなヤツ、死んじまえばいいんだ！',
	
	'(5000G)',
	]],
	
	['', a, [
	'村2',
	]],
	['334', a, [
	'ちょっと、あんた、どう思う？',
	
	'ノディオンのエルトシャン王と妹のラケシス姫、',
	'兄妹にしちゃあ仲が良すぎると思わないかい？',
	
	'あたしら、いつも噂してるのさ',
	'えっ？そんなに暇なのかって？',
	'なんだい！悪かったね！！',
	
	'(5000G)',
	]],
	
	['', a, [
	'村3',
	]],
	['374', a, [
	'戦争は嫌だねえ',
	'泣くのはいつも女や子供さ',
	'あんたも早く恋人の所へ帰ってやりなよ',
	
	'(5000G)',
	]],
	
	['改ページ', -1, ['']],
	
	['', a, [
	'村4',
	]],
	['394', a, [
	'ほお〜、これはよく来てくれたのぉ',
	'ほおびにこの剣をやろう',
	
	'これは斬鉄の剣といってな',
	'硬い鎧でも切り裂くことができる不思議な剣じゃ',
	
	'もしお前さんが使えなければ中古屋に売るといい',
	'良い金になるぞ',
	
	'(ざんてつの剣)',
	
	'(5000G)',
	]],
	
	['', a, [
	'村5',
	]],
	['444', a, [
	'助けてくれてありがとう',
	'お礼に私の大切なモノをあげるわ',
	
	'ほら、綺麗な腕輪でしょ',
	'これを付けてると、',
	'お店のおじさんがサービスしてくれるのよ',
	
	'(ねぎりのうでわ)',
	
	'(500G)',
	]],
	
	['', a, [
	'村6',
	]],
	['484', a, [
	'暗黒神ロプトウスの血族が、',
	'まだ生き延びているって本当かな？',
	
	'アグスティやマッキリーみたいな大きな街じゃ、',
	'毎年たくさんの人が魔神狩りという名のもとに、',
	
	'火あぶりになって殺されている',
	'別に罪人でもないのに非道い話だぜ',
	
	'(2000G)',
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
