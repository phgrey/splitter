from subprocess import Popen

# try:
#     from collections import namedtuple
# except ImportError:
#     from namedtuple import namedtuple
# BaseApplet = namedtuple('Applet', 'process window is_ready')


class Applet:

    def __init__(self, **kvargs):
        self.window = None
        self.process = None
        if 'command' in kvargs: self.run(kvargs['command'])
        elif 'window' in kvargs: self.set_window(kvargs['window'])
        else: raise TypeError('Either command, or window attributes are required')

    def run(self, command):
        self.process = Popen([command])

    def set_window(self, window):
        self.window = window
        self.ready()

    def ready(self):
        self.is_ready = True

    @classmethod
    def commands(cls, commands):
        return {cls(command=x) for x in commands}


