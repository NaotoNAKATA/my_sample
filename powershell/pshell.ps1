# Excelオブジェクト作成
$excel = New-Object -ComObject Excel.Application


# 表示するかどうか
#$excel.Visible = $true
#$excel.DisplayAlerts = $true
$excel.Visible = $false
$excel.DisplayAlerts = $false

# ワークブックの新規作成
$book = $excel.Workbooks.Add()

# 既存のファイルを開く
#$book = $excel.Workbooks.Open("hoge.xlsx")


# シートの数
$book.Sheets.Count

# 1番目のシートの名前
$book.Sheets(1).Name

# アクティブになっているシート名
$book.ActiveSheet.Name


# シートの取得
$sheet = $book.Sheets(1)

# シートの名前の変更
$sheet.Name = "テストシート"

# シートに書き込み
$sheet.Cells.Item(1, 1) = "ここはA1"
$sheet.Cells.Item(1, 2) = "ここはA2"
$sheet.Cells.Item(1, 1).Text

$row = 10
for($i=0; $i -lt $row; $i++) {
	if($i -eq $row-1) {
		$sheet.Cells.Item($i+2, 1) = "合計"
		#$sheet.Cells.Item($i+2, 2) = 
	}
	else {
		$sheet.Cells.Item($i+2, 1) = $i
		$sheet.Cells.Item($i+2, 2) = $i
	}
}

# 保存する
#$book.SaveAs("${HOME}/Desctop/PowerShellサンプル.xlsx")
$book.SaveAs("PowerShellサンプル.xlsx")

# 終了する
$excel.Quit()

# 変数の破棄
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel)
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($book)
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($sheet)

pause
