title: Not compliant device can be time consuming!
published: 2011-04-27
tags: [compliance, gnomefr]

Travis Atkinson of [Com-Pac Filtration](http://www.com-pac.net) and me have
worked together to find out why the HMI of Weintek Labs I-Series, with Ethernet,
answered only to request sent by the modpoll program (proprietary software).

After many emails and the help of Wireshark, we have discovered modpoll uses the
unit identifier as slave ID for TCP requests, according to
the [Modbus specs](http://www.modbus.org/specs.php) that's incorrect (cf page 23
of Modbus Messaging Implementation Guide v1.0b) but else the device drops the
request!

Two problems can sometimes lead to proper operation or Weintek company has
designed this product on modpoll requests :-/

PS: The workaround was to set the slave ID with `modbus_set_slave()`.
