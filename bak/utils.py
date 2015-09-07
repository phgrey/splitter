from .applet import Applet
from . import protocol
from .protocol import X, root



from select import select

debug = print


class EventLoop(object):
    def __init__(self, window=None, *args, **kvargs):
        self.mask = 0
        self.callbacks = set()
        self.window = window or root
        self.display = self.window.display
        # super(self, object).__init__(self, *args, **kvargs)
        EventLoop._instance = self


    def event_add(self, cb, mask=0):
        if mask:
            mask = self.mask | mask
            if self.mask != mask:
                self.mask = mask
                self.window.change_attributes(event_mask=mask)
        self.callbacks.add(cb)
        if len(self.callbacks) == 1: self.loop()

    def event_remove(self, cb):
        self.callbacks.remove(cb)


    def handle_event(self, e):
        to_del = set()
        for c in self.callbacks:
            res = c(e)
            if res == 'delete': to_del.add(c)
        self.callbacks = self.callbacks - to_del

    def loop(self):
        readable = [self.display]
        while len(self.callbacks) > 0:
            if readable and self.display in readable:
                event = self.display.next_event()
                self.handle_event(event)
                debug('readable')
            else:
                debug('nonreadable')
            readable, w, e = select([self.display], [], [], 1)
            # readable, w, e = select([self.display], [], [], 1)
            # if self.display in readable:
            #     i = self.display.pending_events()
            #     debug('readable', i)
            #     while i > 0:
            #         event = self.display.next_event()
            #         self.handle_event(event)
            #         i -= 1
    @staticmethod
    def get_instance():
        return EventLoop._instance or EventLoop()

EventLoop._instance = None


class Catcher:
    looking = {}
    found = {}

    def __init__(self, looper=None, autostart=False):
        self.looper = looper or EventLoop.get_instance()
        self.root = root
        self.autostart = autostart

    def intercept(self, a: [Applet]):
        self.intercept_add(a.process.pid, lambda w: a.set_window(w))

    def intercept_add(self, pid, cb):
        self.looking[pid] = cb
        if len(self.looking) == 1:
            window = self.intercept_start(pid)
            if window: return cb(window)


    def intercept_start(self, pid):
        if len(self.found) == 0:
            self.found = {protocol.get_pid(x): x for x in protocol.get_wnds()}
        if pid in self.found: return self.found[pid]
        self.root.change_attributes(event_mask=X.SubstructureNotifyMask)
        self.added_event = lambda w: self.intercept_check(w)
        self.looper.event_add(self.added_event)


    def intercept_check(self, e):
        debug('checking event ' + e.__class__.__name__, e.type == X.CreateNotify)
        if e.type == X.CreateNotify:
            pid = protocol.get_pid(e.window)
            if pid in self.looking:
                self.intercept_got(pid, e.window)
                if len(self.looking) == 0: return self.intercept_stop()
            else: debug('Unknown pid', pid, self.looking.keys())


    def intercept_got(self, pid, window):
        self.looking[pid](window)
        del(self.looking[pid])
        self.found[pid] = window
        debug('got window '+str(pid))


    def intercept_stop(self):
        self.root.change_attributes(event_mask=0)
        return 'delete'


