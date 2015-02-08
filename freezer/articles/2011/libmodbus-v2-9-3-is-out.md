title: libmodbus v2.9.3 is out!
published: 2011-01-17
tags: [release]

During this development cycle, I've received more feedback than for any
other releases. That's really cool, thank you! With this new release,
you can consider to migrate from the previous 2.0.x series for your
applications.

**libmodbus v2.9.3 (2011-01-14)**

- Major rewriting of the message reading (no more timeouts on
  exception)
- New function to reply to an indication with an exception message
  `modbus_reply_exception()`
- New function `modbus_get_header_length(modbus_t *ctx)`
- New functions to manipulate data:
    - `MODBUS_GET_INT32_FROM_INT16`
    - `MODBUS_GET_INT16_FROM_INT8`
    - `MODBUS_SET_INT16_TO_INT8`
- Fix [#2](https://github.com/stephane/libmodbus/issues/2). Read/write were
  swapped in `_FC_READ_AND_WRITE_REGISTERS`
- Install an ignore handler for SIGPIPE on *BSD. Original patch by  Jason Oster.
- Fix closing of Win32 socket. Reported by Petr Parýzek.
- Fix unit identifier not copied by the TCP server. Reported by Antti Manninen
- Fix missing `modbus_flush()` in unit tests.
- Fixes for OpenBSD by Barry Grumbine and Jason Oster

This time, the release is not only availabe as tarball but also as
Fedora and Ubuntu packages on the [download
page](http://libmodbus.org/download).

For the next release, I've already merged my `ipv6` branch (based on the work of
Florian Forster), the [rtai](https://github.com/clecol/libmodbus/tree/rtai)
branch of Chris Cole is waiting for review (ah, RTAI, like in the good old days
:) and I hope to take care of the `gtk-doc` work done by Luis Matos.
