#include <boost/python.hpp>
#include <boost/numpy.hpp>

#include <cmath>

#include "multivate.hpp"

namespace p = boost::python;
namespace np = boost::numpy;

/************************************************/
/* 平均値                                       */
/************************************************/
float mean(np::ndarray a) {
	int nd = a.get_nd();
	if (nd != 1)
		throw std::runtime_error("a must be 1-dimensional");

	if (a.get_dtype() != np::dtype::get_builtin<double>())
		throw std::runtime_error("a must be float64 array");
	
	size_t N = a.shape(0);
	double *p = reinterpret_cast<double *>(a.get_data());
	std::vector<float> x;
	for(int i=0;i<N;i++) x.push_back(*p++);

	return calc_mean(x);
}

/************************************************/
/* 分散                                         */
/************************************************/
float variance(np::ndarray a) {
	int nd = a.get_nd();
	if (nd != 1)
		throw std::runtime_error("a must be 1-dimensional");

	if (a.get_dtype() != np::dtype::get_builtin<double>())
		throw std::runtime_error("a must be float64 array");

	size_t N = a.shape(0);
	double *p = reinterpret_cast<double *>(a.get_data());
	std::vector<float> x;
	for(int i=0;i<N;i++) x.push_back(*p++);

	return calc_variance(x);
}

/************************************************/
/* 共分散                                       */
/************************************************/
float covariance(np::ndarray a, np::ndarray b) {
	int nd1 = a.get_nd();
	int nd2 = b.get_nd();
	if (nd1 != 1 || nd2 != 1)
		throw std::runtime_error("a and b must be 1-dimensional");

	if ( (a.get_dtype() != np::dtype::get_builtin<double>()) ||
			(b.get_dtype() != np::dtype::get_builtin<double>()) )
		throw std::runtime_error("a and b must be float64 array");

	size_t N = a.shape(0);
	if ( N != b.shape(0) )
		throw std::runtime_error(" a and b must be same size");

	double *p = reinterpret_cast<double *>(a.get_data());
	std::vector<float> x;
	for(int i=0;i<N;i++) x.push_back(*p++);

	double *q = reinterpret_cast<double *>(b.get_data());
	std::vector<float> y;
	for(int i=0;i<N;i++) y.push_back(*q++);

	return calc_covariance(x,y);
}

/************************************************/
/* 不偏分散                                     */
/************************************************/
float u_variance(np::ndarray a) {
	int nd = a.get_nd();
	if (nd != 1)
		throw std::runtime_error("a must be 1-dimensional");

	if (a.get_dtype() != np::dtype::get_builtin<double>())
		throw std::runtime_error("a must be float64 array");

	size_t N = a.shape(0);
	double *p = reinterpret_cast<double *>(a.get_data());
	std::vector<float> x;
	for(int i=0;i<N;i++) x.push_back(*p++);

	return calc_u_variance(x);
}

/************************************************/
/* 回帰系数                                     */
/************************************************/
float simple_liner_regression(np::ndarray a, np::ndarray b, np::ndarray c) {
	int nd1 = a.get_nd();
	int nd2 = b.get_nd();
	if (nd1 != 1 || nd2 != 1)
		throw std::runtime_error("a and b must be 1-dimensional");

	if ( (a.get_dtype() != np::dtype::get_builtin<double>()) ||
			(b.get_dtype() != np::dtype::get_builtin<double>()) )
		throw std::runtime_error("a and b must be float64 array");

	size_t N = a.shape(0);
	if ( N != b.shape(0) )
		throw std::runtime_error(" a and b must be same size");

	double *p = reinterpret_cast<double *>(a.get_data());
	std::vector<float> x;
	for(int i=0;i<N;i++) x.push_back(*p++);

	double *q = reinterpret_cast<double *>(b.get_data());
	std::vector<float> y;
	for(int i=0;i<N;i++) y.push_back(*q++);

	// 回帰系数の計算
	float a1 = calc_covariance(x,y) / calc_variance(x);
	float a0 = calc_mean(y) - a1 * calc_mean(x);

	double *r = reinterpret_cast<double *>(c.get_data());
	*r = a0; r++;
	*r = a1;
}

/************************************************/
/* 相関系数                                     */
/************************************************/
float coefficient(np::ndarray a, np::ndarray b) {
	int nd1 = a.get_nd();
	int nd2 = b.get_nd();
	if (nd1 != 1 || nd2 != 1)
		throw std::runtime_error("a and b must be 1-dimensional");

	if ( (a.get_dtype() != np::dtype::get_builtin<double>()) ||
			(b.get_dtype() != np::dtype::get_builtin<double>()) )
		throw std::runtime_error("a and b must be float64 array");

	size_t N = a.shape(0);
	if ( N != b.shape(0) )
		throw std::runtime_error(" a and b must be same size");

	double *p = reinterpret_cast<double *>(a.get_data());
	std::vector<float> x;
	for(int i=0;i<N;i++) x.push_back(*p++);

	double *q = reinterpret_cast<double *>(b.get_data());
	std::vector<float> y;
	for(int i=0;i<N;i++) y.push_back(*q++);

	return calc_covariance(x,y) / sqrt( calc_variance(x) * calc_variance(y) );
}

/************************************************/
/* Pythonとの連携                               */
/************************************************/
// BOOST_PYTHON_MODULE(Pythonのモジュール名)
BOOST_PYTHON_MODULE(mymodule) {
	Py_Initialize();
	np::initialize();

	// def(Pythonの関数名, C++の関数名)
	p::def("mean", mean);
	p::def("variance", variance);
	p::def("covariance", covariance);
	p::def("u_variance", u_variance);
	p::def("simple_liner_regression", simple_liner_regression);
	p::def("coefficient", coefficient);
}
