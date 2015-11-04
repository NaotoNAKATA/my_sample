# -*- coding: utf-8 -*-

import sys
import xlrd
import numpy as np
import matplotlib.pyplot as plt

import mymodule

if __name__ == "__main__":

	# ファイルのオープン
	book = xlrd.open_workbook('sample.xls')

	# シートの選択
	sheet = book.sheet_by_name(u"Sheet1")
#	sheet = book.sheet_by_index(0)

	plot_x = np.zeros(sheet.nrows-1, dtype=np.float64)
	plot_y = np.zeros(sheet.nrows-1, dtype=np.float64)

	for row in range(sheet.nrows):
		if row==0:
			plt.xlabel(sheet.cell(0,1).value)
			plt.ylabel(sheet.cell(0,2).value)
			pass
		elif row>=1:
			plot_x[row-1] = float(sheet.cell(row,1).value)
			plot_y[row-1] = float(sheet.cell(row,2).value)
			
	print "mean(x) = " + str(mymodule.mean(plot_x))
	print "mean(y) = " + str(mymodule.mean(plot_y))
	print "variance(x) = " + str(mymodule.variance(plot_x))
	print "variance(y) = " + str(mymodule.variance(plot_y))
	print "co-variance(x,y) = " + str(mymodule.covariance(plot_x,plot_y))
	
	plt.xlim([0,100])
	plt.ylim([0,50])
	plt.plot(plot_x, plot_y,'o',color='r', label='test1')
	plt.title(u'title')
	plt.legend(loc='lower right') # 凡例表示
	plt.show()



