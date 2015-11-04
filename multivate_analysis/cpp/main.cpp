#include <boost/python.hpp>
#include <boost/numpy.hpp>

#include "multivate.hpp"

namespace p = boost::python;
namespace np = boost::numpy;

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

// BOOST_PYTHON_MODULE(Python$B$N%b%8%e!<%kL>(B)
BOOST_PYTHON_MODULE(mymodule) {
	Py_Initialize();
	np::initialize();

	// def(Python$B$N4X?tL>(B, C++$B$N4X?tL>(B)
	p::def("mean", mean);
}
