#include <stdio.h>
#include "clibs.h"
#include "aLib_ext.h"

int main(int argc, const char *argv[])
{
	printf("Hello\n");
	aLib("静的リンク(同一のプロジェクト)");
	bLib("動的リンク(同一のプロジェクト)");
	cLib("静的リンク(別々のプロジェクト)");
	dLib("動的リンク(別々のプロジェクト)");

	// aLib API
	tALIB * a = aLibInitialize();
	aLibTerminate(a);

	return 0;
}
