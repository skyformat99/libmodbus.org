title: libmodbus v2.9.4 is out!
published: 2011-06-05
tags: [release]

This minor release contains many new features with IPv6 support, documentation
(man and HTML), error recovery modes and small API changes. I'm intend to
release the version 3.0 so I need feeback from this release even more if you use
libmodbus on Windows or MacOS X (check nanosleep support for example).

It's easy to test the library, just compile and run the unit tests! Don't forget
to notify your success or failure (by mail, wiki or bug report), see the
[Call for Testers][] page or the mailing list for details.

There are already Debian and Fedora packages but I need help to submit them to
the distributions, so all experience in this field is appreciated.

**libmodbus 2.9.4 (2011-06-05)**

- IPv6 support Make the TCP implementation "protocol independent" by
  Florian Forster and Stéphane Raimbault.
- Fix compilation on Windows 7 (x64) with MinGW/MSYS and GCC 4.
  Reported by Patsy Kaye.
- Documentation of libmodbus functions with AsciiDoc (man and HTML) by
  Stéphane Raimbault
- Avoid an iteration in flush function
- New functions to send and receive raw requests
  (`modbus_send_raw_request`, `modbus_receive_confirmation`)
- Fix flush function of TCP backend on Windows
- API changes for server/slave:

    - `modbus_receive` doesn't take socket/fd argument anymore
    - new function `modbus_set_socket` to set socket/fd

- API changes for timeout functions:

    - `modbus_get_timeout_begin` -> `modbus_get_response_timeout`
    - `modbus_set_timeout_begin` -> `modbus_set_response_timeout`
    - `modbus_get_timeout_end` -> `modbus_get_byte_timeout`
    - `modbus_set_timeout_end` -> `modbus_set_byte_timeout`

- Fix longstanding limitation of server to wait forever
- New functions `modbus_set/get_serial_mode` by Manfred Gruber and
  Stéphane Raimbault for RS485 communications
- Improved recovery mode (see `modbus_set_error_recovery`
  documentation) for data link and protocol errors.
- Fix compilation issue with Microsoft Visual Studio 2008. Reported by
  Allan Cornet.

[Call for Testers]: https://github.com/stephane/libmodbus/wiki/Call-for-Testers
