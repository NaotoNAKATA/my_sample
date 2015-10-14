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
		int process(void);
		const float get_aveY(void){ return _aveY; }
		const float get_aveX(void){ return _aveX; }
		const int get_sizeY(void){ return _y.size(); }
		const int get_sizeX(void){ return _x.size(); }
		const float get_varY(void){ return _varX; }
		const float get_varX(void){ return _varY; }
		const float get_uvarY(void){ return _uvarX; }
		const float get_uvarX(void){ return _uvarY; }
		const float get_cov(void){ return _cov; }
		const float get_stdX(void){ return _stdX; }
		const float get_stdY(void){ return _stdY; }

	private:
		const float calc_ave(std::vector<float> x);
		const float calc_var(std::vector<float> x);
		const float calc_uvar(std::vector<float> x);
		const float calc_cov(std::vector<float> x, std::vector<float> y);

	private:
		std::vector<float> _y;
		std::vector<float> _x;
		float _aveX;
		float _aveY;
		float _varX;
		float _varY;
		float _uvarX;
		float _uvarY;
		float _cov;
		float _stdX;
		float _stdY;
};

#endif /* _MY_STATICS_HPP_ */

