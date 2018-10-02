
from __future__ import print_function


from threading import Timer


def hello():
    print("Hello World!")


class RepeatingTimer(object):

    def __init__(self, interval, f, *args, **kwargs):
        self.interval = interval
        self.f = f
        self.args = args
        self.kwargs = kwargs

        self.timer = None


    def callback(self):
        self.f(*self.args, **self.kwargs)
        self.start()

    def cancel(self):
        self.timer.cancel()

    def start(self):
        self.timer = Timer(self.interval,self.f)
        self.timer.start()
    def run(self):
        self.timer.run()



t = RepeatingTimer(3, hello)
print(t.run())
t.start()
print("d")
print(t.run())
