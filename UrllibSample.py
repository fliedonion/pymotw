import unittest
from unittest import TestCase

class UrllibSample(object):
    def get(self):
        from urllib import urlopen
        return urlopen("http://www.google.co.jp").read()

    def post(self):
        from urllib import urlopen, urlencode
        params = {'param1':'value1', 'param2':'value2'}
        return urlopen("http://www.case-of-t.net/", urlencode(params))


class UrllibSampleTest(TestCase):
    def testGet(self):
        c = UrllibSample()
        self.assertNotEqual("", c.get())

    def testPost(self):
        c = UrllibSample()
        self.assertNotEqual("", c.post())

