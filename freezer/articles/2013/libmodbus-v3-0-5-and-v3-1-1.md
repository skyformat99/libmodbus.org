title: Two releases the same day v3.0.5 and v3.1.1
published: 2013-10-29
tags: [release]
summary: Many features and a remote buffer overflow vulnerability has been fixed.

**libmodbus 3.0.5 (2013-10-06)**

libmodbus v3.0.x branch has been updated to include important fixes backported
from v3.1.1.

- Fix remote buffer overflow vulnerability
- Fix receiving of incorrect queries in write_single

**libmodbus 3.1.1 (2013-10-06)**

More robust to exploits, more compliant and better handling of connect/close
sequences. Windows support still broken.

- New unit tests
- Fix remote buffer overflow vulnerability (closes #25, #105)
- Explain how to define response timeouts when many RTU slaves
- Fix receiving of incorrect queries in `write_single` and
  `mask_write_register`. Thanks to James Nutaro.
- Check return value of autoreconf. Thanks to Lauri Nurmi.
- Constant for broacast and test ordering
- Fix the fix of device string check
- Various changes to try to improve *broken* Windows support
- Try to fix MinGW compilation
- Portable use of bswap_32
- Improve support of MacOS X
- Fix socket value on init/close
- Returns -1 on invalid mode in `modbus_rtu_set_rts`
- Protect all public functions against invalid context
- Sleep for delay of response timeout before reconnect (closes #77). Thanks to Karl Palsson.
- Baud rate until 4,000,000 (POSIX), 1,000,000 (Windows) (closes #93)
- New `modbus_get|set_float_dcba` to get|set float in inversed byte order
- Remove unsupported -Wtype-limits for GCC < 4.3.5 (closes #109).
- Enable out-of-source build. Thanks to Yegor Yefremov.
- Fix alignment problem on ARMv5 platform
- Improvement to Debian package. Thanks to Alexander Klauer.
- Improve support of VS 2005. Thanks to Petr Gladkiy.
- Add documentation for `modbus_mask_write_register` (closes #91). Thanks to Martijn de Gouw.
- Avoid C99 declaration in win32 section code (closes #92). Thanks to oldfaber and endrelovas.
- Add a windows scripting host configure file. Thanks to oldfaber and Stéphane Raimbault.
- Fix typo in modbus_strerror documentation. Thanks to Mirko Rajkovaca.
- Rename reserved C++ keywords of modbus_mask_write_register. Thanks Tobias Doerffel.
- Another quick workaround for deficient OS (closes #63)
- Add support for Mask Write Register
- Fix missing close on socket in random-test-server. Thanks to Damian Zieliński.
- Use nonblocking sockets on Win32 and OS X/iOS too. Thanks to Julian Raschke.
- Fix all compilations warnings spotted by new compilation flags
- Major update of build system
- Calculate RTS activation time by send length
- Dynamic memory allocation of device name (closes #11)
- Add unit tests for `modbus_mapping_new`
- Add Visual Studio 2008 project files by oldfaber
- Fix missing argument in synopsis section of `modbus_rtu_set_serial_mode`
- Fix wrong constant names to create version number
- More compilation fixes for Windows by oldfaber.
- Fix wrong constant names to create version number. Thanks to Denis Davydov.
