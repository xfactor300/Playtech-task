xcopy /s %~dp0src %~dp0dest /Y
IF exist %~dp0dest\tool.exe (
	ren %~dp0dest\tool.exe launcher.exe
) ELSE (
 echo "File not found"
)
rmdir %~dp0src /s /q
START %~dp0dest\launcher.exe