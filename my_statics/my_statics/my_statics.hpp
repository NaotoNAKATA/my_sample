#ifndef _MY_STATICS_HPP_
#define _MY_STATICS_HPP_

#include <iostream>
#include <vector>

class My_statics
{
	public:
		My_statics();
		My_statics(std::vector<float> y, std::vector<float> x);
		~My_statics();
		int set_Y(std::vector<float> y);
		int set_X(std::vector<float> x);
		const float get_aveY(void);
		const float get_aveX(void);
		const int get_sizeY(void);
		const int get_sizeX(void);

	private:
		std::vector<float> _y;
		std::vector<float> _x;
};

#endif /* _MY_STATICS_HPP_ */

