#pragma once

#include <dshow.h>

#pragma include_alias("dxtrans.h", "qedit.h")
#define __IDxtCompositor_INTERFACE_DEFINED__
#define __IDxtAlphaSetter_INTERFACE_DEFINED__
#define __IDxtJpeg_INTERFACE_DEFINED__
#define __IDxtKey_INTERFACE_DEFINED__
#include "qedit.h"

#include <iostream>
#include <cstdint>

class SysDevEnum
{
public:
	SysDevEnum();
	~SysDevEnum();

	void preview_video_device_name(void);
	void preview_audio_device_name(void);
	void preview_video_compressor_name(void);
	void preview_audio_compressor_name(void);

private:
	ICreateDevEnum * pSysDevEnum;
	void system_device_enum(const IID & CLSID);
	void property_bag_control(IMoniker * pMoniker);
	void preview_friendly_name(IPropertyBag * pPropertyBag);
};
