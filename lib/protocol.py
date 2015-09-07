from Xlib import X
from Xlib.protocol import request
from Xlib.display import Display
from Xlib.xobject.drawable import Window

display = Display()
root = display.screen().root

def get_property(wnd, name):
    type = request.InternAtom(display=wnd.display, name=name, only_if_exists=0).atom
    res = wnd.get_property(type, X.AnyPropertyType, 0, 100)
    if res:
        return res.value
    else:
        return []


def get_naming(atom):
    try:
        return request.GetAtomName(display=display.display, atom=atom).name
    except:
        print(atom)
        return 'UNKNOWN'


def get_pid(wnd):
    ret = get_property(wnd, '_NET_WM_PID')
    return ret[0] if len(ret) > 0 else 0


def get_wnds():
    wnd_ids = get_property(display.screen().root, '_NET_CLIENT_LIST')
    # print(wnd_ids)
    return [display.create_resource_object('window', wid) for wid in wnd_ids]