from .protocol import X, display, Window
from .applet import Applet
from .utils import EventLoop


class Palette():
    """
    :type window: Window
    """
    mask = X.KeyPressMask | X.ExposureMask

    def __init__(self):
        super().__init__()
        self.display = display
        self.screen = self.display.screen()
        self.root = self.screen.root
        self.window = self.root.create_window(
            10, 10, 100, 100, 1,
            self.screen.root_depth,
            background_pixel=self.screen.white_pixel,
            event_mask=self.mask,
            )
        self.gc = self.window.create_gc(
            foreground = self.screen.black_pixel,
            background = self.screen.white_pixel,
            )
        self.applets = []
        self.window.map()
        # self.event_add(lambda e: self.close() if e.type == X.DestroyNotify else None, X.StructureNotifyMask)
        # self.run_applets(['terminator', 'terminator', 'terminator'])
        # self.run_applets(['terminator'])
        self.loop()

    def close(self):
        raise SystemExit

    def run_applets(self, commands):
        self.applets = [Applet(command=x) for x in commands]
        a = self.applets[0]
        self.intercept_add(a.process.pid, a.set_window)
        # map(self.intercept, self.applets)
        # for applet in self.applets: self.intercept(applet)

    def loop(self):
        while True:
            e = self.display.next_event()
            if e.type == X.KeyPress:
                raise SystemExit
    #this is runned processes window interceptor

    #here we are with event looper
