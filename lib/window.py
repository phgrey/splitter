from lib.protocol import X, display, request
from select import select

class Window:
    def __init__(self, displ=None, msg='Hello world'):
        self.display = displ or display
        self.msg = msg

        self.screen = self.display.screen()
        self.window = self.screen.root.create_window(
            10, 10, 100, 100, 1,
            self.screen.root_depth,
            background_pixel=self.screen.white_pixel,
            event_mask=X.ExposureMask | X.KeyPressMask,
            )
        self.gc = self.window.create_gc(
            foreground = self.screen.black_pixel,
            background = self.screen.white_pixel,
            )
        request.StoreName(self.display, self.window.id, 'Hi! it\'s me')
        self.window.map()

    def loop(self):
        while True:
            e = self.display.next_event()
            if e.type == X.KeyPress:
                raise SystemExit


    def loop2(self):
        readable = [self.display]
        while True:
            if readable and self.display in readable:
                e = self.display.next_event()
                if e.type == X.KeyPress:
                    raise SystemExit
                print('readable')
            else:
                print('nonreadable')
            readable, w, e = select([self.display], [], [], 1)

if __name__ == "__main__":
    Window().loop()