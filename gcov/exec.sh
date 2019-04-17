#!/bin/bash

BUILD=build
OBJ=main
OBJ_SRC=main.cpp

# Execute object
cd ${BUILD}
./${OBJ}

# Coverage
cd CMakeFiles/${OBJ}.dir/
gcov -l -p ${OBJ_SRC}.gcda | grep ${OBJ_SRC} -B1
