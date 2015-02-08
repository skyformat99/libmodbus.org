title: libmodbus 1.2.2 is out!
published: 2008-01-02
tags: [release]

[libmodbus](https://launchpad.net/libmodbus/) is an old project but I
never wrote a post about it, 2008 is the right year!

I recently released 2 new versions to include some bug fixes:

**libmodbus 1.2.2 (2007-11-12)**

-   Fix [\#161989](https://bugs.launchpad.net/libmodbus/+bug/161989)
    (Konstantinos Togias) Serial device paths more than 10 chars long
    (eg. /dev/ttyUSB0) don't fit to modbus\_param\_t -\> device char[11]
    var.
-   Structure is also bit better 'packed' to conserve memory (see the
    trunk for a real enhancement). libmodbus 1.2.1 (2007-11-02)
-   Fix [\#159443](https://bugs.launchpad.net/libmodbus/+bug/159443)
    (Stefan Bisanz) Index of incoming data in force multiple coils
    function
-   Deleted useless code in check\_crc16()
-   Untabify source code
-   Changed author's email (Stéphane Raimbault)

The development continues (slowly) in trunk to include the slave component of
the protocol.
