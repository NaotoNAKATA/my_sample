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
	if( FAILED(hr) ) {
		return hr;
	}
	
	// デバイスフィルタ
	IBaseFilter * pVideoInput = NULL;
	IBaseFilter * pAudioInput = NULL;
	IBaseFilter * pVideoComp = NULL;
	IBaseFilter * pAudioComp = NULL;
	const int videoInputNo = 0;
	const int audioInputNo = 0;
	const int videoCompNo = 4;
	const int audioCompNo = 0;

	// ビデオ入力デバイスカテゴリのクラス列挙子の取得
	IEnumMoniker * pEnumCat = NULL;
	
	std::cout << "Video Input Device" << std::endl;
	
	hr = pSysDevEnum->CreateClassEnumerator(
		CLSID_VideoInputDeviceCategory,
		&pEnumCat,
		0);
	if( hr == S_OK ) {
		// 一応、リセットして先頭から数えなおす
		pEnumCat->Reset();
		
		// モニカを列挙する
		IMoniker * pMoniker = NULL;
		ULONG cFetched;
		int i = 0;
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
					if(i==videoInputNo) {
						printf(" * ");
					}
					else {
						printf("   ");
					}
					printf("%s\n", (LPSTR)devname);
					//printf("%ls\n", var.bstrVal);
				}
				VariantClear(&var);
				pPropertyBag->Release();
			}
			
			if(i==videoInputNo) {
				// モニカをフィルタにbind
				pMoniker->BindToObject(
					0, 0,
					IID_IBaseFilter,
					(LPVOID *)&pVideoInput);
					
				// フィルタをグラフに追加
				pGraphBuilder->AddFilter(
					pVideoInput,
					L"Video Device");
			}
			pMoniker->Release();
			i++;
		}
		pEnumCat->Release();
	}
	
	std::cout << "Audio Input Device" << std::endl;
	
	hr = pSysDevEnum->CreateClassEnumerator(
		CLSID_AudioInputDeviceCategory,
		&pEnumCat,
		0);
	if( hr == S_OK ) {
		// 一応、リセットして先頭から数えなおす
		pEnumCat->Reset();
		
		// モニカを列挙する
		IMoniker * pMoniker = NULL;
		ULONG cFetched;
		int i = 0;
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
					if(i==audioInputNo) {
						printf(" * ");
					}
					else {
						printf("   ");
					}
					printf("%s\n", (LPSTR)devname);
					//printf("%ls\n", var.bstrVal);
				}
				VariantClear(&var);
				pPropertyBag->Release();
			}
			
			if(i==audioInputNo) {
				// モニカをフィルタにbind
				pMoniker->BindToObject(
					0, 0,
					IID_IBaseFilter,
					(LPVOID *)&pAudioInput);
					
				// フィルタをグラフに追加
				pGraphBuilder->AddFilter(
					pAudioInput,
					L"Audio Device");
			}
			pMoniker->Release();
			i++;
		}
		pEnumCat->Release();
	}
	
	std::cout << "Video Compressor" << std::endl;
	
	hr = pSysDevEnum->CreateClassEnumerator(
		CLSID_VideoCompressorCategory,
		&pEnumCat,
		0);
	if( hr == S_OK ) {
		// 一応、リセットして先頭から数えなおす
		pEnumCat->Reset();
		
		// モニカを列挙する
		IMoniker * pMoniker = NULL;
		ULONG cFetched;
		int i = 0;
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
					if(i==videoCompNo) {
						printf(" * ");
					}
					else {
						printf("   ");
					}
					printf("%s\n", (LPSTR)devname);
					//printf("%ls\n", var.bstrVal);
				}
				VariantClear(&var);
				pPropertyBag->Release();
			}
			
			if(i==videoCompNo) {
				// モニカをフィルタにbind
				pMoniker->BindToObject(
					0, 0,
					IID_IBaseFilter,
					(LPVOID *)&pVideoComp);
					
				// フィルタをグラフに追加
				pGraphBuilder->AddFilter(
					pVideoComp,
					L"Video Compressor");
			}
			pMoniker->Release();
			i++;
		}
		pEnumCat->Release();
	}
	
	std::cout << "Audio Compressor" << std::endl;

	hr = pSysDevEnum->CreateClassEnumerator(
		CLSID_AudioCompressorCategory,
		&pEnumCat,
		0);
	if (hr == S_OK) {
		// 一応、リセットして先頭から数えなおす
		pEnumCat->Reset();

		// モニカを列挙する
		IMoniker * pMoniker = NULL;
		ULONG cFetched;
		int i = 0;
		while (pEnumCat->Next(1, &pMoniker, &cFetched) == S_OK)
		{
			// IPropertyBagにBind
			IPropertyBag * pPropertyBag;
			hr = pMoniker->BindToStorage(
				0,
				0,
				IID_IPropertyBag,
				(LPVOID *)&pPropertyBag);
			if (SUCCEEDED(hr))
			{
				// フィルタのフレンドリー名を取得
				VARIANT var;
				VariantInit(&var);
				var.vt = VT_BSTR;
				hr = pPropertyBag->Read(
					L"FriendlyName",
					&var,
					0);
				if (SUCCEEDED(hr))
				{
					// フレンドリー名の表示
					TCHAR devname[256];
					WideCharToMultiByte(
						CP_ACP, 0, var.bstrVal, -1,
						(LPSTR)devname, sizeof(devname),
						0, 0);
					if (i == audioCompNo) {
						printf(" * ");
					}
					else {
						printf("   ");
					}
					printf("%s\n", (LPSTR)devname);
					//printf("%ls\n", var.bstrVal);
				}
				VariantClear(&var);
				pPropertyBag->Release();
			}

			if (i == audioCompNo) {
				// モニカをフィルタにbind
				pMoniker->BindToObject(
					0, 0,
					IID_IBaseFilter,
					(LPVOID *)&pAudioComp);

				// フィルタをグラフに追加
				pGraphBuilder->AddFilter(
					pAudioComp,
					L"Audio Compressor");
			}
			pMoniker->Release();
			i++;
		}
		pEnumCat->Release();
	}

	pSysDevEnum->Release();
	
	//
	// 画角の取得
	//
	IEnumPins * pEnumPins = NULL;
	hr = pVideoInput->EnumPins(&pEnumPins);

	IPin *pCameraOutPin = NULL;
	hr = pEnumPins->Next(1, &pCameraOutPin, NULL);

	IAMStreamConfig *pAMSConfig = NULL;
	hr = pCameraOutPin->QueryInterface(IID_IAMStreamConfig, (LPVOID *)&pAMSConfig);

	int iCount = 0;
	int iSize = 0;
	pAMSConfig->GetNumberOfCapabilities(&iCount, &iSize);

	std::cout << "Size , fps" << std::endl;
	for (int i = 0; i < iCount; i++) {
		AM_MEDIA_TYPE * pmt = NULL;
		VIDEO_STREAM_CONFIG_CAPS vscc;
		hr = pAMSConfig->GetStreamCaps(i, &pmt, reinterpret_cast<BYTE*>(&vscc));

		if (pmt->majortype == MEDIATYPE_Video && pmt->formattype == FORMAT_VideoInfo &&
			pmt->cbFormat >= sizeof(VIDEOINFOHEADER) && pmt->pbFormat != NULL) {
			VIDEOINFOHEADER *pVih = (VIDEOINFOHEADER*)pmt->pbFormat;
			double fps = 1.0 / (double(pVih->AvgTimePerFrame) * 100.0*1.0e-9);

			printf("%4d x %4d : %5.1ffps\n", pVih->bmiHeader.biWidth, pVih->bmiHeader.biHeight, fps);

//			if (pVih->bmiHeader.biWidth == 1920) {
//				pAMSConfig->SetFormat(pmt);
//				break;
//			}
		}
	}

	pAMSConfig->Release();
	pCameraOutPin->Release();
	pEnumPins->Release();

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
	
	// グラフを生成(プレビューの登録？)
