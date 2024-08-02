base_dir = '/storage/43E3-332A/others/test/work/ROM/SNES/ファイアーエムブレム 聖戦の系譜 (J)/'
#base_dir = './test/'
chaper_dir = '00-序章-聖騎士誕生/'
ivent_dir = '24-vsゲラルド/'
ivent_dir2 = '25-ミデェールvsゲラルド/'

title = 'Phase3 : vsゲラルド'

dirs = [
	base_dir + chaper_dir + ivent_dir,
	base_dir + chaper_dir + ivent_dir2,
]

#files = [
#]

a = 1
fld = 0.5
bat = 0.75

scene = [
	['006', bat,[]],
	['005', a, [
	'グランベルの犬め',
	'くたばれ！',
	]],
	['016', bat,[]],
	['026', bat,[]],
	['036', bat,[]],
	['035', a, [
	'残念だったな・・・',
	'あの女はここにはいねぇよ',
	'今頃はガンドルフ王子に・・・',
	]],
	['046', bat,[]],
	
	['', a, [
	'ミデェールvsゲラルド',
	]],
	['053', a, [
	'ま、待て！',
	'飛び道具とは卑怯だぞ！',
	]],
	['054', a, [
	'だまれ！エーディン様をどこへやった！',
	'早く返せ！！',
	]],
]
