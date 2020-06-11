#include <dshow.h>

#pragma include_alias("dxtrans.h", "qedit.h")
#define __IDxtCompositor_INTERFACE_DEFINED__
#define __IDxtAlphaSetter_INTERFACE_DEFINED__
#define __IDxtJpeg_INTERFACE_DEFINED__
#define __IDxtKey_INTERFACE_DEFINED__
#include "qedit.h"

#include <iostream>
#include <cstdint>


HRESULT system_device_enum(ICreateDevEnum * pSysDevEnum,
	const IID & CLSID)
{
	HRESULT hr;

	// ビデオ入力デバイスカテゴリのクラス列挙子の取得
	IEnumMoniker * pEnumCat = NULL;
	hr = pSysDevEnum->CreateClassEnumerator(CLSID, &pEnumCat, 0);
	if (hr == S_OK) {
		// 一応、リセットして先頭から数えなおす
		pEnumCat->Reset();

		// モニカを列挙する
		IMoniker * pMoniker = NULL;
		ULONG cFetched;
		int32_t i = 0;
		while (pEnumCat->Next(1, &pMoniker, &cFetched) == S_OK)
		{
			// IPropertyBagにBind
			IPropertyBag * pPropertyBag;
			hr = pMoniker->BindToStorage(0, 0, IID_IPropertyBag, (LPVOID *)&pPropertyBag);
			if (SUCCEEDED(hr))
			{
				// フィルタのフレンドリー名を取得
				VARIANT var;
				VariantInit(&var);
				var.vt = VT_BSTR;
				hr = pPropertyBag->Read(L"FriendlyName", &var, 0);
				if (SUCCEEDED(hr))
				{
					// フレンドリー名の表示
					TCHAR devname[256];
					WideCharToMultiByte(
						CP_ACP, 0, var.bstrVal, -1,
						(LPSTR)devname, sizeof(devname),
						0, 0);

					printf("   %s\n", (LPSTR)devname);
					//printf("%   ls\n", var.bstrVal);
				}
				VariantClear(&var);
				pPropertyBag->Release();
			}
			pMoniker->Release();
			i++;
		}
		pEnumCat->Release();
	}

	return hr;
}

int32_t main(int32_t argc, const char * const argv[])
{
	std::cout << "デバイスを列挙する" << std::endl;

	HRESULT hr;

	//
	// COMを初期化
	//
	CoInitialize(NULL);

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
	if (FAILED(hr)) {
		return hr;
	}

	// ビデオデバイスの取得
	std::cout << "Video Input Device" << std::endl;
	system_device_enum(pSysDevEnum, CLSID_VideoInputDeviceCategory);

	// オーディオデバイスの取得
	std::cout << "Audio Input Device" << std::endl;
	system_device_enum(pSysDevEnum, CLSID_AudioInputDeviceCategory);

	// ビデオコンプレッサーの取得
	std::cout << "Video Compressor" << std::endl;
	system_device_enum(pSysDevEnum, CLSID_VideoCompressorCategory);

	// オーディオコンプレッサーの取得
	std::cout << "Audio Compressor" << std::endl;
	system_device_enum(pSysDevEnum, CLSID_AudioCompressorCategory);

	// 解放
	pSysDevEnum->Release();

	//
	// COMを終了
	//
	CoUninitialize();

	return 0;
}
