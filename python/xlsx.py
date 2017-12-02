# -*- coding: utf-8 -*-

import sys

import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell
from xlsxwriter.utility import xl_range

import xlrd

if __name__ == "__main__":
	
	# 
	# エクセルファイルの新規作成
	# 
	excelFileName = 'サンプル.xlsx'
	book = xlsxwriter.Workbook(excelFileName)

	# シートの作成
	sheetName = 'テストシート'
	sheet = book.add_worksheet(sheetName)

	# セルの書式設定
	format1 = book.add_format({'bold': True, 'pattern':1, 'bg_color':'#FFCCFF', 'border':2})

	# セルに値を書き込む
	sheet.write(0, 0, 'タイトル', format1)

	# セルに数式を書き込む
	sheet.write(1, 0, 2)
	sheet.write(2, 0, 3)
	sheet.write_formula(3, 0, 'SUM({0})'.format(xl_range(1, 0, 2, 0)))

	# セルへの文字列の取得
	sheet.write(5, 0, 'このセル')
	sheet.write(6, 0, xl_rowcol_to_cell(5, 0))

	# グラフの挿入
	sheet.write(0, 3, 'x')
	sheet.write(0, 4, 'x^2')
	sheet.write(0, 5, 'x^3')
	for i in range(10):
		sheet.write(i+1, 3, i)
		sheet.write(i+1, 4, i**2)
		sheet.write(i+1, 5, i**3)
	chart = book.add_chart({'type':'scatter'})
	chart.add_series({
		'name':'y=x^2',
		'categories':[sheet.name, 1, 3, 10, 3 ],
		'values':[sheet.name, 1, 4, 10, 4 ],
		'line':{'dash_type':'solid'},
		})
	chart.add_series({
		'name':[sheet.name, 0, 5],
		'categories':[sheet.name, 1, 3, 10, 3 ],
		'values':[sheet.name, 1, 5, 10, 5 ],
		'line':{'dash_type':'solid'},
		})
	chart.set_title({'name':'y=x^n'})
	chart.set_x_axis({'min':-1, 'max':15})
	chart.set_y_axis({'log_base':10, 'major_gridlines':{'visible':True},})
	sheet.insert_chart(xl_rowcol_to_cell(0, 6), chart, { 'x_offset': 0, 'y_offset': 0, 'x_scale':  1, 'y_scale':  1, })

	# エクセルファイルの保存
	book.close()

	# 
	# エクセルファイルの読み込み
	# 
	book = xlrd.open_workbook(excelFileName)

	# 読み込んだ結果をテキストで出力する
	with open('エクセル結果.txt', 'w') as f:
		for name in book.sheet_names():
			f.write('{0}\n'.format(name))

			# シートの取得
			sheet = book.sheet_by_name(name)
			f.write('rows={0}, cols={1}\n'.format(sheet.nrows,sheet.ncols))

			f.write('{0} = {1}\n'.format(xl_rowcol_to_cell(0,0), sheet.cell(0,0).value))

