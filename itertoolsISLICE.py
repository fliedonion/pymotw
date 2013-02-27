__author__ = 'takahiro'

import itertools

rtval = ""
def raw_input():
    return rtval

def starting_at_five():
    value = raw_input().strip()
    while value != '':
        for el in itertools.islice(value.split(), 4, None):
            yield el
        value = raw_input().strip()

iter = starting_at_five()
rtval="one two three four five"
print iter.next()
rtval="one"
print iter.next()
rtval="one two three four five six"
print iter.next()
print iter.next()


