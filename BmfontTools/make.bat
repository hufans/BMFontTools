@echo off & setlocal enabledelayedexpansion
set BMFont_PATH=C:\Program Files (x86)\AngelCode\BMFont
set WORK_PATH=C:\Users\St\Desktop\BmfontTools
set OUT_FILE_NAME=myCoin
set OUT_FILE_PATH=%WORK_PATH%\output
set IMG_FILES_NAME=pic

copy %WORK_PATH%\configModel.bmfc %WORK_PATH%\config.bmfc

del %WORK_PATH%\pngName.txt

for /R "%WORK_PATH%\%IMG_FILES_NAME%" %%s in (*.png) do ( 
echo icon="%%s",%%d,0,0,0 >>%WORK_PATH%\pngName.txt
)

BmExt.exe <%WORK_PATH%\font_ascii.txt >>%WORK_PATH%\config.bmfc
pause
"%BMFont_PATH%\bmfont.exe" -t %WORK_PATH%\font_utf_8.txt -c "%WORK_PATH%\config.bmfc" -o "%OUT_FILE_PATH%\%OUT_FILE_NAME%.fnt"
pause