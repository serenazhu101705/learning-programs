Python 3.7.3 (default, Dec 20 2019, 18:57:59) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
==================== RESTART: /home/serena/test_turtle.py ====================
What color would you like the pen to be?
turqoise
Traceback (most recent call last):
  File "/home/serena/test_turtle.py", line 4, in <module>
    t.fillcolor(color)
  File "/usr/lib/python3.7/turtle.py", line 2288, in fillcolor
    color = self._colorstr(args)
  File "/usr/lib/python3.7/turtle.py", line 2696, in _colorstr
    return self.screen._colorstr(args)
  File "/usr/lib/python3.7/turtle.py", line 1158, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: turqoise
>>> 
==================== RESTART: /home/serena/test_turtle.py ====================
What color would you like the pen to be?
light blue

=============================== RESTART: Shell ===============================
>>> import turtle
>>> from turtle import Turtle
>>> from turtle import Screen
>>> screen = Screen()
>>> t = Turtle("turtle")
>>> def dragging(x, y):  # These parameters will be the mouse position
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

    
>>> def clickRight():
    t.clear()

    
>>> def main():  # This will run the program
    turtle.list

    
>>> t.ondrag(dragging)
>>> turtle.onscreenclick(clickRight,3)
>>> screen.mainloop()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    screen.mainloop()
  File "/usr/lib/python3.7/turtle.py", line 813, in mainloop
    TK.mainloop()
  File "/usr/lib/python3.7/tkinter/__init__.py", line 560, in mainloop
    _default_root.tk.mainloop(n)
KeyboardInterrupt
>>> 
==================== RESTART: /home/serena/test_turtle.py ====================
What color would you like the pen to be?
Traceback (most recent call last):
  File "/home/serena/test_turtle.py", line 5, in <module>
    t.color(color)
  File "/usr/lib/python3.7/turtle.py", line 2218, in color
    self.pen(pencolor=pcolor, fillcolor=fcolor)
  File "/usr/lib/python3.7/turtle.py", line 2425, in pen
    self._newLine()
  File "/usr/lib/python3.7/turtle.py", line 3291, in _newLine
    self.screen._drawline(self.currentLineItem, top=True)
  File "/usr/lib/python3.7/turtle.py", line 551, in _drawline
    self.cv.tag_raise(lineitem)
  File "<string>", line 1, in tag_raise
  File "/usr/lib/python3.7/tkinter/__init__.py", line 2602, in tag_raise
    self.tk.call((self._w, 'raise') + args)
_tkinter.TclError: invalid command name ".!canvas"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
** IDLE Internal Exception: 
  File "/usr/lib/python3.7/idlelib/run.py", line 474, in runcode
    exec(code, self.locals)
KeyboardInterrupt
>>> import turtle
>>> t = Screen()
>>> s = Turtle("turtle")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s = Turtle("turtle")
  File "/usr/lib/python3.7/turtle.py", line 3816, in __init__
    visible=visible)
  File "/usr/lib/python3.7/turtle.py", line 2557, in __init__
    self._update()
  File "/usr/lib/python3.7/turtle.py", line 2660, in _update
    self._update_data()
  File "/usr/lib/python3.7/turtle.py", line 2646, in _update_data
    self.screen._incrementudc()
  File "/usr/lib/python3.7/turtle.py", line 1292, in _incrementudc
    raise Terminator
turtle.Terminator
>>> s = Turtle("turtle")
>>> s.speed(-1)
>>> s.fillcolor("light blue")
>>> s.color("light blue")
>>> def dragging(x, y):  # These parameters will be the mouse position
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

    
>>> def clickRight():
    t.clear()

    
>>> def main():  # This will run the program
    turtle.listen()
    
    t.ondrag(dragging)  # When we drag the turtle object call dragging
    turtle.onscreenclick(clickRight, 3)

    screen.mainloop()  # This will continue running main()

    
>>> main()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    main()
  File "<pyshell#26>", line 4, in main
    t.ondrag(dragging)  # When we drag the turtle object call dragging
AttributeError: '_Screen' object has no attribute 'ondrag'
>>> 
==================== RESTART: /home/serena/test_turtle.py ====================
What color would you like the pen to be?
light blue
Traceback (most recent call last):
  File "/home/serena/test_turtle.py", line 38, in <module>
    main()
  File "/home/serena/test_turtle.py", line 36, in main
    screen.mainloop()  # This will continue running main()
  File "/usr/lib/python3.7/turtle.py", line 813, in mainloop
    TK.mainloop()
  File "/usr/lib/python3.7/tkinter/__init__.py", line 560, in mainloop
    _default_root.tk.mainloop(n)
