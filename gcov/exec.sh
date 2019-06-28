#!/bin/bash

BUILD=build
OBJ=main
OBJ_SRC=main.cpp

# Execute object
cd ${BUILD}
./${OBJ}

# Coverage
cd CMakeFiles/${OBJ}.dir/
gcov -b -l -p ${OBJ_SRC}.gcda

# Lcov
lcov -c -d ./ -o ${OBJ}.info
genhtml ${OBJ}.info -o html --legend
