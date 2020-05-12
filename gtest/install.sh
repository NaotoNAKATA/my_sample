#!/bin/bash

VER=1.10.0
#wget https://github.com/googletest/archive/release-${VER}.zip

#unzip googletest-release-${VER}.zip
cd googletest-release-${VER}

BUILD=build
mkdir ${BUILD}
cd ${BUILD}
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=../../gtest

make && make install
