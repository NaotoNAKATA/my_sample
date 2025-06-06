# -*- coding: utf-8 -*-

import fe_param_02.pptx as pptx
import fe_param_02.prologue_map as prlg
import fe_param_02.prologue_scene as prlg_s
#import fe_param_01.prologue_gif as prlg_g

import fe_param_02.field00 as fld00
import fe_param_02.field01 as fld01
import fe_param_02.field02 as fld02
import fe_param_02.field03 as fld03
import fe_param_02.field04 as fld04

import fe_param_02.ivent01 as ivt01
import fe_param_02.ivent02 as ivt02
import fe_param_02.ivent03 as ivt03
import fe_param_02.ivent04 as ivt04
import fe_param_02.ivent05 as ivt05
import fe_param_02.ivent06 as ivt06
import fe_param_02.ivent07 as ivt07
import fe_param_02.ivent08 as ivt08
import fe_param_02.ivent09 as ivt09
import fe_param_02.ivent10 as ivt10
import fe_param_02.ivent11 as ivt11
import fe_param_02.ivent12 as ivt12
import fe_param_02.ivent13 as ivt13
import fe_param_02.ivent14 as ivt14
import fe_param_02.ivent15 as ivt15
import fe_param_02.ivent16 as ivt16
import fe_param_02.ivent17 as ivt17
import fe_param_02.ivent18 as ivt18
import fe_param_02.ivent19 as ivt19
import fe_param_02.ivent20 as ivt20
import fe_param_02.ivent21 as ivt21

import fe_param_02.profile01 as prf01
import fe_param_02.profile02 as prf02
import fe_param_02.profile03 as prf03
import fe_param_02.profile04 as prf04
import fe_param_02.profile05 as prf05
import fe_param_02.profile06 as prf06
import fe_param_02.profile07 as prf07
import fe_param_02.profile08 as prf08
import fe_param_02.profile09 as prf09

#import fe_param_01.battle01 as btl01

