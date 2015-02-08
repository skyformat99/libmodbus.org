title: Very late announce of libmodbus v3.1.0
published: 2013-05-11
tags: [release]

OK last year, I've silently released libmodbus v3.1.0 and it's never too late to
announce it!

**libmodbus 3.1.0 (2012-05-22)**

Major changes to handle many slaves in RTU mode, non blocking connections and
RTS flow control.

- Fixes for Microsoft Visual C++ compiler
- Fixes for Windows. Thanks to oldfaber
- Return value of `_modbus_tcp_pi_connect()` on failure (closes )
- Avoid ioctl call on non-RS485 ports. Thanks to Michael Haberler
- Display node and service in PI and port in IPv4 at connection
- Return -1 on getaddrinfo error and print error in debug mode
- More robust way to establish the connection in non blocking mode
- TCP - Socket in non blocking mode by default. Thanks to Thomas Stalder
- Apply CLOEXEC flag for TCP protocol independent too (IPv6)
- New RTU receive() to ignore confirmation from other slaves (closes #18)
- Move RTU filtering in CRC check to avoid useless call to modbus_reply
- Unique transaction identifier by TCP connection
- Use accept4 with SOCK_CLOEXEC when available (Linux)
- Open fd and socket with the CLOEXEC flag when available
- Exception response on report slave ID wasn't detected (closes #27)
- Provides a way to disable the byte timeout (Alex Stapleton)
- Added slave ID check for response messages (Alex Stapleton)
- RTS flow control with `modbus_rtu_set_rts` and `modbus_rtu_get_rts` functions by Torello Querci and Stéphane Raimbault.

[Download libmodbus v3.1.0](https://github.com/stephane/libmodbus/archive/v3.1.0.tar.gz)
