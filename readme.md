To read:
http://www.pygtk.org/pygtk2tutorial/index.html                          pugtk2+
http://www.sbin.org/doc/Xlib/chapt_08.html                              xlib
http://python-xlib.sourceforge.net/doc/html/python-xlib_11.html#SEC10   pyxlib
https://pypi.python.org/pypi/ewmh                                       uses xlib, very helpful when trying to understand it

#short references
 - поиск PID процесса активного окна
xprop -id $(xprop -root | awk '/_NET_ACTIVE_WINDOW\(WINDOW\)/{print $(NF-1)}') | awk '/_NET_WM_PID\(CARDINAL\)/{print $(NF)}'
 - X11 properties and selections

Конкуренты возможно
http://help.ubuntu.ru/wiki/devilspie

To do:
wmctrl operating
devilspy operating
у xprop забрать стартовое выделение окна (когда без параметров запущен)


залипание, желательно методами иксов, а еще лучше - dockable окна

скайптаб свой

Deskboard creation app
Clipboard and selections are also used





requirements:
sudo apt-get install wmctrl