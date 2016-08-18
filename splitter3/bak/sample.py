#!/usr/bin/python3
from ewmh import EWMH
from Xlib import Xatom, X, display
from Xlib.protocol import request
from Xlib.xobject.drawable import Window
from Xlib.protocol.event import CreateNotify
from subprocess import Popen
from select import select
from pprint import pprint
from lib.window import Window



def get_property(wnd, name):
    type = request.InternAtom(display=wnd.display, name=name, only_if_exists=0).atom
    res = wnd.get_property(type, X.AnyPropertyType, 0, 100)
    if res:
        return res.value
    else:
        return []


def get_naming(atom):
    try:
        return request.GetAtomName(display=d.display, atom=atom).name
    except:
        print(atom)
        return 'UNKNOWN'


def get_pid(wnd):
    ret = get_property(wnd, '_NET_WM_PID')
    return ret[0] if len(ret) > 0 else 0


def check_wnd(window: Window):
    # print('checking wnd ' + get_property(window, '_NET_WM_NAME') + ' ')
    # types = get_property(window, '_NET_WM_WINDOW_TYPE')
    # print(types)
    # print(list(map(get_naming, types)))
    # print(window)
    return get_pid(window) == p1.pid


def got_wnd(window):
    global wnd
    print('window '+ window.get_wm_name())
    wnd = window


def handle_event(event):
    print('checking event ' + event.__class__.__name__)
    if isinstance(event, CreateNotify):
        check_wnd(event.window) and got_wnd(event.window)


def find_by_pid(pid):
    ewmh = EWMH()
    wnds = list(ewmh.getClientList())
    # pprint(wnds)
    matched = list(filter(check_wnd, wnds))
    if matched:
        got_wnd(matched[0])


d = display.Display()
r = d.screen().root
r.change_attributes(event_mask=X.SubstructureNotifyMask | X.StructureNotifyMask)
wnd = None



p1 = Popen(["terminator"])
find_by_pid(p1.pid)
while not wnd:
    # Wait for display to send something, or a timeout of one second
    readable, w, e = select([d], [], [], 1)

    # if no files are ready to be read, it's an timeout
    if not readable:
        # raise TimeoutError('Can not launch subprocess')
        print('non-readable')
        find_by_pid(p1.pid)
    # if display is readable, handle as many events as have been recieved
    elif d in readable:
        i = d.pending_events()
        print('readable')
        while i > 0:
            event = d.next_event()
            handle_event(event)
            i -= 1



Window().loop()

p1.terminate()

while 1: pass