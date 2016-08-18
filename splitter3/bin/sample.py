#!/usr/bin/python3
from lib.applet import Applet
from lib.split import Split
from lib.finder import wnds_by_pids


if __name__ == '__main__':
    applets = Applet.commands({'terminator', 'thunar'})
    apps = {x.process.pid: x for x in applets}
    try:
        wnds_by_pids(set(apps.keys()), lambda pid, w: apps[pid].set_window(w))
        print('all found')
        Split().loop()
    except KeyboardInterrupt: pass
    finally:
        for app in applets:
            app.process.terminate()