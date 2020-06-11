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
	std::cout << "�f�o�C�X��񋓂���" << std::endl;

	//
	// COM��������
	//
	CoInitialize(NULL);

	//
	// �L���v�`���f�o�C�X�̎擾
	//
	SysDevEnum sys_dev_enum = SysDevEnum();

	// �r�f�I�f�o�C�X�̎擾
	sys_dev_enum.preview_video_device_name();

	// �I�[�f�B�I�f�o�C�X�̎擾
	sys_dev_enum.preview_audio_device_name();

	// �r�f�I�R���v���b�T�[�̎擾
	sys_dev_enum.preview_video_compressor_name();

	// �I�[�f�B�I�R���v���b�T�[�̎擾
	sys_dev_enum.preview_audio_compressor_name();

	//
	// COM���I��
	//
	CoUninitialize();

	return 0;
}