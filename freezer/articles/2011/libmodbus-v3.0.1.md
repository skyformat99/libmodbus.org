title: libmodbus v3.0.1 to avoid big 0 problems!
published: 2011-07-22
tags: [release]

A dot zero isn't a dot zero without few problems, so I've released
[libmodbus
v3.0.1](https://github.com/downloads/stephane/libmodbus/libmodbus-3.0.1.tar.gz)
to fix problems with non-recent Linux kernels and other platforms.

**libmodbus 3.0.1 (2011-07-18)**

- Avoid useless `serial_mode` integer when *TIOCSRS485* isn't supported
- Fix compilation failure on Windows (RS485 support) by Tobias
  Doerffel
- Properly check TIOCSRS485 define by Matthijs Kool
- Rename package to libmodbus5 to fix lintian warning.
