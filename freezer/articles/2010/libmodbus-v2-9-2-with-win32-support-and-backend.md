title: New libmodbus 2.9.2 with win32 support and backends
published: 2010-12-05
tags: [release]

OK, I don't care about Windows but I'm happy libmodbus offers a
bit of Open Source to this platform so thank you to Tobias Doerffel for
this contribution. The other major change is the use of an internal
backend to isolate the transport layers (only serial RTU and TCP/IPv4
for now).

**libmodbus 2.9.2 (2010-12-05)**

-   Fix segfault in bandwidth-server-many-up on inet\_ntoa() call
-   Fix unit test of report slave ID in RTU
-   Fix GH-3. Remove inclusion of config.h in modbus.h
-   Correctly detect if we are cross
-   compiling for win32 by Kirill Smelkov.
-   Rename modbus\_[listen|accept] to modbus\_tcp\_[listen|accept]
-   Fix setting of the broadcast address
-   Remove slave argument from modbus\_new\_rtu()
-   Win32 support by Tobias Doerffel
-   Split source code around RTU and TCP (backends)
-   Check received function code

So let's run your MinGW!
