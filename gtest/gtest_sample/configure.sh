#!/bin/bash

BUILD=build

if [ ! -e ${BUILD} ] ; then
	mkdir ${BUILD}
	cd ${BUILD}
	cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=../../gtest
else
	cd ${BUILD}
fi

make
