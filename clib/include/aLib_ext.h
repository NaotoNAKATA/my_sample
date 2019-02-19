#ifndef _ALIB_EXT_H_
#define _ALIB_EXT_H_

// 構造体を前方宣言。中身は隠蔽
struct stALIB;
typedef struct stALIB tALIB;

// ステータス
typedef enum {
	ALIB_STATUS_INIT = 0,
	ALIB_STATUS_SET,
	ALIB_ERROR
} ALIB_STATUS;

// APIで操作する
tALIB * aLibInitialize(void);
int aLibSetStatus(ALIB_STATUS sta, tALIB * a);
int aLibSetName(const char * name, tALIB * a);
ALIB_STATUS aLibGetStatus(const tALIB * a);
int aLibGetName(const tALIB * a, char * name);
int aLibGetNameLen(void);
int aLibTerminate(tALIB * a);

#endif /* _ALIB_EXT_H_ */