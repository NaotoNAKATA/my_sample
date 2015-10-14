#include <iostream>
#include <vector>

#include "my_statics.hpp"

My_statics::My_statics() { }

My_statics::My_statics(std::vector<float> y, std::vector<float> x)
{
	copy(y.begin(), y.end(), back_inserter(_y) );
	copy(x.begin(), x.end(), back_inserter(_x) );
}

My_statics::~My_statics()
{ 
	_y.clear();
	_x.clear();
}

int My_statics::set_Y(std::vector<float> y)
{
	int num = 0;
	for(std::vector<float>::const_iterator iter=_y.begin();
			iter!=_y.end();
			iter++)
	{
		_y.push_back(*iter);
		num++;
	}

	return num;
}

int My_statics::set_X(std::vector<float> y)
{
	int num = 0;
	for(std::vector<float>::const_iterator iter=_x.begin();
			iter!=_x.end();
			iter++)
	{
		_x.push_back(*iter);
		num++;
	}

	return num;
}

int My_statics::process(void)
{
	if(_x.size()==0 || _y.size()==0 || _x.size()!=_y.size() ) {
		return 1;
	}
	_aveY = calc_ave(_y);
	_aveX = calc_ave(_x);

	_varY = calc_var(_y);
	_varX = calc_var(_x);

	_uvarY = calc_uvar(_y);
	_uvarX = calc_uvar(_x);

	_cov = calc_cov(_x, _y);

	_stdY = 0;
	_stdX = 0;

	return 0;
}

const float My_statics::calc_ave(std::vector<float> x)
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

const float My_statics::calc_var(std::vector<float> x)
{
	float sum = 0;
	float ave = calc_ave(x);

	for(std::vector<float>::const_iterator iter=x.begin();
			iter!=x.end();
			iter++)
	{
		sum += (*iter - ave);
	}

	return sum / x.size();
}

const float My_statics::calc_uvar(std::vector<float> x)
{
	float sum = 0;
	float ave = calc_ave(x);

	for(std::vector<float>::const_iterator iter=x.begin();
			iter!=x.end();
			iter++)
	{
		sum += (*iter - ave);
	}

	return sum / (x.size() - 1);
}

const float My_statics::calc_cov(std::vector<float> x, std::vector<float> y)
{
	float sum = 0;
	float ave_x = calc_ave(x);
	float ave_y = calc_ave(y);

	std::vector<float>::const_iterator iter_y=y.begin();
	std::vector<float>::const_iterator iter_x=x.begin();
	for(;
			iter_x!=x.end() && iter_y!=y.end();
			iter_x++, iter_y++)
	{
		sum += (*iter_x - ave_x) * (*iter_y - ave_y);
	}

	return sum / x.size();
}

