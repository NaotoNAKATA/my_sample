#include <dshow.h>

#pragma include_alias("dxtrans.h", "qedit.h")
#define __IDxtCompositor_INTERFACE_DEFINED__
#define __IDxtAlphaSetter_INTERFACE_DEFINED__
#define __IDxtJpeg_INTERFACE_DEFINED__
#define __IDxtKey_INTERFACE_DEFINED__
#include "qedit.h"

#include <iostream>
#include <cstdint>

int32_t main(int32_t argc, const char * const argv[])
{
	std::cout << "USB�J���� �e�X�g�v���O����" << std::endl;
	
	HRESULT hr;
	
	// COM��������
	CoInitialize(NULL);
	
	// FilterGraph�𐶐�
	IGraphBuilder * pGraphBuilder;
	hr = CoCreateInstance(CLSID_FilterGraph,
		NULL,
		CLSCTX_INPROC,
		IID_IGraphBuilder,
		(LPVOID *)&pGraphBuilder);
	
	// FiltetGraph�����
	pGraphBuilder->Release();
	
	// COM���I��
	CoUninitialize();

	return 0;
}
