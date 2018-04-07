#include "Cls.h"

//CppUTest includes should be after your and system includes
#include "CppUTest/TestHarness.h"

TEST_GROUP(Cls)
{
  Cls* cls;

  void setup()
  {
    cls = new Cls();
  }
  void teardown()
  {
    delete cls;
  }
};

TEST(Cls, Create)
{
  FAIL("Start here");
}

