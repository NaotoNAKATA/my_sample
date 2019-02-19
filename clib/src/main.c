#include <stdio.h>
#include "clibs.h"

int main(int argc, const char *argv[])
{
	printf("Hello\n");
	aLib("静的リンク(同一のプロジェクト)");
	bLib("動的リンク(同一のプロジェクト)");
	cLib("静的リンク(別々のプロジェクト)");
	dLib("動的リンク(別々のプロジェクト)");

	return 0;
}
