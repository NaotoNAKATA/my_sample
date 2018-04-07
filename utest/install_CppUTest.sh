#!/bin/sh

# CppUTestのインストール。cpputest-3.8はutestと同じ階層に置いておく
cd ../cpputest-3.8

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

