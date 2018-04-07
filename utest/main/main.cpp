#include <stdio.h>

#include "Fnc.h"

int main(int argc, const char *argv[])
{
	printf("use fnc\n");
	int a = 10;
	int b = 5;
	printf("Fnc(%d, %d) = %d\n", a, b, Fnc(a,b));

	return 0;
}

