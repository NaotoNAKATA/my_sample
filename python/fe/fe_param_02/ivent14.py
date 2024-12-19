from .params import *
scene_dir = [
	'22-マッキリー出撃',
	'23-アグスティ出撃',
	
]
dirs = [ base_dir + chaper_dir + s for s in scene_dir]

files = [
]

title = 'Phase3：アグストリア全面戦争'

a = 1
fld = 0.5
bat = 0.75

scene = [
	['', a, [
	'マッキリー出撃',
	]],
	['000', fld, []],
	['012', a, [
	'なに、アンフォニーまで制圧されただと！？',
	'むむ・・・さては奴ら、アグストリアを征服するつもりか',
	
	'こうなっては戦う他はない',
	'シューターを配置につかせろ',
	
	'グランベル軍をアグスティへ行かせてはならん！',
	]],
	['040', fld, []],
	
	['改ページ', -1, ['']],
	
	['', a, [
	'アグスティ出撃',
	]],
	['050', fld, []],
	['061', a, [
	'シャガール王',
	'いつまで待てば良いのですか',
	
	'私達は一刻も早くレヴィン王子を探さねばならぬのです',
	
	'あなたが王子のいる所を知っているというから、',
	'私はこの城にとどまっているのです',
	]],
	['082', a, [
	'いや、すまぬな',
	'しかし、ようやくわかった',
	
	'レヴィン王子はグランベルの軍隊に、',
	'捕らわれているという事だ',
	'ヤツらは我が国を侵略し、そのうえ関係のない人々まで、',
	
	'手当たり次第に捕まえて処刑しているらしい',
	
	'王子も、ヤツらの本拠地エバンスに囚われ、',
	'間もなく処刑されるという',
	'早く助けねば危ないぞ',
	]],
	['121', a, [
	'なんてこと・・・わかりました',
	'今すぐエバンスに向かい王子を助け出してきます',
	
	'シレジアのラーナ王妃からは、',
	'他国との争いを避けよと言われましたが、',
	'やむを得ません',
	
	'グランベル軍は見つけ次第、攻撃いたします',
	]],
	['142', a, [
	'おお、それは願ってもない',
	'よろしく頼むぞ',
	]],
	['151', a, [
	'では、失礼します',
	]],
	
	['160', fld, []],
	
	['172', a, [
	'ふっ、行ったか・・・バカな女め・・・',
	'よし、アグスティからも騎士団をだせ！',
	'一気にケリをつけるのだ！',
	]],
	
	['180', fld, []],
	
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
