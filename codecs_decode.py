# coding:utf-8

__author__ = 'takahiro'


from codecs_to_hex import to_hex

text = u'pi: π'

encoded = text.encode('utf-8')
decoded = encoded.decode('utf-8')

print 'Original :', repr(text)
print 'Encoded  :', to_hex(encoded, 1), type(encoded)
print 'Decoded  :', repr(decoded), type(decoded)

