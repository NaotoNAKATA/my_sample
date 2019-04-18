#!/bin/sh

if [ ! -e ./build ] ; then
	mkdir ./build
	cd build
#	cmake .. -DCMAKE_PREFIX_PATH="../cpputest-3.8/build_Release" -DCMAKE_BUILD_TYPE=Release
	cmake .. -DCMAKE_PREFIX_PATH="../cpputest-3.8/build_Debug" -DCMAKE_BUILD_TYPE=Debug
	
else
	cd build
fi

make
