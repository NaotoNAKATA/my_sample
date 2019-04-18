CMAKE_MINIMUM_REQUIRED(VERSION 2.6)
ADD_LIBRARY(fnc STATIC Fnc.cpp)

ADD_EXECUTABLE(utest
    FncTest.cpp
    utest.cpp
    Fnc.cpp
    )
TARGET_LINK_LIBRARIES(utest ${CppUTest_LIBRARIES})
