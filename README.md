SUMMARY:
basicly this is a probe of make not tiling wm, but window with tiled parts management

#first try
splitter3 - xlib, python, gtk, xprop

gem wmctrl - тоже возможности для command-line dpfbvjltqcndbz

#next way
devilspy (devilspy2) + gdevilspy - a way to operate windows

gem shoes - a way to create own app with gui

#chrome way
u should use terminal console and make it multiterminal perhaps. via extensions coding


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