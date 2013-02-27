# -*- coding: utf-8 -*-
__author__ = 'takahiro'

import binascii

def to_hex(t, nbytes):
    """Format t as sequence of nbytes long values separated by spaces"""
    chars_per_item = nbytes * 2
    hex_version = binascii.hexlify(t)
    num_chunks = len(hex_version) / chars_per_item
    def chunkify():
        for start in xrange(0, len(hex_version), chars_per_item):
            yield hex_version[start:start+chars_per_item]
    return ' '.join(chunkify())

if __name__ == '__main__':
    print to_hex("abcdef",1)
    print to_hex("abcdef",2)
    print to_hex(u"あいうえお".encode('cp932'),2)
    print binascii.hexlify(u'あ'.encode('utf7')).upper()

