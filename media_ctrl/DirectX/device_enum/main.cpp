#include <dshow.h>

#pragma include_alias("dxtrans.h", "qedit.h")
#define __IDxtCompositor_INTERFACE_DEFINED__
#define __IDxtAlphaSetter_INTERFACE_DEFINED__
#define __IDxtJpeg_INTERFACE_DEFINED__
#define __IDxtKey_INTERFACE_DEFINED__
#include "qedit.h"

#include <iostream>
#include <cstdint>

#include "device_enum.h"

int32_t main(int32_t argc, const char * const argv[])
{
	std::cout << "デバイスを列挙する" << std::endl;

	//
	// COMを初期化
	//
	CoInitialize(NULL);

	//
	// キャプチャデバイスの取得
	//
	SysDevEnum sys_dev_enum = SysDevEnum();

	// ビデオデバイスの取得
	sys_dev_enum.preview_video_device_name();

	// オーディオデバイスの取得
	sys_dev_enum.preview_audio_device_name();

	// ビデオコンプレッサーの取得
	sys_dev_enum.preview_video_compressor_name();

	// オーディオコンプレッサーの取得
	sys_dev_enum.preview_audio_compressor_name();

	//
	// COMを終了
	//
	CoUninitialize();

	return 0;
}