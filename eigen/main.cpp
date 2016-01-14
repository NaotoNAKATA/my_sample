#include <iostream>
#include <Eigen/Core>
#include <Eigen/Geometry>

using namespace Eigen;

int main(int argc, const char *argv[])
{
	Vector3f v = Vector3f::Zero();

	std::cout << "v = " << std::endl
		<< v << std::endl;

	int n = 15;
	VectorXf v1(n);
	for(int i=0;i<n;i++){
		v1[i] = i;
	}
	std::cout << "v1 = " << std::endl
		<< v1 << std::endl;

	Matrix3d m;

	m << 1.0, 0.0, 0.0,
	  0.0, 1.0, 0.0,
	  0.0, 0.0, 1.0;

	std::cout << "m = " << std::endl
		<< m << std::endl;

	return 0;
}

