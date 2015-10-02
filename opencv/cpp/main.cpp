#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

int main(int argc, const char *argv[])
{
	cv::Mat img = cv::imread(argv[1],1);
	cv::namedWindow("main", CV_WINDOW_AUTOSIZE);
	cv::imshow("main", img);
	cv::waitKey(0);

	return 0;
}

