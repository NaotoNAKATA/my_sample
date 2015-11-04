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

float calc_variance(std::vector<float> x)
{
	// $BJ?6Q$N7W;;(B
	float mean = calc_mean(x);

	float sum = 0;

#if 0
	// $BDj5A<0(B
	for(std::vector<float>::const_iterator iter=x.begin();
			iter!=x.end();
			iter++)
	{
		float sub = (*iter - mean);
		sum += sub * sub;
	}

	return sum / x.size();
#else
	// $B7W;;<0(B
	for(std::vector<float>::const_iterator iter=x.begin();
			iter!=x.end();
			iter++)
	{
		sum += *iter * *iter;
	}

	return (sum / x.size()) - (mean * mean);
#endif
}
