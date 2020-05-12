#include "gtest/gtest.h"

class TestClass01 : public ::testing::Test {
	
	// 各テストの直前に呼ばれる
	virtual void SetUp() {
	}
	
	// 各テストの直後に呼ばれる
	virtual void TearDown() {
	}
};

TEST_F(TestClass01, TestCase01)
{
	EXPECT_FLOAT_EQ(0.0f, 0.0f);
}
