# Why Microsoft CRT DLLs live in this directory

`determinex.exe` links the MSVC C++ runtime dynamically. Its import table names
`MSVCP140.dll` and `MSVCP140_1.dll` directly, and those pull in `VCRUNTIME140.dll`
transitively. A clean Windows 11 image ships none of them.

Until 2026-07-29 the app therefore **could not start at all** on a first install. It died
during loader initialisation with `0xC0000135` (`STATUS_DLL_NOT_FOUND`) about two seconds
after launch. A developer machine can never reproduce this, because installing any Visual
Studio or VC++ redistributable satisfies the dependency permanently.

## Why not install the redistributable from the installer

That was the original design and it cannot work. `windows/vc_redist.wxs` declared a WiX
CustomAction to run the `vc_redist.x64.exe` the bundle shipped. Two separate faults:

1. The fragment was **silently pruned**. WiX discards a fragment nothing references, and
   discarding it is not an error, so `tauri build` succeeded while the produced MSI contained
   no such action. Tauri 2.10 offers `componentRefs` but no `customActionRefs`, so the
   fragment could be anchored only indirectly.
2. Once anchored so it genuinely ran, it failed anyway. The verbose MSI log:

   ```
   MSI_LUA : Custom Action 'InstallVcRedist' is running with sufficient privileges.
   CustomAction InstallVcRedist returned actual error code 1618
      but will be translated to success due to continue marking
   ```

   `1618` is `ERROR_INSTALL_ALREADY_RUNNING`. The action runs inside our own MSI
   transaction, and Windows Installer permits one install at a time, so a nested
   redistributable install can never succeed there. `Return="ignore"` turned that into a
   silent success.

Chaining the redistributable properly needs a Burn bootstrapper wrapping the MSI, which the
Tauri bundler does not produce.

## What we do instead

App-local deployment: the DLLs sit next to `determinex.exe`, and the Windows loader searches
the application directory before `System32`. This needs no elevation, no network, no
install-time action, and behaves identically for the MSI, the NSIS setup, and any portable
layout. Microsoft's redistributable licence explicitly permits app-local deployment of these
files.

Proven on a clean Azure VM with no VC++ runtime, same MSI and same binary both times:

| condition | result |
| --- | --- |
| no CRT beside the exe | exited after 1841 ms, `0xC0000135` |
| these six DLLs beside the exe | resident 15 s, launch OK |

## The files

All six are version **14.50.35719.0**, copied from `C:\Windows\System32` on a machine with
the VC++ 2015-2022 x64 redistributable installed. Keep them at one consistent version;
mixing CRT versions across `MSVCP140*` and `VCRUNTIME140*` is unsupported.

| file | bytes |
| --- | --- |
| `vcruntime140.dll` | 123,472 |
| `vcruntime140_1.dll` | 47,264 |
| `msvcp140.dll` | 553,552 |
| `msvcp140_1.dll` | 35,488 |
| `msvcp140_2.dll` | 278,608 |
| `concrt140.dll` | 321,696 |

`msvcp140_2.dll` and `concrt140.dll` are not in the current import table; they are included
because the set above is the one actually verified to launch, and trimming to a
minimal guess is how this class of bug returns. The whole set is 1.36 MB, against the 25.6 MB
redistributable it replaces.

They are declared as bare filenames in `tauri.conf.json`'s `bundle.resources`, because Tauri
preserves a resource's relative path under the resource root and on Windows that root is the
executable's own directory. A subdirectory would not be on the loader's search path.

## Guard

`tests/test_windows_installer_runtime.py` parses the built `determinex.exe`'s PE import table,
subtracts the DLLs Windows itself provides, and asserts every remaining import is shipped. It
is deliberately derived from the binary rather than from a hardcoded list, so a new native
dependency that needs shipping fails the test instead of shipping a product that cannot start.
