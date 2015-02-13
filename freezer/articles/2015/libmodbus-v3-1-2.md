title: libmodbus v3.1.2
published: 2015-02-10
tags: [release]
summary: This new development release contains new features about server listening and timeout handling.

If you still want to listen any addresses in your TCP IPv4 server, you must now
set the IP address to NULL in `modbus_new_tcp` before listening. Now,
`modbus_tcp_listen` only listen the IP address set in the Modbus context (see
documentation).

This release introduces API changes on `modbus_get_byte_timeout`,
`modbus_get_response_timeout`, `modbus_set_byte_timeout`,
`modbus_set_response_timeout` to ease writing of language bindings.

- Rewrite documentation building system
- Fix timeouts in unit tests
- Don't flush on illegal address errors in single write functions
- Fix compilation on compilers not supporting c99 mode.
  Thanks to Michael Heimpold.
- Update license for the tests in Debian packaging (#221)
- Move check of device earlier to avoid a free call
- Unit test for baud rate check and error message.
- Fix crash `modbus_new_rtu` when baud is 0.
  Thank you to Daniel Schürmann.
- Removed function prototype without implementation
  Thank you Andrej Skvortzov.
- Switch test programs to a BSD license
- Fix remote buffer overflow vulnerability on write requests
- Avoid twice `connect()` in source code (closes #194)
- Fix compilation with MinGW (GCC 4.8.1) under Win7 (closes #163)
  Thank you MarjanTomas and SwissKnife.
- Fix TCP IPv4 `modbus_connect()` on win32 (closes #100 and #165)
  Thank you Petr Gladkiy and Marjan Tomas.
- Fix 24a05ebd3c0 - win32: init of `modbus_tcp_pi_listen` (#187)
- `INADDR_*` macros are defined in host byte order
- Filter of IP addresses in IPv4 server (closes #190)
- Allow to listen any hosts in IPv6 (closes #32)
- Define and public export of `MODBUS_MAX_PDU_LENGTH` (closes #167)
- Truncate data from response in `report_slave_id` to new max arg (closes #167)
- Fix response timeout modification on connect (closes #80)
- New API to set/get response and byte timeouts.
  New unit tests and updated documentation.
- Export Modbus function codes supported by libmodbus
- Fix bandwidth-server-one (closes #152)
- Check debug flag in RTU code
- Remove warnings caused by shadowed 'index' variable.
  Thanks to Åke Forslund.
- Use accept4 in TCP PI if available
- Add documentation for `tcp[_pi]_accept` (closes #31)
- Fix mistake in `modbus_tcp_listen` documentation
- Add documentation for `modbus_tcp_pi_listen`
- Fix for MinGW and Windows (#144, #169, #175, #180, #181, #187)
  Thanks to Marjan Tomas.
- Many other fixes (#134, #157, #158, #183, #184) and improvements.
