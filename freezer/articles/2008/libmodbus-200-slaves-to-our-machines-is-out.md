title: libmodbus 2.0.0 'Slaves to Our Machines' is out!
published: 2008-05-18
tags: [release]

[libmodbus](http://libmodbus.org) is a library to send/receive data to/from
ModBus devices which respect the protocol established by Modicon.

This new release contains major enhancements like the slave component.

A special thanks to [Todd Denniston](https://launchpad.net/~todd-denniston) for
this release.


libmodbus 2.0.0 (2008-05-18)
============================

-   Slave API
    <https://blueprints.launchpad.net/libmodbus/+spec/slave-api>
-   No more glib dependency
    <https://blueprints.launchpad.net/libmodbus/+spec/glib-dependency>
-   Unit testing and many test programs
-   Waf build support
    <https://blueprints.launchpad.net/libmodbus/+spec/waf-support>
-   MacOS X support by Matthew Butch
    <https://blueprints.launchpad.net/libmodbus/+spec/macosx-support>
-   No more glib dependency
    <https://blueprints.launchpad.net/libmodbus/+spec/glib-dependency>
-   Unit testing (unit-test-slave and unit-test-master)
-   Port number is now defined at initialisation by Dirk Reusch
-   Better memory management (uint8\_t \*data and packing of
    modbus\_param\_t)
-   Better error management
-   Declare many static functions and const arrays
-   Enhance an integer division
-   The GNU licences LGPL and GPL are in version 3
-   Debian and RPM packages (\#224496)
-   Many cleanups
-   Fix \#159443 reported by Stefan Bisanz

    Index of incoming data in force multiple coils function
-   Fix \#161989 reported by Konstantinos Togias

    Serial device paths more than 10 chars long (eg. /dev/ttyUSB0) don't
    fit to modbus\_param\_t -\> device char[11] var.
-   Fix \#188189 reported by Chris Hellyar

    Compute\_response\_size() no entry for read\_input\_status()
-   Fix \#191039 reported by Todd Denniston

    modbus.h is not installed at prefix.
-   Fix \#211460 reported by Todd Denniston

    With TCP, automatic reconnect on error may not be desired.
-   Fix \#224485 reported by Todd Denniston

    libmodbus does not link with c++ code.
-   Fix \#224496 reported by Todd Denniston

    It is easier to install on rpm based systems with a spec file.
