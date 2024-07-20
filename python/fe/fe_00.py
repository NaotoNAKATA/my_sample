# -*- coding: utf-8 -*-

import fe_param_00.pptx as pptx
import fe_param_00.prologue as prlg


from fe_pptx import fe_pptx
from fe_compose import fe_compose
from fe_prologue import fe_prologue

if __name__ == "__main__":

	#
	# プレゼンテーションの作成
	#
	fe = fe_pptx(pptx.title)
	
	#
	# 表題スライド
	#
	fe.make_title(subtitle=pptx.subtitle)
	
	#
	# プロローグスライド
	#
	# プロローグ(全体マップ)
	fe_prlg = fe_prologue()
	fe_prlg.configure(prlg)
	fe_prlg.run()
	
	# プロローグ(シナリオ)
	fe_prlg_senario = fe_prologue()
	fe_prlg_senario.add_dir(prlg.slides)
	fe_prlg_senario.read()
	fe_prlg_senario.save_main_temp()
	
	# プロローグスライドの作成
	fe.make_prologue(
		field_map=fe_prlg.out_file,
		phrase=prlg.phrase,
		titile_file=prlg.title_file,
	)
	
	# プロローグのアニメーションgifの作成
	fe_prlg_gif = fe_compose()
	fe_prlg_gif.add_dir(prlg.dir_gif)
	fe_prlg_gif.set_out_file(prlg.out_gif)
	fe_prlg_gif.read()
	fe_prlg_gif.save_gif(fps=0.5)
	
	# Tempの削除
	fe_prlg_senario.del_temp2()
	
	#
	# Phase1
	#
	# 導入(切り出し)
	
	
	# 編成
	
	# 戦闘
	
	# 終幕
	
	#
	# Phase2
	#
	
	# 導入
	
	# 編成
	
	# 会話
	
	# 村解放
	
	# 戦闘
	
	# 終幕
	
	#
	# Phase3
	#
	
	# 導入
	
	# 編成
	
	# 会話
	
	# 戦闘
	
	# 終幕
	
	#
	# プレゼンテーションの保存
	#
	fe.save()
	