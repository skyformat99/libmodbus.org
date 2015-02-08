title: New libmodbus v3.0.3
published: 2012-05-26
tags: [release]

This new bugfix release contains the following changes:

- Fix another Visual C++ 2008/2010 deficiency (closes #53)
- Add -lsocket to compile on QNX
- Fix TCP PI init under Windows. Thanks to oldfaber.
- Fix a missing free in random-test-client Thanks again to Stefan
  Finzel.
- Fix OMG bug in `modbus_mapping_free` not freeing memory. Thanks to
  Stefan Finzel for the bug report.
- Fix semicolon typo and unistd.h include under Windows. Thanks to
  Andrew Kravchuk.

[Download libmodbus 3.0.3](https://github.com/downloads/stephane/libmodbus/libmodbus-3.0.3.tar.gz)
