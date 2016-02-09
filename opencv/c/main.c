#include <stdio.h>
#include "cv.h"
#include "highgui.h"

int main(int argc, const char *argv[])
{
	IplImage *img = cvLoadImage(argv[1], CV_LOAD_IMAGE_ANYCOLOR | CV_LOAD_IMAGE_ANYDEPTH);
	cvNamedWindow("main", CV_WINDOW_AUTOSIZE);
	cvShowImage("main", img);
	cvWaitKey(0);
	cvDestroyWindow("lena");
	cvSaveImage("test.jpg",img, 95);
	cvReleaseImage(&img);

	return 0;
}