KeyboardInterrupt
>>> 
======================= RESTART: /home/serena/test.py =======================
Traceback (most recent call last):
  File "/home/serena/test.py", line 3, in <module>
    import Tkinter as tkinter
ModuleNotFoundError: No module named 'Tkinter'
>>> import tkinter
>>> 
======================= RESTART: /home/serena/test.py =======================
Traceback (most recent call last):
  File "/home/serena/test.py", line 5, in <module>
    import gobject
ModuleNotFoundError: No module named 'gobject'
>>> import tkinter as tk
>>> window = tk.Tk()
>>> greeting = tk.Label(text="Hello, Tkinter")
>>> greeting.pack()
>>> window.mainloop()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    window.mainloop()
  File "/usr/lib/python3.7/tkinter/__init__.py", line 1283, in mainloop
    self.tk.mainloop(n)
KeyboardInterrupt
end()
import os
import sys
import Tkinter as tkinter

import gobject
import gst

def on_sync_message(bus, message, window_id):
        if not message.structure is None:
            if message.structure.get_name() == 'prepare-xwindow-id':
                image_sink = message.src
                image_sink.set_property('force-aspect-ratio', True)
                image_sink.set_xwindow_id(window_id)

gobject.threads_init()

window = tkinter.Tk()
window.geometry('500x400')

video = tkinter.Frame(window, bg='#000000')
video.pack(side=tkinter.BOTTOM,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)

window_id = video.winfo_id()

player = gst.element_factory_make('playbin2', 'player')
player.set_property('video-sink', None)
player.set_property('uri', 'file://%s' % (os.path.abspath(sys.argv[1])))
player.set_state(gst.STATE_PLAYING)

bus = player.get_bus()
bus.add_signal_watch()
bus.enable_sync_message_emission()
bus.connect('sync-message::element', on_sync_message, window_id)

window.mainloop()
import os
import sys
import Tkinter as tkinter

import gobject
import gst

def on_sync_message(bus, message, window_id):
        if not message.structure is None:
            if message.structure.get_name() == 'prepare-xwindow-id':
                image_sink = message.src
                image_sink.set_property('force-aspect-ratio', True)
                image_sink.set_xwindow_id(window_id)

gobject.threads_init()

window = tkinter.Tk()
window.geometry('500x400')

video = tkinter.Frame(window, bg='#000000')
video.pack(side=tkinter.BOTTOM,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)

window_id = video.winfo_id()

player = gst.element_factory_make('playbin2', 'player')
player.set_property('video-sink', None)
player.set_property('uri', 'file://%s' % (os.path.abspath(sys.argv[1])))
player.set_state(gst.STATE_PLAYING)

bus = player.get_bus()
bus.add_signal_watch()
bus.enable_sync_message_emission()
bus.connect('sync-message::element', on_sync_message, window_id)

window.mainloop()
>>> label = tk.Label(text = "Hello, Tkinter!")
>>> label = tk.Label(
	text = "Hellow, Tkinter",
	foreground = "light blue",
	background = "white")
>>> label = tk.Label(
	text = "Hellow, Tkinter",
	foreground = "light blue",
	background = "white",
	width = 10,
	height = 10)
>>> label.pack()
>>> window.mainloop()

=============================== RESTART: Shell ===============================
>>> import tkinter
>>> import tkinter as tk
>>> window = tk.Tk()
>>> button = tk.Button(text = "click me!",width=25,height=5,bg='light blue',fg='white')
>>> button.pack()
>>> entry = tk.Entry(fg='white',bg='light blue',width=50)
>>> label = tk.Label(text='Name: ',width=25,height=5,bg='light blue',fg='white')
>>> entry = tk.Entry()
>>> label.pack()
>>> entry.pack()
>>> name = entry.get()
>>> name
'Serena'
>>> entry.delete()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    entry.delete()
TypeError: delete() missing 1 required positional argument: 'first'
>>> entry.delete(0)
>>> entry.delete(0,tk.END)
>>> text_box = tk.Text(width=25,height=5,bg='light blue',fg='white')

