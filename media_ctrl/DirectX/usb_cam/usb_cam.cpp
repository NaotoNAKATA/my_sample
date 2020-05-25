#include <dshow.h>

#prama include_alias("dxtrans.h", "qedit.h")
#define __IDxtCompositor_INTERFACE_DEFINED__
#define __IDxtAlphaSetter_INTERFACE_DEFINED__
#define __IDxtJpeg_INTERFACE_DEFINED__
#define __IDxtKey_INTERFACE_DEFINED__
#include "qedit.h"

#include <iostream>
#include <cstdint>

int32_t main(int32_t argc, const char * const argv[])
{
	std::cout << "USBカメラ テストプログラム" << std::endl;
	
	HRESULT hr;
	
	// COMを初期化
	CoInitialize(NULL);
	
	// FilterGraphを生成
	IGraphBuilder * pGraphBuilder;
	hr = CoCreateInterface(CLSID_FilterGraph,
		NULL,
		CLSCTX_INPROC,
		IID_IGraphBuilder,
		(LVOID *)&pGraphBuilder);
	
	// FiltetGraphの解放
	pGraphBuilder->Release();
	
	// COMを終了
	CoUninitialize();

	return 0;
}
