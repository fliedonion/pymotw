__author__ = 'takahiro'

hosts = file('/etc/hosts')
try:
    for line in hosts:
        if line.startswith("#"):
            continue
        print line
finally:
    hosts.close()

with file('/etc/hosts') as hosts:
    for line in hosts:
        if line.startswith("#"):
            continue
        print line


class Context(object):
    def __enter__(self):
        print 'entering the zone'
    def __exit__(self, exception_type, exception_value, exception_traceback):
        print 'leaving the zone'
        if exception_type is None:
            print 'with no error'
        else:
            print 'with an error (%s)' % exception_value

with Context():
    print 'i am the zone'


try:
    with Context():
        print 'i am the buggy zone'
        raise TypeError('i am the bug')
except:
    pass

# with contextlib module
from contextlib import contextmanager
@contextmanager
def context():
    print 'entering the zone'
    try:
        yield
    except Exception , e:
        print 'with an error (%s)' % e
        # we need to re-raise here
        raise e
    else:
        print 'with no error'


with context():
    print 'i am the zone'

try:
    with context():
        print 'i am the buggy zone'
        raise TypeError('decorator ')
except:
    pass