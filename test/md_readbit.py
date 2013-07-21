#!/usr/bin/env python
import minimalmodbus

x = minimalmodbus.Instrument('/dev/ttyUSB0', 1) 
x.serial.parity = 'E'

print x.read_bit(0, 1)
print x.read_bit(1, 1)
print x.read_bit(31, 1)

print 

print x.read_bit(0, 2)
print x.read_bit(2, 2)
print x.read_bit(15, 2)

print

print x.read_bit(0, 1)
print x.write_bit(0, 1, 5)
print x.read_bit(0, 1)
print x.write_bit(0, 0, 5)

print

print x.read_bit(0, 1)
print x.write_bit(0, 1, 15)
print x.read_bit(0, 1)
print x.write_bit(0, 0, 15)
