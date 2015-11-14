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

float calc_covariance(std::vector<float> x, std::vector<float> y)
{
	// 平均の計算
	float mean_x = calc_mean(x);
	float mean_y = calc_mean(y);

	float sum = 0;

#if 1
	// 定義式
	std::vector<float>::const_iterator iter_y = y.begin();
	for(std::vector<float>::const_iterator iter_x=x.begin();
			iter_x!=x.end() && iter_y!=y.end();
			iter_x++, iter_y++)
	{
		sum += (*iter_x - mean_x) * (*iter_y - mean_y);
	}

	return sum / x.size();
#else
	// 計算式
	std::vector<float>::const_iterator iter_y = y.begin();
	for(std::vector<float>::const_iterator iter_x=x.begin();
			iter_x!=x.end() && iter_y!=y.end();
			iter_x++, iter_y++)
	{
		sum += *iter_x * *iter_y;
	}

	return (sum / x.size()) - (mean_x * mean_y);
#endif
}

float calc_u_variance(std::vector<float> x)
{
	// 平均の計算
	float mean = calc_mean(x);

	float sum = 0;

	for(std::vector<float>::const_iterator iter=x.begin();
			iter!=x.end();
			iter++)
	{
		float sub = (*iter - mean);
		sum += sub * sub;
	}

	return sum / (x.size() - 1);
}
