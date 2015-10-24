#!/bin/sh

cpp_src=./cpp
python_src=./python
lib_name=mymodule.so
build_dir=./build

if [ ! -e ${build_dir} ] ; then
	mkdir ${build_dir}
fi

cd ${build_dir}
cmake ../${cpp_src}
make
cd ../${python_src}

if [ -f ${lib_name} ] ; then
	rm ${lib_name}
fi
ln -s ../${build_dir}/${lib_name} ${lib_name}

python main.py

cd ..