//	pCaptureGraphBuilder2->RenderStream(
//		&PIN_CATEGORY_PREVIEW,
//		&MEDIATYPE_Video,
//		pVideoInput,
//		NULL, NULL);
				
	//
	// AVI出力
	//
//	IBaseFilter * pMux = NULL;
//	pCaptureGraphBuilder2->SetOutputFileName(&MEDIASUBTYPE_Avi, L".\\test.avi", &pMux, NULL);
//	pCaptureGraphBuilder2->RenderStream(&PIN_CATEGORY_CAPTURE, &MEDIATYPE_Video, pVideoInput, pVideoComp, pMux);
//	pCaptureGraphBuilder2->RenderStream(&PIN_CATEGORY_CAPTURE, &MEDIATYPE_Audio, pAudioInput, NULL, pMux);
 
	//
	// メディアコントロールの取得
	//
	IMediaControl * pMediaControl;
	pGraphBuilder->QueryInterface(
		IID_IMediaControl,
		(LPVOID *)&pMediaControl);
		
	// 再生開始
	pMediaControl->Run();
	
	// OKで終了
	MessageBox(NULL,
		L"OKで終了",
		L"再生中",
		MB_OK);
	
	//
	// FilterGraphを解放
	//
//	pMux->Release();
	pVideoInput->Release();
	pAudioInput->Release();
	pVideoComp->Release();
	pMediaControl->Release();
	pCaptureGraphBuilder2->Release();
	pGraphBuilder->Release();
	
	//
	// COMを終了
	//
	CoUninitialize();

	return 0;
}
