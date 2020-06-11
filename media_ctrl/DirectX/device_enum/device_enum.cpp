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

	// �r�f�I���̓f�o�C�X�J�e�S���̃N���X�񋓎q�̎擾
	IEnumMoniker * pEnumCat = NULL;
	hr = pSysDevEnum->CreateClassEnumerator(CLSID, &pEnumCat, 0);
	if (hr == S_OK) {
		// �ꉞ�A���Z�b�g���Đ擪���琔���Ȃ���
		pEnumCat->Reset();

		// ���j�J��񋓂���
		IMoniker * pMoniker = NULL;
		ULONG cFetched;
		int32_t i = 0;
		while (pEnumCat->Next(1, &pMoniker, &cFetched) == S_OK)
		{
			// IPropertyBag��Bind
			IPropertyBag * pPropertyBag;
			hr = pMoniker->BindToStorage(0, 0, IID_IPropertyBag, (LPVOID *)&pPropertyBag);
			if (SUCCEEDED(hr))
			{
				// �t�B���^�̃t�����h���[�����擾
				VARIANT var;
				VariantInit(&var);
				var.vt = VT_BSTR;
				hr = pPropertyBag->Read(L"FriendlyName", &var, 0);
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
	std::cout << "�f�o�C�X��񋓂���" << std::endl;

	HRESULT hr;

	//
	// COM��������
	//
	CoInitialize(NULL);

	//
	// �L���v�`���f�o�C�X�̎擾
	//
	// �f�o�C�X��񋓂��邽�߂�SystemDeviceEnum�𐶐�
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

	// �r�f�I�f�o�C�X�̎擾
	std::cout << "Video Input Device" << std::endl;
	system_device_enum(pSysDevEnum, CLSID_VideoInputDeviceCategory);

	// �I�[�f�B�I�f�o�C�X�̎擾
	std::cout << "Audio Input Device" << std::endl;
	system_device_enum(pSysDevEnum, CLSID_AudioInputDeviceCategory);

	// �r�f�I�R���v���b�T�[�̎擾
	std::cout << "Video Compressor" << std::endl;
	system_device_enum(pSysDevEnum, CLSID_VideoCompressorCategory);

	// �I�[�f�B�I�R���v���b�T�[�̎擾
	std::cout << "Audio Compressor" << std::endl;
	system_device_enum(pSysDevEnum, CLSID_AudioCompressorCategory);

	// ���
	pSysDevEnum->Release();

	//
	// COM���I��
	//
	CoUninitialize();

	return 0;
}
