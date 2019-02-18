#ifndef _CLIBS_H_
#define _CLIBS_H_

// 静的リンク(同一のプロジェクト)
int aLib(const char* c);

// 動的リンク(同一のプロジェクト)
int bLib(const char* c);

// 静的リンク(別々のプロジェクト)
int cLib(const char* c);

// 動的リンク(別々のプロジェクト)
int dLib(const char* c);

#endif /* _CLIBS_H_ */

