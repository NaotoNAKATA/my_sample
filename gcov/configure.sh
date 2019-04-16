#!/bin/bash

BUILD=build

if [ ! -e ${BUILD} ] ; then
	mkdir ${BUILD}
	cd ${BUILD}
	cmake -DCMAKE_BUILD_TYPE=Release ..
#	cmake -DCMAKE_BUILD_TYPE=Debug ..
else
	cd ${BUILD}
fi

make
