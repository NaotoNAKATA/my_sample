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
	
	//
	// COM��������
	//
	CoInitialize(NULL);
	
	//
	// FilterGraph�𐶐�
	//
	IGraphBuilder * pGraphBuilder;
	hr = CoCreateInstance(
		CLSID_FilterGraph,
		NULL,
		CLSCTX_INPROC,
		IID_IGraphBuilder,
		(LPVOID *)&pGraphBuilder);
		
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
	if( FAILED(hr) ) {
		return hr;
	}
	
	// �r�f�I���̓f�o�C�X�J�e�S���̃N���X�񋓎q�̎擾
	IEnumMoniker * pEnumCat = NULL;
	hr = pSysDevEnum->CreateClassEnumerator(
		//CLSID_VideoCompressorCategory,
		CLSID_VideoInputDeviceCategory,
		&pEnumCat,
		0);
	if( hr == S_OK ) {
		// �ꉞ�A���Z�b�g���Đ擪���琔���Ȃ���
		pEnumCat->Reset();
		
		// ���j�J��񋓂���
		IMoniker * pMoniker = NULL;
		ULONG cFetched;
		while(pEnumCat->Next(1, &pMoniker, &cFetched) == S_OK )
		{
			// IPropertyBag��Bind
			IPropertyBag * pPropertyBag;
			hr = pMoniker->BindToStorage(
				0,
				0,
				IID_IPropertyBag,
				(LPVOID *)&pPropertyBag);
			if( SUCCEEDED(hr) )
			{
				// �t�B���^�̃t�����h���[�����擾
				VARIANT var;
				VariantInit(&var);
				var.vt = VT_BSTR;
				hr = pPropertyBag->Read(
					L"FriendlyName",
					&var,
					0);
				if( SUCCEEDED(hr) )
				{
					// �t�����h���[���̕\��
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
			pMoniker->Release();
		}
		pEnumCat->Release();
	}
	pSysDevEnum->Release();
	
	//
	// FiltetGraph�����
	//
	pGraphBuilder->Release();
	
	//
	// COM���I��
	//
	CoUninitialize();

	return 0;
}
