from lib.palette import Palette
from lib.utils import Catcher
from lib.applet import Applet

# Palette()


catch = Catcher(autostart=True)
a = Applet(command='terminator')
catch.intercept(a)

print(a.window)


Palette()


while 1:pass

a.process.terminate()