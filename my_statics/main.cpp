#include <iostream>
#include <vector>
#include "my_statics.hpp"

int main(int argc, const char *argv[])
{

	std::vector<float> y;
	std::vector<float> x;
	for(int i=0; i<10; i++)
	{
		y.push_back( (float)i );
		x.push_back( (float)(i+1) );
	}

	My_statics sta(y, x);
	std::cout << sta.get_aveY() << std::endl;
	std::cout << sta.get_aveX() << std::endl;

	return 0;
}

