@echo off

pause

@rem ‚Ä‚·‚Æ

SET PATH=C:\ProgramData\Anaconda3;C:\ProgramData\Anaconda3\Library\mingw-w64\bin;C:\ProgramData\Anaconda3\Library\usr\bin;C:\ProgramData\Anaconda3\Library\bin;C:\ProgramData\Anaconda3\Scripts;C:\ProgramData\Anaconda3\bin;C:\ProgramData\Anaconda3\condabin;%PATH%

SET PATH=C:\Program Files\Tesseract-OCR;%PATH%
SET TESSDATA_PREFIX=C:\Program Files\Tesseract-OCR

python ss_eve.py 2
rem python ocr_test.py
rem python ss_crop.py

pause

exit /B

