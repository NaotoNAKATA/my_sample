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
	std::cout << "USBカメラ テストプログラム" << std::endl;
	
	HRESULT hr;
	
	//
	// COMを初期化
	//
	CoInitialize(NULL);
	
	//
	// FilterGraphを生成
	//
	IGraphBuilder * pGraphBuilder;
	hr = CoCreateInstance(
		CLSID_FilterGraph,
		NULL,
		CLSCTX_INPROC,
		IID_IGraphBuilder,
		(LPVOID *)&pGraphBuilder);
		
	//
	// キャプチャデバイスの取得
	//
	// デバイスを列挙するためのSystemDeviceEnumを生成
	ICreateDevEnum * pSysDevEnum;
	hr = CoCreateInstance(
		CLSID_SystemDeviceEnum,
		NULL,
		CLSCTX_INPROC_SERVER,
		IID_ICreateDevEnum,
		(LPVOID *)&pSysDevEnum);
	if( FAILD(hr) ) {
		return hr;
	}
	
	// ビデオコンプレッサカテゴリのクラス列挙子の取得
	IEnumMoniker * pEnumCat = NULL;
	hr = pSysDevEnum->CreateClassEnumerater(
		CLSID_VideoCompressorCategory,
		&pEnumCat,
		0);
	if( hr == S_OK ) {
		// 一応、リセットして先頭から数えなおす
		pEnumCat->Reset();
		
		// モニカを列挙する
		IMoniker * pMoniker = NULL;
		ULONG cFetched;
		while(pEnumCat->Next(1, &pMoniker, &cFetched) == S_OK )
		{
			// IPropertyBagにBind
			IPropertyBag * pPropertyBag;
			hr = pMoniker->BindToStogare(
				0,
				0,
				IID_PropertyBag,
				(LPVOID *)&pPropertyBag);
			if( SUCCEEDED(hr) )
			{
				// フィルタのフレンドリー名を取得
				VARIANT var;
				VariantInit(&var);
				var.vt = VT_BSTR;
				hr = pPropertyBag->Read(
					L"FriendlyName",
					&var,
					0);
				if( SUCCEEDED(hr) )
				{
					// フレンドリー名の表示
					TCAR devname[256];
					WideCharToMultiByte(
						CP_ACP, 0, var.bstrVal, -1,
						(LPSTR)devname, sizeof(devname),
						0, 0);
					printf("Device Name : %s\n", (LPSTR)devname);
				}
				VariantClear(&var);
				
				
				pPropertyBag->Release();
			}
			pMoniker->Release();
		}
		pEnumCat->Release();
	}
	pDevEnum->Release();
	
	//
	// FiltetGraphを解放
	//
	pGraphBuilder->Release();
	
	//
	// COMを終了
	//
	CoUninitialize();

	return 0;
}
