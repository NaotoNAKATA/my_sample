#!/bin/sh

# CppUTestのインストール。cpputest-3.8は同じ階層に置いておく
#wget https://github.com/cpputest/cpputest/releases/download/v3.8/cpputest-3.8.tar.gz
#tar zxvf cpputest-3.8.tar.gz
cd cpputest-3.8

mkdir build_Debug
cd build_Debug
cmake -DCMAKE_INSTALL_PREFIX=./install -DTESTS=OFF -DCOVERAGE=ON ..
make
make install

cd ..

mkdir build_Release
cd build_Release
cmake -DCMAKE_INSTALL_PREFIX=./install -DTESTS=OFF ..
make
make install

