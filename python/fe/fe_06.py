# -*- coding: utf-8 -*-

import fe_param_06.pptx as pptx
import fe_param_06.prologue_map as prlg
import fe_param_06.prologue_scene as prlg_s
#import fe_param_06.prologue_gif as prlg_g

import fe_param_06.field00 as fld00
import fe_param_06.field01 as fld01
import fe_param_06.field02 as fld02

import fe_param_06.ivent01 as ivt01
import fe_param_06.ivent02 as ivt02
import fe_param_06.ivent02a as ivt02a
import fe_param_06.ivent03 as ivt03
import fe_param_06.ivent03a as ivt03a
import fe_param_06.ivent04 as ivt04
import fe_param_06.ivent05 as ivt05
import fe_param_06.ivent06 as ivt06
import fe_param_06.ivent07 as ivt07
import fe_param_06.ivent07a as ivt07a
import fe_param_06.ivent08 as ivt08
import fe_param_06.ivent08a as ivt08a
import fe_param_06.ivent09 as ivt09
import fe_param_06.ivent09a as ivt09a
import fe_param_06.ivent10 as ivt10
import fe_param_06.ivent11 as ivt11
import fe_param_06.ivent12 as ivt12
import fe_param_06.ivent13 as ivt13
import fe_param_06.ivent14a as ivt14a
import fe_param_06.ivent15 as ivt15
import fe_param_06.ivent16 as ivt16

import fe_param_06.profile01 as prf01
import fe_param_06.profile01a as prf01a
import fe_param_06.profile02 as prf02
import fe_param_06.profile03 as prf03
import fe_param_06.profile03a as prf03a
import fe_param_06.profile04 as prf04
import fe_param_06.profile04a as prf04a

