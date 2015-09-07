from .protocol import root, display, get_pid, get_wnds, X
from select import select


def wnds_by_pids(pids, callback):
    root.change_attributes(event_mask=X.SubstructureNotifyMask | X.StructureNotifyMask)
    known = set()

    def check_all(wnds = None):
        wnds = wnds or get_wnds()
        known.update({check(x) for x in wnds})

    def check(w):
        if w.id in known: return w.id
        pid = get_pid(w)
        if pid in pids:
            callback(pid, w)
            pids.remove(pid)
        return w.id

    check_all()

    while len(pids) > 0:
        readable, w, e = select([display], [], [], 1)
        if not readable:
            # print('non-readable')
            check_all()
        elif display in readable:
            i = display.pending_events()
            # print('readable')
            while i > 0:
                event = display.next_event()
                if event.type == X.CreateNotify: check_all({event.window})
                i -= 1