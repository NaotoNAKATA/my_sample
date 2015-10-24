#include <iostream>
#include <vector>

#include "multivate.hpp"

float calc_mean(std::vector<float> x)
{
	float sum = 0;

	for(std::vector<float>::const_iterator iter=x.begin();
			iter!=x.end();
			iter++)
	{
		sum += *iter;
	}

	return sum / x.size();
}
