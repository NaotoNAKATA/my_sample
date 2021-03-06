#ifndef _MULTIVATE_HPP_
#define _MULTIVATE_HPP_

#include <vector>

extern float calc_mean(std::vector<float> x);
extern float calc_variance(std::vector<float> x);
extern float calc_covariance(std::vector<float> x, std::vector<float> y);
extern float calc_u_variance(std::vector<float> x);

#endif /* _MULTIVATE_HPP_ */

