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
	
	// �f�o�C�X�t�B���^
	IBaseFilter * pVideoInput = NULL;
	IBaseFilter * pAudioInput = NULL;
	IBaseFilter * pVideoComp = NULL;
	const int videoInputNo = 0;
	const int audioInputNo = 0;
	const int videoCompNo = 0;
	
	// �r�f�I���̓f�o�C�X�J�e�S���̃N���X�񋓎q�̎擾
	IEnumMoniker * pEnumCat = NULL;
	
	std::cout << "Video Input Device" << std::endl;
	
	hr = pSysDevEnum->CreateClassEnumerator(
		CLSID_VideoInputDeviceCategory,
		&pEnumCat,
		0);
	if( hr == S_OK ) {
		// �ꉞ�A���Z�b�g���Đ擪���琔���Ȃ���
		pEnumCat->Reset();
		
		// ���j�J��񋓂���
		IMoniker * pMoniker = NULL;
		ULONG cFetched;
		int i = 0;
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
			
			if(i!=videoInputNo) {
				// ���j�J���t�B���^��bind
				pMoniker->BindToObject(
					0, 0,
					IID_IBaseFilter,
					(LPVOID *)&pVideoInput);
					
				// �t�B���^���O���t�ɒǉ�
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
		// �ꉞ�A���Z�b�g���Đ擪���琔���Ȃ���
		pEnumCat->Reset();
		
		// ���j�J��񋓂���
		IMoniker * pMoniker = NULL;
		ULONG cFetched;
		int i = 0;
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
				// ���j�J���t�B���^��bind
				pMoniker->BindToObject(
					0, 0,
					IID_IBaseFilter,
					(LPVOID *)&pVideoInput);
					
				// �t�B���^���O���t�ɒǉ�
				pGraphBuilder->AddFilter(
					pVideoInput,
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
		// �ꉞ�A���Z�b�g���Đ擪���琔���Ȃ���
		pEnumCat->Reset();
		
		// ���j�J��񋓂���
		IMoniker * pMoniker = NULL;
		ULONG cFetched;
		int i = 0;
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
				// ���j�J���t�B���^��bind
				pMoniker->BindToObject(
					0, 0,
					IID_IBaseFilter,
					(LPVOID *)&pVideoInput);
					
				// �t�B���^���O���t�ɒǉ�
				pGraphBuilder->AddFilter(
					pVideoInput,
					L"Video Compressor");
			}
			pMoniker->Release();
			i++;
		}
		pEnumCat->Release();
	}
	
	pSysDevEnum->Release();
	
	//
	// CaptureGraphBuilder2�Ńt�B���^�O���t���\�z����
	//
	ICaptureGraphBuilder2 * pCaptureGraphBuilder2;
	hr = CoCreateInstance(
		CLSID_CaptureGraphBuilder2,
		NULL,
		CLSCTX_INPROC,
		IID_ICaptureGraphBuilder2,
		(LPVOID *)&pCaptureGraphBuilder2);
	
	// �t�B���^�O���t���Z�b�g
	pCaptureGraphBuilder2->SetFiltergraph(pGraphBuilder);
	
	// �O���t�𐶐�(�v���r���[�̓o�^�H)
	pCaptureGraphBuilder2->RenderStream(
		&PIN_CATEGORY_PREVIEW,
		NULL,
		pVideoInput,
		NULL, NULL);
				
	//
	// ���f�B�A�R���g���[���̎擾
	//
	IMediaControl * pMediaControl;
	pGraphBuilder->QueryInterface(
		IID_IMediaControl,
		(LPVOID *)&pMediaControl);
		
	// �Đ��J�n
	pMediaControl->Run();
	
	// OK�ŏI��
	MessageBox(NULL,
		L"OK�ŏI��",
		L"�Đ���",
		MB_OK);
	
	//
	// FilterGraph�����
	//
	pVideoInput->Release();
	pMediaControl->Release();
	pCaptureGraphBuilder2->Release();
	pGraphBuilder->Release();
	
	//
	// COM���I��
	//
	CoUninitialize();

	return 0;
}
