#include <iostream>
#include <fstream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

int main(int argc, const char *argv[])
{
//	cv::Mat img = cv::imread(argv[1],1);
//	cv::namedWindow("main", CV_WINDOW_AUTOSIZE);
//	cv::imshow("main", img);
//	std::string str="test.jpg";
//	cv::imwrite(str, img);
//	cv::waitKey(0);

	// solverテスト
	std::ifstream ifs("solverサンプルデータ.csv");
	int cnt = 0;
	cv::Mat x(201, 4, CV_64F);
	cv::Mat y(201, 1, CV_64F);
	cv::Mat ye(201, 1, CV_64F);
	while(1) {
		char line[1024];
		ifs.getline(line, 1024);
		if(ifs.eof())
			break;

		// 先頭はヘッダ行
		if(cnt==0) {
			cnt++;
			continue;
		}

		int _x;
		int _y;
		float _ye;
		sscanf(line,"%d,%d,%f\n", &_x, &_y, &_ye);

		x.at<double>(cnt, 0) = std::pow(_x, 3);
		x.at<double>(cnt, 1) = std::pow(_x, 2);
		x.at<double>(cnt, 2) = std::pow(_x, 1);
		x.at<double>(cnt, 3) = 1.0;
		y.at<double>(cnt, 0) = static_cast<double>(_y);
		ye.at<double>(cnt, 0) = static_cast<double>(_ye);
		cnt++;
	}

	cv::Mat coef_true;
	cv::solve(x, y, coef_true, cv::DECOMP_SVD);

	cv::Mat coef_with_err;
	cv::solve(x, ye, coef_with_err, cv::DECOMP_SVD);
	
	std::cout << "coef(ture)" << std::endl;
	std::cout << coef_true << std::endl;
	std::cout << "coef(err)" << std::endl;
	std::cout << coef_with_err << std::endl;

	return 0;
}

