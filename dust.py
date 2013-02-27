#
#
#seq =  ['one', 'two', 'three']
#seq2=range(3)
#
#for i,element in enumerate(seq):
#    seq2[i] = "%d: %s" % (i,element)
#
#print seq2
#
#
#def _treatment(pos, element):
#    return "%d: %s" % (pos, element)
#print [_treatment(i,el) for i, el in enumerate(seq)]
#
#
#f = lambda i, el : "%d: %s" % (i,el)
#print [ f(i,el) for i ,el in enumerate(seq)]
#
#
#print [ (lambda i,el: "%d: %s" % (i,el))(p,e) for p, e in enumerate(seq)  ]
#
#
#print [ "%d: %s" % (i, el) for i,el in enumerate(seq) ]



class MyIterator(object):
    def __init__(self, step):
        self.step = step
    def next(self):
        """Returns the next element. """
        if self.step ==0:
            raise StopIteration
        self.step -=1
        return self.step
    def __iter__(self):
        """Returns the iterator itself. """
        return self

for el in MyIterator(5):
    print el


def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a,b = b, a + b
        if a > 300:
            break


fib = fibonacci()
print fib.next()
print fib.next()
print fib.next()
print [fib.next() for i in range(10)]

for i in fibonacci():
    print i