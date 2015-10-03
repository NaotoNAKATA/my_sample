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

const float My_statics::get_aveY(void)
{
	float sum = 0;
	for(std::vector<float>::const_iterator iter=_y.begin();
			iter!=_y.end();
			iter++)
	{
		sum += *iter;
	}

	return sum / _y.size();
}

const float My_statics::get_aveX(void)
{
	float sum = 0;
	for(std::vector<float>::const_iterator iter=_x.begin();
			iter!=_x.end();
			iter++)
	{
		sum += *iter;
	}

	return sum / _x.size();
}

const int My_statics::get_sizeY(void)
{
	return _y.size();
}

const int My_statics::get_sizeX(void)
{
	return _x.size();
}