#import fe_param_05.battle01 as btl01

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
	
	fe_ivt02 = fe_ivent()
	fe_ivt02.configure(ivt02)
	fe_ivt02.run()
	
	fe.make_ivent(
		scene=ivt02.scene,
		title=ivt02.title,
	)
	
	fe_ivt02a = fe_ivent()
	fe_ivt02a.configure(ivt02a)
	fe_ivt02a.run()
	
	fe.make_ivent(
		scene=ivt02a.scene,
		title=ivt02a.title,
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
	fe_prf01a = fe_profile()
	fe_prf01a.configure(prf01a)
	fe_prf01a.run()
	
	# 編成
	fe.make_organization(
		field_map=fe_fld01.out_file,
		title=prf01a.title,
		organization=prf01a.organization,
	)
	
	# 会話イベント
	fe_ivt03 = fe_ivent()
	fe_ivt03.configure(ivt03)
	fe_ivt03.run()
	
	fe.make_ivent(
		scene=ivt03.scene,
		title=ivt03.title,
	)
	
	fe_ivt03a = fe_ivent()
	fe_ivt03a.configure(ivt03a)
	fe_ivt03a.run()
	
	fe.make_ivent(
		scene=ivt03a.scene,
		title=ivt03a.title,
	)
	
	# 戦闘
	fe_ivt04 = fe_ivent()
	fe_ivt04.configure(ivt04)
	fe_ivt04.run()
	
	fe.make_ivent(
		scene=ivt04.scene,
		title=ivt04.title,
	)
	
	# 制圧
	fe_ivt05 = fe_ivent()
	fe_ivt05.configure(ivt05)
	fe_ivt05.run()
	
	fe.make_ivent(
		scene=ivt05.scene,
		title=ivt05.title,
	)
	
	#
	# Phase2
	#
	# 導入
	fe_ivt06 = fe_ivent()
	fe_ivt06.configure(ivt06)
	fe_ivt06.run()
	
	fe.make_ivent(
		scene=ivt06.scene,
		title=ivt06.title,
	)
	
	fe_ivt07 = fe_ivent()
	fe_ivt07.configure(ivt07)
	fe_ivt07.run()
	
	fe.make_ivent(
		scene=ivt07.scene,
		title=ivt07.title,
	)
	
	fe_ivt07a = fe_ivent()
	fe_ivt07a.configure(ivt07a)
	fe_ivt07a.run()
	
	fe.make_ivent(
		scene=ivt07a.scene,
		title=ivt07a.title,
	)
	
	# フィールドマップ作成
	fe_fld02 = fe_field()
	fe_fld02.configure(fld02)
	fe_fld02.run()
	
	# 登場人物
	fe_prf03 = fe_profile()
	fe_prf03.configure(prf03)
	fe_prf03.run()
	
	# 編成
	fe.make_organization(
		field_map=fe_fld02.out_file,
		title=prf03.title,
		organization=prf03.organization,
	)
	
	# 登場人物
	fe_prf03a = fe_profile()
	fe_prf03a.configure(prf03a)
	fe_prf03a.run()
	
	# 編成
	fe.make_organization(
		field_map=fe_fld02.out_file,
		title=prf03a.title,
		organization=prf03a.organization,
	)
	
	fe_ivt09 = fe_ivent()
	fe_ivt09.configure(ivt09)
	fe_ivt09.run()
	
	fe.make_ivent(
		scene=ivt09.scene,
		title=ivt09.title,
	)
	
	fe_ivt09a = fe_ivent()
	fe_ivt09a.configure(ivt09a)
	fe_ivt09a.run()
	
	fe.make_ivent(
		scene=ivt09a.scene,
		title=ivt09a.title,
	)
	
	# 会話イベント
	fe_ivt08 = fe_ivent()
	fe_ivt08.configure(ivt08)
	fe_ivt08.run()
	
	fe.make_ivent(
		scene=ivt08.scene,
		title=ivt08.title,
	)
	
	fe_ivt08a = fe_ivent()
	fe_ivt08a.configure(ivt08a)
	fe_ivt08a.run()
	
	fe.make_ivent(
		scene=ivt08a.scene,
		title=ivt08a.title,
	)
	
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
	
	# 制圧
	fe_ivt12 = fe_ivent()
	fe_ivt12.configure(ivt12)
	fe_ivt12.run()
	
	fe.make_ivent(
		scene=ivt12.scene,
		title=ivt12.title,
	)
	
	#
	# Phase3
	#
	# 登場人物
	fe_prf04 = fe_profile()
	fe_prf04.configure(prf04)
	fe_prf04.run()
	
	# 編成
	fe.make_organization(
		field_map=fe_fld02.out_file,
		title=prf04.title,
		organization=prf04.organization,
	)
	
	# 登場人物
	fe_prf04a = fe_profile()
	fe_prf04a.configure(prf04a)
	fe_prf04a.run()
	
	# 編成
	fe.make_organization(
		field_map=fe_fld02.out_file,
		title=prf04a.title,
		organization=prf04a.organization,
	)
	
	# 会話イベント
	fe_ivt13 = fe_ivent()
	fe_ivt13.configure(ivt13)
	fe_ivt13.run()
	
	fe.make_ivent(
		scene=ivt13.scene,
		title=ivt13.title,
	)
	
	fe_ivt14a = fe_ivent()
	fe_ivt14a.configure(ivt14a)
	fe_ivt14a.run()
	
	fe.make_ivent(
		scene=ivt14a.scene,
		title=ivt14a.title,
	)
	
	# 戦闘
	fe_ivt15 = fe_ivent()
	fe_ivt15.configure(ivt15)
	fe_ivt15.run()
	
	fe.make_ivent(
		scene=ivt15.scene,
		title=ivt15.title,
	)
	
	# 制圧
	fe_ivt16 = fe_ivent()
	fe_ivt16.configure(ivt16)
	fe_ivt16.run()
	
	fe.make_ivent(
		scene=ivt16.scene,
		title=ivt16.title,
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
