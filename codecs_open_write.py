
__author__ = 'takahiro'

from codecs_to_hex import to_hex

import codecs
import sys

encoding = sys.argv[1]

filename = encoding + '.txt'

print  'Writing to ', filename
with codecs.open(filename, mode='wt', encoding = encoding) as f:
    f.write(u'pi: \u03c0')

nbytes = { 'utf-8':1,
           'utf-16':2,
           'utf-32':4,
        }.get(encoding, 1)

# Show the raw bytes in the file
print "File contens:"
with open(filename, mode='rt') as f:
    print to_hex(f.read(), nbytes)
