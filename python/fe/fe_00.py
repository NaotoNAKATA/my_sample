# -*- coding: utf-8 -*-

import fe_param_00.pptx as pptx
import fe_param_00.prologue_map as prlg
import fe_param_00.prologue_scene as prlg_s
import fe_param_00.prologue_gif as prlg_g
import fe_param_00.field00 as fld00
import fe_param_00.field01 as fld01
import fe_param_00.field02 as fld02
import fe_param_00.field03 as fld03
import fe_param_00.ivent01 as ivt01
import fe_param_00.ivent02 as ivt02
import fe_param_00.ivent03 as ivt03
import fe_param_00.ivent04 as ivt04
import fe_param_00.ivent05 as ivt05
import fe_param_00.ivent06 as ivt06
import fe_param_00.ivent07 as ivt07
import fe_param_00.ivent08 as ivt08
import fe_param_00.ivent09 as ivt09
import fe_param_00.ivent10 as ivt10
import fe_param_00.ivent11 as ivt11
import fe_param_00.profile01 as prf01
import fe_param_00.profile02 as prf02
import fe_param_00.profile03 as prf03
import fe_param_00.battle02 as btl02
import fe_param_00.battle03 as btl03

from fe_pptx import fe_pptx
from fe_compose import fe_compose
from fe_prologue import fe_prologue
from fe_prologue_scene import fe_prologue_scene
#from fe_gif import fe_gif
from fe_ivent import fe_ivent
from fe_field import fe_field
from fe_profile import fe_profile

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
	
	# フィールドマップ作成
	fe_fld00 = fe_field()
	fe_fld00.configure(fld00)
	fe_fld00.run()
	
	# プロローグ(シナリオ)
	fe_prlg_s = fe_prologue_scene()
	fe_prlg_s.configure(prlg_s)
	fe_prlg_s.run()
	
	# プロローグスライドの作成
	fe.make_prologue(
		prologue_map=fe_prlg.out_file,
		field_map=fe_fld00.out_file,
		scene=prlg_s.scene,
		title=prlg_s.title,
	)

	#
	# Phase1
	#
	# イベント
	fe_ivt01 = fe_ivent()
	fe_ivt01.configure(ivt01)
	fe_ivt01.run()
	
	fe.make_ivent(
		scene=ivt01.scene,
		title=ivt01.title,
	)
	
	# フィールドマップ作成
	fe_fld01 = fe_field()
	fe_fld01.configure(fld01)
	fe_fld01.run()
	
	# 登場人物
	fe_prf01 = fe_profile()
	fe_prf01.configure(prf01)
	fe_prf01.run()
	
	# 編成
	fe.make_organization(
		field_map=fe_fld01.out_file,
		title=prf01.title,
		organization=prf01.organization,
	)
	
	# 戦闘
	fe_ivt02 = fe_ivent()
	fe_ivt02.configure(ivt02)
	fe_ivt02.run()
	
	fe.make_ivent(
		scene=ivt02.scene,
		title=ivt02.title,
	)
	
	# イベント
	fe_ivt03 = fe_ivent()
	fe_ivt03.configure(ivt03)
	fe_ivt03.run()
	
	fe.make_ivent(
		scene=ivt03.scene,
		title=ivt03.title,
	)
	
	# フィールドマップ作成
	fe_fld02 = fe_field()
	fe_fld02.configure(fld02)
	fe_fld02.run()
	
	# 登場人物
	fe_prf02 = fe_profile()
	fe_prf02.configure(prf02)
	fe_prf02.run()
	
	# 編成
	fe.make_organization(
		field_map=fe_fld02.out_file,
		title=prf02.title,
		organization=prf02.organization,
	)
	
	# 会話
	fe_ivt04 = fe_ivent()
	fe_ivt04.configure(ivt04)
	fe_ivt04.run()
	
	fe.make_ivent(
		scene=ivt04.scene,
		title=ivt04.title,
	)
	
	# 村解放
	fe_ivt05 = fe_ivent()
	fe_ivt05.configure(ivt05)
	fe_ivt05.run()
	
	fe.make_ivent(
		scene=ivt05.scene,
		title=ivt05.title,
	)
	
	# 戦闘
	fe_ivt06 = fe_ivent()
	fe_ivt06.configure(ivt06)
	fe_ivt06.run()
	
	fe.make_ivent(
		scene=ivt06.scene,
		title=ivt06.title,
	)
	
	# 制圧
	fe_ivt07 = fe_ivent()
	fe_ivt07.configure(ivt07)
	fe_ivt07.run()
	
	fe.make_ivent(
		scene=ivt07.scene,
		title=ivt07.title,
	)
	
	#
	# Phase2
	#
	# イベント
	fe_ivt08 = fe_ivent()
	fe_ivt08.configure(ivt08)
	fe_ivt08.run()
	
	fe.make_ivent(
		scene=ivt08.scene,
		title=ivt08.title,
	)
	
	# フィールドマップ作成
	fe_fld03 = fe_field()
	fe_fld03.configure(fld03)
	fe_fld03.run()
	
	# 登場人物
	fe_prf03 = fe_profile()
	fe_prf03.configure(prf03)
	fe_prf03.run()
	
	# 編成
	fe.make_organization(
		field_map=fe_fld03.out_file,
		title=prf03.title,
		organization=prf03.organization,
	)
	
	# 会話
	fe_ivt09 = fe_ivent()
	fe_ivt09.configure(ivt09)
	fe_ivt09.run()
	
	fe.make_ivent(
		scene=ivt09.scene,
		title=ivt09.title,
	)
	
	# 戦闘
	fe_ivt10 = fe_ivent()
	fe_ivt10.configure(ivt10)
	fe_ivt10.run()
	
	fe.make_ivent(
		scene=ivt10.scene,
		title=ivt10.title,
	)
	
	# 制圧
	fe_ivt11 = fe_ivent()
	fe_ivt11.configure(ivt11)
	fe_ivt11.run()
	
	fe.make_ivent(
		scene=ivt11.scene,
		title=ivt11.title,
	)
	
	#
	# プレゼンテーションの保存
	#
	fe.save()
	
	#
	# アニメーションgifの作成
	#
	
	# プロローグ
	#fe_prlg_gif = fe_gif()
	#fe_prlg_gif.configure(prlg_g)
	#fe_prlg_gif.run()
	
	# 戦闘シーン
	#fe_btl02 = fe_gif()
	#fe_btl02.configure(btl02)
	#fe_btl02.run()
	
	#fe_btl03 = fe_gif()
	#fe_btl03.configure(btl03)
	#fe_btl03.run()
	