from fe_pptx import fe_pptx
from fe_compose import fe_compose
from fe_prologue import fe_prologue
from fe_prologue_scene import fe_prologue_scene
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
	# 導入
	fe_ivt01 = fe_ivent()
	fe_ivt01.configure(ivt01)
	fe_ivt01.run()
	
	fe.make_ivent(
		scene=ivt01.scene,
		title=ivt01.title,
	)
	
	# 2ターン目
	fe_ivt02 = fe_ivent()
	fe_ivt02.configure(ivt02)
	fe_ivt02.run()
	
	fe.make_ivent(
		scene=ivt02.scene,
		title=ivt02.title,
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
	
	# 登場人物
	fe_prf02 = fe_profile()
	fe_prf02.configure(prf02)
	fe_prf02.run()
	
	# 編成
	fe.make_organization(
		field_map=fe_fld01.out_file,
		title=prf02.title,
		organization=prf02.organization,
	)
	
	# 登場人物
	fe_prf03 = fe_profile()
	fe_prf03.configure(prf03)
	fe_prf03.run()
	
	# 編成
	fe.make_organization(
		field_map=fe_fld01.out_file,
		title=prf03.title,
		organization=prf03.organization,
	)
	
	# 登場人物
	fe_prf04 = fe_profile()
	fe_prf04.configure(prf04)
	fe_prf04.run()
	
	# 編成
	fe.make_organization(
		field_map=fe_fld01.out_file,
		title=prf04.title,
		organization=prf04.organization,
	)
	
	# 会話イベント
	fe_ivt03 = fe_ivent()
	fe_ivt03.configure(ivt03)
	fe_ivt03.run()
	
	fe.make_ivent(
		scene=ivt03.scene,
		title=ivt03.title,
	)
	
	# 戦闘
	fe_ivt04 = fe_ivent()
	fe_ivt04.configure(ivt04)
	fe_ivt04.run()
	
	fe.make_ivent(
		scene=ivt04.scene,
		title=ivt04.title,
	)
	
	# 戦闘
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
	# 導入
	fe_ivt08 = fe_ivent()
	fe_ivt08.configure(ivt08)
	fe_ivt08.run()
	
	fe.make_ivent(
		scene=ivt08.scene,
		title=ivt08.title,
	)
	
	fe_ivt09 = fe_ivent()
	fe_ivt09.configure(ivt09)
	fe_ivt09.run()
	
	fe.make_ivent(
		scene=ivt09.scene,
		title=ivt09.title,
	)
	
	# フィールドマップ作成
	fe_fld02 = fe_field()
	fe_fld02.configure(fld02)
	fe_fld02.run()
	
	# 登場人物
	fe_prf05 = fe_profile()
	fe_prf05.configure(prf05)
	fe_prf05.run()
	
	# 編成
	fe.make_organization(
		field_map=fe_fld02.out_file,
		title=prf05.title,
		organization=prf05.organization,
	)
	
	# 登場人物
	fe_prf06 = fe_profile()
	fe_prf06.configure(prf06)
	fe_prf06.run()
	
	# 編成
	fe.make_organization(
		field_map=fe_fld02.out_file,
		title=prf06.title,
		organization=prf06.organization,
	)
	
	# 会話イベント
	fe_ivt10 = fe_ivent()
	fe_ivt10.configure(ivt10)
	fe_ivt10.run()
	
	fe.make_ivent(
		scene=ivt10.scene,
		title=ivt10.title,
	)
	
	# 戦闘
	fe_ivt11 = fe_ivent()
	fe_ivt11.configure(ivt11)
	fe_ivt11.run()
	
	fe.make_ivent(
		scene=ivt11.scene,
		title=ivt11.title,
	)
	
	fe_ivt12 = fe_ivent()
	fe_ivt12.configure(ivt12)
	fe_ivt12.run()
	
	fe.make_ivent(
		scene=ivt12.scene,
		title=ivt12.title,
	)
	
	# 制圧
	fe_ivt13 = fe_ivent()
	fe_ivt13.configure(ivt13)
	fe_ivt13.run()
	
	fe.make_ivent(
		scene=ivt13.scene,
		title=ivt13.title,
	)
	
	#
	# Phase3
	#
	# 導入
	fe_ivt14 = fe_ivent()
	fe_ivt14.configure(ivt14)
	fe_ivt14.run()
	
	fe.make_ivent(
		scene=ivt14.scene,
		title=ivt14.title,
	)
	
	# フィールドマップ作成
	fe_fld03 = fe_field()
	fe_fld03.configure(fld03)
	fe_fld03.run()
	
	# 登場人物
	fe_prf07 = fe_profile()
	fe_prf07.configure(prf07)
	fe_prf07.run()
	
	# 編成
	fe.make_organization(
		field_map=fe_fld03.out_file,
		title=prf07.title,
		organization=prf07.organization,
	)
	
	fe_prf08 = fe_profile()
	fe_prf08.configure(prf08)
	fe_prf08.run()
	
	# 編成
	fe.make_organization(
		field_map=fe_fld03.out_file,
		title=prf08.title,
		organization=prf08.organization,
	)
	
	# 会話イベント
	fe_ivt15 = fe_ivent()
	fe_ivt15.configure(ivt15)
	fe_ivt15.run()
	
	fe.make_ivent(
		scene=ivt15.scene,
		title=ivt15.title,
	)
	
	# 戦闘
	fe_ivt16 = fe_ivent()
	fe_ivt16.configure(ivt16)
	fe_ivt16.run()
	
	fe.make_ivent(
		scene=ivt16.scene,
		title=ivt16.title,
	)
	
	# 制圧
	fe_ivt17 = fe_ivent()
	fe_ivt17.configure(ivt17)
	fe_ivt17.run()
	
	fe.make_ivent(
		scene=ivt17.scene,
		title=ivt17.title,
	)
	
	#
	# Phase4
	#
	# 導入
	fe_ivt18 = fe_ivent()
	fe_ivt18.configure(ivt18)
	fe_ivt18.run()
	
	fe.make_ivent(
		scene=ivt18.scene,
		title=ivt18.title,
	)
	
	# フィールドマップ作成
	fe_fld04 = fe_field()
	fe_fld04.configure(fld04)
	fe_fld04.run()
	
	# 登場人物
	fe_prf09 = fe_profile()
	fe_prf09.configure(prf09)
	fe_prf09.run()
	
	# 編成
	fe.make_organization(
		field_map=fe_fld04.out_file,
		title=prf09.title,
		organization=prf09.organization,
	)
	
	# 戦闘
	fe_ivt19 = fe_ivent()
	fe_ivt19.configure(ivt19)
	fe_ivt19.run()
	
	fe.make_ivent(
		scene=ivt19.scene,
		title=ivt19.title,
	)
	
	fe_ivt20 = fe_ivent()
	fe_ivt20.configure(ivt20)
	fe_ivt20.run()
	
	fe.make_ivent(
		scene=ivt20.scene,
		title=ivt20.title,
	)
	
	# 制圧
	fe_ivt21 = fe_ivent()
	fe_ivt21.configure(ivt21)
	fe_ivt21.run()
	
	fe.make_ivent(
		scene=ivt21.scene,
		title=ivt21.title,
	)
	
	#
	# プレゼンテーションの保存
	#
	fe.save()
	
	#
	# アニメーションgifの作成
	#
	if False:
		from fe_gif import fe_gif
		# プロローグ
		fe_prlg_gif = fe_gif()
		fe_prlg_gif.configure(prlg_g)
		fe_prlg_gif.run()
