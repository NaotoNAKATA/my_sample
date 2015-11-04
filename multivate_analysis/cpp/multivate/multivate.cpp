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
	// 平均の計算
	float mean = calc_mean(x);

	float sum = 0;

#if 0
	// 定義式
	for(std::vector<float>::const_iterator iter=x.begin();
			iter!=x.end();
			iter++)
	{
		float sub = (*iter - mean);
		sum += sub * sub;
	}

	return sum / x.size();
#else
	// 計算式
	for(std::vector<float>::const_iterator iter=x.begin();
			iter!=x.end();
			iter++)
	{
		sum += *iter * *iter;
	}

	return (sum / x.size()) - (mean * mean);
#endif
}
