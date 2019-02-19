#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "aLib.h"

int aLib(const char* c) {
	printf("%s:%s\n",__FILE__,c);

	return 0;
}

// aLib API
// 初期化
tALIB * aLibInitialize(void)
{
	tALIB * a = (tALIB *)malloc(sizeof(tALIB));
	a->status = ALIB_STATUS_INIT;
	a->name = (char *)malloc(sizeof(char)*ALIB_NAME_LEN);

	return a;
}

int aLibSetStatus(ALIB_STATUS sta, tALIB * a)
{
	a->status = sta;

	return 0;
}
int aLibSetName(const char * name, tALIB * a)
{
	strcpy(a->name, name);

	return 0;
}

ALIB_STATUS aLibGetStatus(const tALIB * a)
{
	return a->status;
}

int aLibGetName(const tALIB * a, char * name)
{
	strcpy(name, a->name);

	return 0;
}

int aLibGetNameLen(void)
{
	return ALIB_NAME_LEN;
}

int aLibTerminate(tALIB * a)
{
	free(a->name);
	free(a);

	return 0;
}