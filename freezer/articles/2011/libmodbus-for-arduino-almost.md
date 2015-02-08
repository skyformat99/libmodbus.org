title: libmodbus for Arduino (almost!)
published: 2011-04-14
tags: [libmodbus, arduino]

The libmodbus project is a real success on many platforms and to conquer
the world, I've written a version dedicated to Arduino devices. My goals
are:

- to talk with a standard Arduino UNO or Duemilanove via the integrated USB
  serial line (8N1)
- to have the lowest footprint (binary sketch size and SRAM)
- to be robust

OK, you're right, other projects exist already:

- [Master/slave](http://sites.google.com/site/jpmzometa) by jpmzometa and others
  is great but the reading in loop doesn't handle serial latency and the code
  contains too many arrays IMHO
- [ModbusMaster](http://arduino.cc/playground/Code/ModbusMaster) is a master and
  I want a slave.
- `Arduino-Modbus`, the code is, eh, ugly!
- [modbusmq](https://code.launchpad.net/modbusmq/) by Mario Di Bacco is based on
  libmodbus but it aims Modbus TCP.

So I've extracted/adapted only the slave, RTU, reading/writing registers
of libmodbus. To reduce the footprint even further, I've replaced the
fast CRC code based on precomputed arrays (512 bytes) by a slow one (not
so slow!). The result is clean library for Arduino able to handle
exceptions if an error occurs.

The binary sketch size is 2,450 bytes and around 1,830 bytes of memory
still free when running on 2K SRAM model.

The source code is available on
[github](https://github.com/stephane/modbusino) and have the project is
referenced in the arduino.cc
[playground](http://arduino.cc/playground/Main/InterfacingWithHardware)
wiki.
