@echo off
set "fileToDelete=C:\Users\%USERNAME%\Desktop\deleteMe.txt"
echo Deleting file: %fileToDelete%
if exist "%fileToDelete%" (
 del "%fileToDelete%"
 echo File deleted successfully.
) else (
 echo The file does not exist or the path is incorrect.
)
pause