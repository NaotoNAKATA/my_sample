#include <iostream>
#include <fstream>
#include <string>

int main(int argc, const char *argv[])
{
#ifdef DEFINE_1
	std::cout << "DEFINE_1 is defined" << std::endl;
#endif

#ifdef DEFINE_2
	std::cout << "DEFINE_2 is defined" << std::endl;
#endif

	if(argc!=3)
	{
		std::cout << "Usage : [1] input , [2] output" << std::endl;
		return 0;
	}

	std::ifstream ifs;
	ifs.open(argv[1]);
	std::string cin;

	while(1)
	{
		ifs >> cin;
		if(ifs.eof())
			break;

		std::cout << cin << std::endl;
	}
	ifs.close();

	std::ofstream ofs(argv[2]);
	ofs << "Test output" << std::endl;

	return 0;
}

