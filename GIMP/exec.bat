@echo off

pause

	SET PATH=%PATH%;C:\Program Files\GIMP 2\bin

	SET INPUT_FILE=./sample.jpg
	SET OUTPUT_DIR=./output

	start gimp-2.10.exe -i -fdsc --verbose --batch-interpreter python-fu-eval -b "pdb.python_fu_my_sample1('%INPUT_FILE%', '%OUTPUT_DIR%')" -b "pdb.gimp_quit(0)"
	
exit /B
