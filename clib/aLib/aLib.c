#include <stdio.h>

int aLib(const char* c) {
	printf("%s:%s\n",__FILE__,c);

	return 0;
}

