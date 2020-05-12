CMAKE_MINIMUM_REQUIRED(VERSION 3.0)
PROJECT(gtest_sample)

FIND_PACKAGE( GTest REQUIRED )

ADD_EXECUTABLE(gtest_sample gtest_sample.cpp)
TARGET_LINK_LIBRARIES( gtest_sample
	PRIVATE
	GTest::GTest
	GTest::Main
)
