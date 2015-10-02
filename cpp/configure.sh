#!/bin/sh

if [ ! -e ./build ] ; then
	mkdir ./build
	cd build
	cmake ..
else
	cd build
fi

make && ./main.exe ../main.cpp ../out.txt
