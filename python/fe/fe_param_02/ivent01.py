from .params import *
scene_dir = [
	'01-アグストリアの動乱/',
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]

files = [
]

title = 'Phase1 : アグストリアの動乱'

a = 1
fld = 0.5
bat = 0.75

scene = [
	['000', fld,[]],
	
	['011', a, [
	'ラケシス、俺はアグスティへ向かう',
	'愚かな挙兵など止めるようシャガール王にお願いする',
	]],
	['012', a, [
	'お待ち下さい、兄上！',
	'シャガール王は自分のお父上すら手にかけたお方、',
	
	'そんな方に何を言っても無駄です',
	'それどころか兄上の身すら危険です',
	]],
	['031', a, [
	'ラケシス、めったなことを言うな',
	'シャガール王が前王を暗殺したという噂は俺も聞いた',
	
	'しかし証拠があるわけではない',
	'諦めずにご説得申し上げれば、',
	'王もきっとわかって下さると思う',
	]],
	['042', a, [
	'しかし・・・',
	]],
	['051', a, [
	'もう何も言うな、',
	
	'万が一の時の為に、',
	'この城には俺が最も信頼する三人の部下を残して行く',
	'',
	
	'ラケシス、そんな悲しそうな顔をするな',
	'大丈夫だ、俺は必ず帰ってくる',
	'お前をおいて死にはしない',
	]],
	['072', a, [
	'エルト兄様・・・',
	]],
	
	#['080', fld,[]],
	['090', fld,[]],
	
	['改ページ', -1, ['']],
	
	#['100', fld,[]],
	['110', fld,[]],
	
	['121', a, [
	'シャガール陛下、どうか挙兵はお止め下さい',
	
	'陛下のお父上はグランベルとの共存を願っておられました',
	
	'戦争は民を苦しめ、',
	'陛下のお名前まで貶めることになります',
	
	'戦争だけはしてはならぬのです！！',
	]],
	['152', a, [
	'ノディオンのエルトシャンか',
	'貴様、父上に可愛がられていたのをよいことに、',
	'今までは散々わしに盾突きおって',
	
	'だがな・・・父上は死に、',
	'今ではわしが全アグストリアの支配者なのだ',
	
	'今までわしをコケにしてきた礼はたっぷりとさせてもらう',
	'誰か、コヤツを地下牢にぶち込め！',
	]],
	['181', a, [
	'ま、待って下さい！シャガール陛下・・・！！',
	]],
	['191', a, [
	'',
	]],
	['202', a, [
	'ふっ、エルトシャンめ、目障りな奴だ',
	'よし、ハイラインのボルドーにノディオン攻略を命じよ',
	
	'それが済み次第、全軍でグランベルに進撃する',
	]],
	['221', a, [
	'・・・シャガール陛下、やっとご決心されましたな',
	]],
	['222', a, [
	'マンフロイか',
	'貴様の言う通り父上はこの手で暗殺した',
	
	'もはや後戻りはなるまい',
	'しかし本当に勝てるのだろうな',
	]],
	['241', a, [
	'グランベルはアグストリアとの不戦条約を信じて、',
	'全軍でイザークへ遠征中です',
	
	'今攻め込めば必ず勝てるでしょう',
	]],
	['252', a, [
	'むむっ、そうか',
	'グランベルさえ倒せば、',
	'アグストリアが世界の支配者になれる',
	
	'そうすれば、わしが皇帝になれるのだな',
	]],
	['271', a, [
	'ふぉふぉふぉ・・・',
	'そうなることを夢見ていなされ・・・',
	]],
	
	['', a,['']],
	['000', fld,[]],
	
	['281', a, [
	'ラケシス様！',
	'エルトシャン王がアグスティで捕らわれたとの報告が！',
	]],
	['282', a, [
	'えっ、兄上が！？',
	'ああっ・・・だからあれほどお止めしたのに・・・',
	]],
	['改ページ', -1, ['']],
	
	['291', a, [
	'姫様、心配なのはそれだけではありません',
	'隣国ハイラインには注意すべきです',
	
	'王が不在と知らば、いつ攻めてくるかもしれません',
	
	'奴等はヴェルダンでの戦いを根に持っているでしょうし、',
	'特にエリオット王子は・・・',
	]],
	['312', a, [
	'エリオットは私が彼の言いなりにならないから',
	'腹を立てているのね',
	
	'でもあんなキザな男は、大キライ！',
	'私はエルト兄様のような人でなければ好きにはなれないわ',
	
	'だから、誰の妻にもならない・・・',
	]],
	['341', a, [
	'・・・それはよろしいのですが、',
	'王直属のクロスナイツも、',
	'今は北のシルベールの砦に駐留しており、',
	
	'この城には僅かな兵しか残っていません',
	
	'私は弟二人とともに全力でお守りしますが、',
	'もしものときは、お覚悟下さい',
	]],
	['362', a, [
	'わかっています',
	'イーヴ、あなたには感謝しているの',
	'でも無理はしないで、死んではダメです',
	
	'エヴァ、アルヴァにもラケシスが謝っていたと伝えてね',
	]],
	['381', a, [
	'もったいないお言葉',
	
	'・・・しかしながら、我々はエルト王から',
	'特に選ばれて、姫様をお守りするよう仰せつかったのです',
	
	'我々も栄光あるノディオンの聖騎士',
	'この一命にかけても最期まで姫様をお守りいたします！！',
	]],
	
	#['410', fld,[]],
	['420', fld,[]],
	
	#['改ページ', -1, ['']],
	['', a, [
	'',
	]],
	
	['430', fld,[]],
	
	['441', a, [
	'なに？あのエルトシャンが陛下のお怒りをかって、',
	'地下牢に放り込まれただと！？',
	
	'よし！エリオット！',
	'この隙にノディオンを攻め落とすのだ',
	'エルトシャンに吠え面かかせてやれ！',
	]],
	['452', a, [
	'かしこまりました、父上',
	]],
	
	['460', fld,[]],
	
	['改ページ', -1, ['']],
	
	['470', fld,[]],
	
	['481', a, [
	'シグルド様、大変です！',
	'エルトシャン様がアグスティ城に囚われ、',
	'ノディオンに攻撃されているとのことです',
	
	'ラケシス王女から援軍を請う書状がまいりました',
	]],
	['492', a, [
	'エルトシャンが！？',
	'なぜだ、あれほどの男が・・・',
	
	'わかった、とにかくノディオンに出陣しよう',
	
	'ラケシスだけは、私が一命にかえても守らねばならない',
	
	'エルトシャンは口にこそ出さなかったが、',
	'あの姫をずっと大事にしてきた',
	
	'ラケシスを失えば彼はどれほど嘆き悲しむ事か・・・',
	]],
	['541', a, [
	'シグルド様、また戦いが始まるのですか',
	]],
	['542', a, [
	'ディアドラ、すまない',
	'だが、私はエルトシャンに多くの借りがある',
	
	'不安な思いをしている彼の妹を、',
	'見捨てるわけにはいかないのだ',
	]],
	['561', a, [
	'はい、わかっています',
	'止めはしません',
	'でも、私も一緒に行きます',
	]],
	['562', a, [
	'え、それは駄目だ',
	'君を危険な目にあわせたくない',
	]],
	['571', a, [
	'シグルド様は約束して下さいました',
	'絶対、私を離さないって',
	'私・・・不安なのです・・・',
	
	'・・・あなたと離れれば、',
	'二度と会えなくなるような気がして・・・',
	'お願いです、どうか私もお側に・・・',
	]],
	['582', a, [
	'ごめん・・・そうだったね',
	'わかった、一緒に行こう',
	'でも、私の側を離れては駄目だよ',
	]],
	['591', a, [
	'はい！シグルド様',
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
