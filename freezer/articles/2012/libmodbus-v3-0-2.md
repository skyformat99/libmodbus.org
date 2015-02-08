title: libmodbus v3.0.2
published: 2012-02-06
tags: [release]

Yet another stable release with minor fixes.

**libmodbus 3.0.2 (2012-01-16)**

- Update Debian package.
- Documentation fixes and additions.
- Add missing C++ macros in public headers. Thanks to Bernhard Agthe.
- Protects `modbus_mapping_free` against NULL argument. Thanks to
  Andrea Mattia.
- Fix check on file doc/libmodbus.7 in acinclude.m4 (closes #28)
- Close file descriptor when the settings don't apply in RTU. Original
  patch provided by Thomas Stalder.
- unit-test.h is now generated to avoid config.h dependency.
- Request for Windows Sockets specification version 2.2 instead of
  2.0. Thanks to Pavel Mazniker for the report.
