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

SysDevEnum::SysDevEnum() {
	// �f�o�C�X��񋓂��邽�߂�SystemDeviceEnum�𐶐�
	HRESULT hr = CoCreateInstance(
		CLSID_SystemDeviceEnum,
		NULL,
		CLSCTX_INPROC_SERVER,
		IID_ICreateDevEnum,
		(LPVOID *)&pSysDevEnum);

	if (FAILED(hr)) {
		pSysDevEnum = NULL;
	}
}

SysDevEnum::~SysDevEnum() {
	pSysDevEnum->Release();
}

void SysDevEnum::preview_video_device_name(void) {
	std::cout << "Video Input Device" << std::endl;
	this->system_device_enum(CLSID_VideoInputDeviceCategory);
}
void SysDevEnum::preview_audio_device_name(void) {
	std::cout << "Audio Input Device" << std::endl;
	this->system_device_enum(CLSID_AudioInputDeviceCategory);
}
void SysDevEnum::preview_video_compressor_name(void) {
	std::cout << "Video Compressor" << std::endl;
	this->system_device_enum(CLSID_VideoCompressorCategory);
}
void SysDevEnum::preview_audio_compressor_name(void) {
	std::cout << "Audio Compressor" << std::endl;
	this->system_device_enum(CLSID_AudioCompressorCategory);
}


void SysDevEnum::system_device_enum(const IID & CLSID) {
	HRESULT hr;

	// �r�f�I���̓f�o�C�X�J�e�S���̃N���X�񋓎q�̎擾
	IEnumMoniker * pEnumCat = NULL;
	hr = pSysDevEnum->CreateClassEnumerator(CLSID, &pEnumCat, 0);
	if (hr == S_OK) {
		// �ꉞ�A���Z�b�g���Đ擪���琔���Ȃ���
		pEnumCat->Reset();

		// ���j�J��񋓂���
		IMoniker * pMoniker = NULL;
		ULONG cFetched;
		while (pEnumCat->Next(1, &pMoniker, &cFetched) == S_OK)
		{
			// Propety�̐���
			this->property_bag_control(pMoniker);

			// ���
			pMoniker->Release();
		}
		pEnumCat->Release();
	}
}

void SysDevEnum::preview_friendly_name(IPropertyBag * pPropertyBag) {
	VARIANT var;
	VariantInit(&var);
	var.vt = VT_BSTR;
	HRESULT hr = pPropertyBag->Read(L"FriendlyName", &var, 0);
	if (SUCCEEDED(hr))
	{
		// �t�����h���[���̕\��
		TCHAR devname[256];
		WideCharToMultiByte(
			CP_ACP, 0, var.bstrVal, -1,
			(LPSTR)devname, sizeof(devname),
			0, 0);

		printf("   %s\n", (LPSTR)devname);
		//printf("%   ls\n", var.bstrVal);
	}
	VariantClear(&var);
}

void SysDevEnum::property_bag_control(IMoniker * pMoniker) {
	// IPropertyBag��Bind
	IPropertyBag * pPropertyBag;
	HRESULT hr = pMoniker->BindToStorage(0, 0, IID_IPropertyBag, (LPVOID *)&pPropertyBag);
	if (SUCCEEDED(hr))
	{
		// �t�B���^�̃t�����h���[�����擾
		this->preview_friendly_name(pPropertyBag);

		// ���
		pPropertyBag->Release();
	}

}