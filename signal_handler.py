import signal
import sys
import time
class test(object):
    def test(self):
        print self.returnstack([])

    def returnstack(self, nlist):
        for i in range(5):
            nlist.append(i)
        print nlist
        return nlist

if __name__ == "__main__":
    s = test()
    s.test()