title: Magic libmodbus v3.0.0 is out
published: 2011-07-12
tags: [release]

OK, the new stable release of libmodbus is finally out! Two years after
libmodbus v2.0.3 and 400 commits, I'm happy to release this new version which
contains many changes to improve the API and enhance the Modbus protocol
conformity. The major features of this release are:

- more coherent and extended API
-  POSIX error return codes
-  full documentation of the API
-  IPv6 support
-  new backend design
-  support for Windows, MacOS X and FreeBSD
-  rewriting of the message reading to avoid timeout
-  native serial communication on Windows

**Thanks to the many contributors**

Tobias Doerffel, Florian octo Forster, Hannu Vuolasaho, Patsy Kaye, Ivo
De Decker, Allan Cornet, Manfred Gruber, Jason Oster, Petr Parýzek,
Antti Manninen, Barry Grumbine, Kirill Smelkov, Anibal Limón, David
Olivari, Sisyph, aladdinwu, Jeff Laughlin, Yishin Li , Henrik Munktell,
Paul Fertser, Norbert Koch and Stéphane Raimbault.

The development continues for the next v3.1 release with this
[roadmap][]. Have fun!

[roadmap]: https://github.com/stephane/libmodbus/wiki/Roadmap
