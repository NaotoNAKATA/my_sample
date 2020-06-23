#!/usr/bin/python
# -*- coding: utf-8 -*-

from gimpfu import *
import os

from array import array

def my_sample1_func(input_filename, output_dirname):

    # 出力ディレクトリの作成
    if not os.path.exists(output_dirname):
        os.makedirs(output_dirname)

    # イメージのロード
    img = pdb.gimp_file_load(input_filename, u'')

    # クリップ
    pdb.gimp_image_crop(img, 160, 100, 30, 40)

    # 別名で保存する
    layer = img.layers[0]
    output_filename = output_dirname + u'/' + os.path.basename(input_filename)
    pdb.gimp_file_save(img, layer, output_filename, output_filename)

    # レイヤーを追加(よくわからないが、レイヤーとして再読み込みしてやってから追加する)
    layer_reload = pdb.gimp_file_load_layer(img, output_filename)
    img.add_layer(layer_reload, 0) # 0で一番上のレイヤー

    # レイヤーを一部塗りつぶし
    src = layer_reload.get_pixel_rgn(0, 0, layer_reload.width, layer_reload.height, False, False)
    dst = layer_reload.get_pixel_rgn(0, 0, layer_reload.width, layer_reload.height, True,  True)
    src_array = array('B', src[0:layer_reload.width, 0:layer_reload.height])
    dst_array = array('B', '\x00' * (layer_reload.width * layer_reload.height * layer_reload.bpp) )
    for y in range(layer_reload.height):
        for x in range(layer_reload.width):
            for b in range(layer_reload.bpp):
                idx = (y*layer_reload.width + x)*layer_reload.bpp + b
                if (y>=20 and y<=80) and (x>=30 and x<=100):
                    dst_array[idx] = 0
                else:
                    dst_array[idx] = src_array[idx]
    dst[0:layer_reload.width, 0:layer_reload.height] = dst_array.tostring()
    layer_reload.flush()
    layer_reload.merge_shadow(True)
    layer_reload.update(0, 0, layer_reload.width, layer_reload.height)

    # xcfで保存
    output_filename_xcf = output_dirname + u'/' + os.path.splitext(os.path.basename(input_filename))[0] + u'.xcf'
    pdb.gimp_xcf_save(0, img, layer, output_filename_xcf, output_filename_xcf)

    # レイヤーを統合して保存
    visibles = img.flatten() # 32bit->24bit
    output_filename_crop = output_dirname + u'/crop_' + os.path.basename(input_filename)
    pdb.gimp_file_save(img, visibles, output_filename_crop, output_filename_crop)

    gimp.delete(img)

    pdb.gimp_message(u'Finished')


register(
    u'my-sample1', # コマンドラインまたはスクリプトから呼び出す場合のコマンドの名前
    u'Explane this plug-in', # プラグインの説明
    u'Explane this plug-in detail', # プラグインの詳細な説明
    u'NaotoNAKATA1', # プラグインの作者
    u'NaotoNAKATA2', # プラグインの著作権保有者
    u'2020/6/11', # 著作権の日付
    u'MySample1', # メニューの中でプラグインに使用されるラベル
    u'RGB*, GRAY*', # プラグインで処理する対象となる画像のタイプ
    [
        (PF_FILE, u'InputFileName', 'Input File Name', u'.'),
        (PF_DIRNAME, u'OutputDirectoryName', 'Output Directory Name', u'.'),
    ], # 引数(型, 名前(プロージャーブラウザに表示される), 説明, 初期値)
    [], # 戻り値
    my_sample1_func,
    menu=u'<Image>/File') # ツールバーで表示される位置

main()
