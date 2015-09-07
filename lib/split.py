from .protocol import X, display, request


class Split:
    def __init__(self):
        self.display = display
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
        self.window.map()

    def loop(self):
        while True:
            e = self.display.next_event()
            if e.type == X.KeyPress:
                raise SystemExit
