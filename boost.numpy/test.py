# -*- coding: utf-8 -*-

import sys
import mymodule
import numpy as np

if __name__ == "__main__":
	param = sys.argv
	print "Hello:" + param[0]

	a = np.array([1,2,3], dtype=np.float64)
	mymodule.mult_two(a)
	print(a)

