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
	// CaptureGraphBuilder2でフィルタグラフを構築する
	//
	ICaptureGraphBuilder2 * pCaptureGraphBuilder2;
	hr = CoCreateInstance(
		CLSID_CaptureGraphBuilder2,
		NULL,
		CLSCTX_INPROC,
		IID_ICaptureGraphBuilder2,
		(LPVOID *)&pCaptureGraphBuilder2);
	
	// フィルタグラフをセット
	pCaptureGraphBuilder2->SetFiltergraph(pGraphBuilder);
	
	//
	// メディアコントロールの取得
	//
	IMediaControl * pMediaControl;
	pGraphBuilder->QueryInterface(
		IID_IMediaControl,
		(LPVOID *)&pMediaControl);
	
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
	if( FAILED(hr) ) {
		return hr;
	}
	
	// デバイスフィルタ
	IBaseFilter * pDeviceFilter;
	
	// ビデオ入力デバイスカテゴリのクラス列挙子の取得
	IEnumMoniker * pEnumCat = NULL;
	hr = pSysDevEnum->CreateClassEnumerator(
		//CLSID_VideoCompressorCategory,
		CLSID_VideoInputDeviceCategory,
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
			hr = pMoniker->BindToStorage(
				0,
				0,
				IID_IPropertyBag,
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
					TCHAR devname[256];
					WideCharToMultiByte(
						CP_ACP, 0, var.bstrVal, -1,
						(LPSTR)devname, sizeof(devname),
						0, 0);
					printf("Device Name : %s\n", (LPSTR)devname);
				}
				VariantClear(&var);
				pPropertyBag->Release();
				}
			
			// モニカをフィルタにbind
			pMoniker->BindToObject(
				0, 0,
				IID_IBaseFilter,
				(LPVOID *)&pDeviceFilter);
				
			// フィルタをグラフに追加
			pGraphBuilder->AddFilter(
				pDeviceFilter,
				L"Device Filter");
				
			pMoniker->Release();
			
			// グラフを生成
			pCaptureGraphBuilder2->RenderStream(
				&PIN_CATEGORY_PREVIEW,
				NULL,
				pDeviceFilter,
				NULL, NULL);

			// (仮)最初に見つけたデバイスを使用する
			break;
		}
		pEnumCat->Release();
	}
	pSysDevEnum->Release();
	
	// 再生開始
	pMediaControl->Run();
	
	// OKで終了
	MessageBox(NULL,
		L"OKで終了",
		L"再生中",
		MB_OK);
	
	//
	// FiltetGraphを解放
	//
	pMediaControl->Release();
	pCaptureGraphBuilder2->Release();
	pGraphBuilder->Release();
	
	//
	// COMを終了
	//
	CoUninitialize();

	return 0;
}
