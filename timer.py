from threading import Timer
import time

class RepeatableTimer(object):
    def __init__(self, interval, function, args=[], kwargs={}):
        self._interval = interval
        self._function = function
        self._args = args
        self._kwargs = kwargs
    def start(self):
        self.t = Timer(self._interval, self._function, *self._args, **self._kwargs)
        self.t.start()
    def stop(self):
        self.t.cancel()
    def alive(self):
        print(self.t.is_alive())


def hello():
    print ("hello")

a=RepeatableTimer(3,hello)

for i in range(1,5):
    print(i)
    a.start()
    time.sleep(1)
    if i == 3:
        a.stop()
    a.alive()



