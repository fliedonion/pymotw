__author__ = 'takahiro'

import struct
import binascii

values = (1, 'ab', 2.7 )
s = struct.Struct('I 2s f')
packed_data = s.pack(*values)

print 'Original values:', values
print 'Format string  :', s.format
print 'uses           :', s.size, 'bytes'
print 'Packed Value   :', binascii.hexlify(packed_data)

