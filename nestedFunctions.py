__author__ = 'takahiro'


var1 = 10
f = None

def func():
    print var1

def func2():
    global f
    f = func
    f()

def func3():
    def func3_1(arg1):
        print arg1

    def func3_2():
        def func3_2_1():
            print var1
        global f
        f = func3_2_1

    global f
    f = func3_1
    return func3_2




if __name__ == '__main__':
    #func()
    func2()
    f()
    print "call func3()()"
    func3()()
    #f("call from __main__")
    print "call f()"
    f()
