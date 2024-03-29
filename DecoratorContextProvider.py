__author__ = 'takahiro'

from threading import RLock


lock = RLock()
def synchronized(function):
    def _synchronized(*args, **kw):
        lock.acquire()
        try:
            return function(*args, **kw)
        finally:
            lock.release()
    return _synchronized

@locker
def thread_safe():  # make sure it locks the resource
    pass

