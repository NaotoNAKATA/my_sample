# Excel�I�u�W�F�N�g�쐬
$excel = New-Object -ComObject Excel.Application


# �\�����邩�ǂ���
#$excel.Visible = $true
#$excel.DisplayAlerts = $true
$excel.Visible = $false
$excel.DisplayAlerts = $false

# ���[�N�u�b�N�̐V�K�쐬
$book = $excel.Workbooks.Add()

# �����̃t�@�C�����J��
#$book = $excel.Workbooks.Open("hoge.xlsx")


# �V�[�g�̐�
$book.Sheets.Count

# 1�Ԗڂ̃V�[�g�̖��O
$book.Sheets(1).Name

# �A�N�e�B�u�ɂȂ��Ă���V�[�g��
$book.ActiveSheet.Name


# �V�[�g�̎擾
$sheet = $book.Sheets(1)

# �V�[�g�̖��O�̕ύX
$sheet.Name = "�e�X�g�V�[�g"

# �V�[�g�ɏ�������
$sheet.Cells.Item(1, 1) = "������A1"
$sheet.Cells.Item(1, 2) = "������A2"
$sheet.Cells.Item(1, 1).Text

$row = 10
for($i=0; $i -lt $row; $i++) {
	if($i -eq $row-1) {
		$sheet.Cells.Item($i+2, 1) = "���v"
		#$sheet.Cells.Item($i+2, 2) = 
	}
	else {
		$sheet.Cells.Item($i+2, 1) = $i
		$sheet.Cells.Item($i+2, 2) = $i
	}
}

# �ۑ�����
#$book.SaveAs("${HOME}/Desctop/PowerShell�T���v��.xlsx")
$book.SaveAs("PowerShell�T���v��.xlsx")

# �I������
$excel.Quit()

# �ϐ��̔j��
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel)
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($book)
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($sheet)

pause