>>> text_bow.pack()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    text_bow.pack()
NameError: name 'text_bow' is not defined
>>> text_box.pack()
>>> text_bow.get('1.0',tk.END)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    text_bow.get('1.0',tk.END)
NameError: name 'text_bow' is not defined
>>> text_box.get('1.0',tk.END)
'My name is Serena Zhu and I am going to Woodbury High School next year. I am 14 years old and I live in Woodbury Minnesota.\n'
>>> text_box.delete('1.0',tk.END)
>>> 
============== RESTART: /home/serena/python/programs/tkinter.py ==============
Traceback (most recent call last):
  File "/home/serena/python/programs/tkinter.py", line 10, in <module>
    label = tk.label(text = 'Please describe yourself.',width = 100, height = 50, bg = 'light blue',fg = 'white')
AttributeError: module 'tkinter' has no attribute 'label'
>>> 
============== RESTART: /home/serena/python/programs/tkinter.py ==============
Traceback (most recent call last):
  File "/home/serena/python/programs/tkinter.py", line 13, in <module>
    text_bow.pack()
NameError: name 'text_bow' is not defined
>>> 
============== RESTART: /home/serena/python/programs/tkinter.py ==============
Traceback (most recent call last):
  File "/home/serena/python/programs/tkinter.py", line 14, in <module>
    mainloop()
NameError: name 'mainloop' is not defined
>>> 
============== RESTART: /home/serena/python/programs/tkinter.py ==============
>>> 
============== RESTART: /home/serena/python/programs/tkinter.py ==============
>>> tk
<module 'tkinter' from '/usr/lib/python3.7/tkinter/__init__.py'>
>>> label
<tkinter.Label object .!label3>
>>> entry = tk.Entry()
>>> entry.pack()
>>> name = entry.get()
>>> name
'Serena'
>>> greeting = tk.Label(text = 'Welcome' + name)
>>> greeting.pack()
>>> greeting = tk.Label(text = 'Welcome ' + name)
>>> greeting.pack()
>>> 
============== RESTART: /home/serena/python/programs/tkinter.py ==============
>>> 
============== RESTART: /home/serena/python/programs/tkinter.py ==============
Traceback (most recent call last):
  File "/home/serena/python/programs/tkinter.py", line 11, in <module>
    window.destroy()
  File "/usr/lib/python3.7/tkinter/__init__.py", line 2062, in destroy
    self.tk.call('destroy', self._w)
_tkinter.TclError: can't invoke "destroy" command: application has been destroyed
>>> 
============== RESTART: /home/serena/python/programs/tkinter.py ==============
>>> 
============== RESTART: /home/serena/python/programs/tkinter.py ==============
Traceback (most recent call last):
  File "/home/serena/python/programs/tkinter.py", line 9, in <module>
    window.destroy()
  File "/usr/lib/python3.7/tkinter/__init__.py", line 2062, in destroy
    self.tk.call('destroy', self._w)
_tkinter.TclError: can't invoke "destroy" command: application has been destroyed
>>> 
============== RESTART: /home/serena/python/programs/tkinter.py ==============
>>> 
============== RESTART: /home/serena/python/programs/tkinter.py ==============
>>> label = tk.Label(text = 'Please describe yourself.',width = 100, height = 50, bg = 'light blue',fg = 'white')

>>> label.pack()
>>> text_box = tk.Text(width = 100, height = 50, bg = 'light blue',fg = 'white')
>>> text_box.pack()
>>> window.destroy()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    window.destroy()
  File "/usr/lib/python3.7/tkinter/__init__.py", line 2062, in destroy
    self.tk.call('destroy', self._w)
_tkinter.TclError: can't invoke "destroy" command: application has been destroyed
>>> window = tk.Tk()
>>> label.pack()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    label.pack()
  File "/usr/lib/python3.7/tkinter/__init__.py", line 2143, in pack_configure
    + self._options(cnf, kw))
_tkinter.TclError: can't invoke "pack" command: application has been destroyed
>>> label = tk.Label(text = 'Please describe yourself.',width = 100, height = 50, bg = 'light blue',fg = 'white')
>>> )
SyntaxError: invalid syntax
>>> text_box = tk.Text(width = 100, height = 50, bg = 'light blue',fg = 'white')
>>> label.pack()
>>> text_box.pack()
>>> window = tk.Tk()
>>> text_box = tk.Text(width = 100, height = 50, bg = 'light blue',fg = 'white')
>>> text_box.pack()
>>> label.pack()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    label.pack()
  File "/usr/lib/python3.7/tkinter/__init__.py", line 2143, in pack_configure
    + self._options(cnf, kw))
