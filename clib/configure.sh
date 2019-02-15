#!/bin/bash

BUILD=build

if [ ! -e ${BUILD} ] ; then
	mkdir ${BUILD}
	cd ${BUILD}
	cmake ..
else
	cd ${BUILD}
fi

make

