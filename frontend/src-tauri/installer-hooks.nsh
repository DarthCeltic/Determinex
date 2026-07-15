!macro NSIS_HOOK_POSTINSTALL
  DetailPrint "Installing Visual C++ Redistributable (required runtime, one-time)..."
  ExecWait '"$INSTDIR\resources\vc_redist.x64.exe" /install /quiet /norestart' $0
  DetailPrint "VC++ Redistributable installer exit code: $0"
!macroend