_tkinter.TclError: can't invoke "pack" command: application has been destroyed
>>> label = tk.Label(text = 'Please describe yourself.',width = 100, height = 50, bg = 'light blue',fg = 'white')
>>> label.pack()
>>> 
=============================== RESTART: Shell ===============================
>>> import tkinter as tk
>>> window = tk.Tk()
>>> label = tk.Label(text = 'Name?',width = 10, height = 5, bg = 'light blue',fg = 'white')
>>> entry = tk.Entry()
>>> label.pack()
>>> entry.pack()
>>> name = entry.get()
>>> name
'serena'
>>> greeting = tk.Label(text = 'Welcome ' + name)
>>> greeting.pack()
>>> label = tk.Label(text = 'Please describe yourself.',bg = 'light blue',fg = 'white')
>>> label.pack()
>>> textbox = tk.Text(width = 100, height = 50, bg = 'light blue',fg = 'white')
>>> textbox.pack()
>>> textbox.get()
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    textbox.get()
TypeError: get() missing 1 required positional argument: 'index1'
>>> textbox.get('1.0',tk.END)
'well, my name is serena zhu, I am going to woodbury high school next year, I am 14 years old and I play soccer and basketball. my birthday is october 17th and i have a brother named justin and a sister named joyce.\n'
>>> tk.Message(text = 'Ok')
<tkinter.Message object .!message>
>>> message = tk.Message(text = 'Ok')
>>> message.pack()
>>> window.destroy()
>>> window = tk.Tk()
>>> label = tk.Label(text = 'Name?',width = 10, height = 5, bg = 'light blue',fg = 'white')
>>> entry = tk.Entry()
>>> label.pack()
>>> entry.pack()
>>> name = entry.get()
>>> name
'Serena Zhu'
>>> greeting = tk.Label(text = 'Welcome ' + name)
>>> greeting.pack()
>>> label = tk.Label(text = 'Please describe yourself.',bg = 'light blue',fg = 'white')
>>> label.pack()
>>> textbox = tk.Text(width = 100, height = 50, bg = 'light blue',fg = 'white')
>>> textbox.pack()
>>> textbox.get('1.0',tk.END)
'Well, my name is Serena Zhu and I will be attending Woodbury High School next fall. I am 14 years old and I play soccer and basketball. My birthday is October 17th and I have a sister named Joyce and a brother named Justin. I love listening to music and hanging out with my friends.\n'
>>> tk.Label(text = 'Ok ' + name)
<tkinter.Label object .!label4>
>>> label = tk.Label(text = 'Ok ' + name)
>>> label.pack()
>>> textbox.mainloop()

=============================== RESTART: Shell ===============================
>>> 
============== RESTART: /home/serena/python/programs/tkinter.py ==============
>>> window
<tkinter.Tk object .>
>>> window = tk.Tk()
>>> label = tk.Label(text = "Name?")
>>> label.pack()
>>> entry = tk.Entry()
>>> label.pack()
>>> entry.pack()
>>> window.listen()
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    window.listen()
  File "/usr/lib/python3.7/tkinter/__init__.py", line 2101, in __getattr__
    return getattr(self.tk, attr)
AttributeError: '_tkinter.tkapp' object has no attribute 'listen'
>>> window.wait_variable(name)

=============================== RESTART: Shell ===============================
>>> 
============== RESTART: /home/serena/python/programs/tkinter.py ==============
>>> window.wait_visibility()
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    window.wait_visibility()
  File "/usr/lib/python3.7/tkinter/__init__.py", line 650, in wait_visibility
    self.tk.call('tkwait', 'visibility', window._w)
_tkinter.TclError: can't invoke "tkwait" command: application has been destroyed
>>> window = tk.Tk()
>>> window.wait_visibility()
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    window.wait_visibility()
  File "/usr/lib/python3.7/tkinter/__init__.py", line 650, in wait_visibility
    self.tk.call('tkwait', 'visibility', window._w)
_tkinter.TclError: window "." was deleted before its visibility changed
>>> window.size
<bound method Misc.grid_size of <tkinter.Tk object .>>
>>> import tkinter as tk
>>> def on_change(e):
	print(e.widget.get())

	
>>> root = tk.Tk()
>>> e = tk.Entry(root)
>>> e.pack()
>>> e.bind("<Return>",on_change)
'3066399820on_change'
>>> root.mainloop()
serena
is
awesome
awesomeand
awesomeandso
awesomeandsocool
awesomeandsocoolman

=============================== RESTART: Shell ===============================
>>> 
============== RESTART: /home/serena/python/programs/tkinter.py ==============
>>> 
