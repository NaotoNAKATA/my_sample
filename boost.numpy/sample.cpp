#include <boost/python.hpp>
#include <boost/numpy.hpp>

namespace p = boost::python;
namespace np = boost::numpy;

void mult_x2(np::ndarray a) {
	int nd = a.get_nd();
	if (nd != 1)
		throw std::runtime_error("a must be 1-dimensional");

	size_t N = a.shape(0);
	double *p = reinterpret_cast<double *>(a.get_data());
	if (a.get_dtype() != np::dtype::get_builtin<double>())
		throw std::runtime_error("a must be float64 array");

	std::transform(p, p + N, p, [](double x) { return 2 * x; });
}

// BOOST_PYTHON_MODULE(Pythonのモジュール名)
BOOST_PYTHON_MODULE(mymodule) {
	Py_Initialize();
	np::initialize();

	// def(Pythonの関数名, C++の関数名)
	p::def("mult_two", mult_x2);
}
