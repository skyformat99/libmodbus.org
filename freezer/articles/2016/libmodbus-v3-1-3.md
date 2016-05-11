title: libmodbus v3.1.3
published: 2016-05-11
tags: [release]
summary: Many fixes and improvements on data mapping, float handling and RTS.

The structure `modbus_mapping_t` has been extended to include the new start
addresses (ABI break).

New function: http://libmodbus.org/docs/v3.1.2/modbus_mapping_new_start_address.html

- New bswap macros for Max OSX by Jakob Bysewski.
- Fix "wildcard address" in TCP IPv6 by Shoichi Sakane.
- Introduce offsets in modbus mappings with `modbus_mapping_new_start_address`.
  Thanks to Michael Heimpold and Stéphane Raimbault.
- Fix address range in random-test-client.
  Thanks to Martin Galvan.
- Add an option to disable tests compilation by Yegor Yefremov.
- Define `MSG_DONTWAIT` to `MSG_NONBLOCK` on AIX (#294).
  Thanks to Fabrice Cantos.
- Fix building when byteswap.h is not defined by Tomasz Mon.
- Add some more macros for data manipulation and documentation.
- Remove duplicate install of modbus.h (closes #290).
  Thanks to Daniel Sutcliffe.
- Move MIGRATION and README.md to dist_doc_DATA target.
- Change order of few functions in modbus RTU code.
- Add entries for `modbus_rtu_[get|set]_delay` in documentation index.
- Implemented runtime configurable RTS delay by Jimmy Bergström.
- Add an entry in libmodbus index page for modbus_rtu_set_custom_rts.
- Add support for user defined RTS toggle function by Jimmy
  Bergström.
- Added `ILLEGAL_DATA_ADDRESS` tests for `modbus_write_register[|s]`.
  Thanks to Andrey Skvortsov.
- Update documentation of `modbus_rtu_set_rts`
- Fix rts signal switch time by Hiromasa Ihara.
- Improve new_rtu and set_slave documentation (related to #276).
- Fix late check of ctx in `modbus_reply[|_exception]` (closes #269).
- Wait the server for 1 second before running tests (help Travis).
- A libmodbus context isn't thread safe and won't be (closes #246).
- Fix buffer overflow in `modbus_mask_write`_register (#265).
- Minor adjustments to README about AsciiDoc.
- Export `MODBUS_MAX_ADU_LENGTH` and documentation (ref #241).
- Explicit check against Modbus broadcast address.
- Do not reply on broadcast requests (fixes #153). Thanks to Michael.
- Add Travis support.
- Run unit tests with standard: make check (closes #205, closes #238).
  This patch has been developed by Andrey Skvortsov, Michael Heimpold
  and Stéphane Raimbault.
- modbus_send_raw_request: limit request length (fixes #207).
  Thanks to Hanno Neuer for spotting this security flaw.
- Add new contributors to AUTHORS
- Introduce SPDX license identifiers. Thanks to Michael Heimpold.