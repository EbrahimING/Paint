# Paint implemented with PYQT5

Hey! Here's a *simple tiny paint implementation project* that I hope it would be useful for you.

So Here we go ..:)

## Files

You may confront **3 files** except this one when you've downloaded the whole repository from *Github*.
The one that called **`paint_pyqt5.py`** contains our main classes for example *Canvas*, *PaletteButton*, *MainWindow*.
Another one called **`paint_stack.py`** has implementation of our stack (which is necessary for having *Undo* & *Redo* functions).
In the last one called **`paint_unredo.py`** , I have implemented a class called *unredo* which contains functions for *Undo* & *Redo* that is connected to our previous file(**`paint_stack.py`**).
> <strong>Tip: </strong> *`paint_stack.py` & `paint_unredo.py` have been imported into the `paint_pyqt5.py`.*

## Classes

||paint_pyqt5.py|paint_stack.py|paint_unredo.py|                   
|-|-|-|-|
|**1**|<center>`Canvas`|<center>`stack_base`|<center>`unredo`|
|**2**|<center>`PaletteButton`|<center>-|<center>-|
|**3**|<center>`MainWindow`|<center>-|<center>-|

## Functions

||paint_pyqt5.py|paint_stack.py|paint_unredo.py|                   
|-|-|-|-|
|**1**|<center>`set_pen_color`|<center>`push`|<center>`push`|
|**2**|<center>`draw_point`|<center>`pop`|<center>`undo`|
|**3**|<center>`draw_line`|<center>`is_empty`|<center>`Catch_clear`|
|**4**|<center>`mousePressEvent`|<center>`Top`|<center>`redo`|
|**5**|<center>`mouseMoveEvent`|<center>`size`|<center>-|
|**6**|<center>`mouseReleaseEvent`|<center>`clear`|<center>-|
|**7**|<center>`undo x2`|<center>-|<center>-|
|**8**|<center>`redo x2`|<center>-|<center>-|
|**9**|<center>`clear x2`|<center>-|<center>-|
|**10**|<center>`save x3`|<center>-|<center>-|
|**11**|<center>`Github`|<center>-|<center>-|
|**12**|<center>`add_palette_button`|<center>-|<center>-|
|**13**|<center>`set_canvas_color`|<center>-|<center>-|

## Shortcuts

|||               
|-|-|
|**Undo**|<center>`Ctrl+Z`|
|**Redo**|<center>`Ctrl+Shift+Z`|
|**Clear**|<center>`Alt+C`|
|**Save**|<center>`Ctrl+S`|

# Brief explanation

This tiny app is a paint with 19 colors, icon, 3 menu bars and these facilities:
- Undo
- Redo
- Clear
- Save ( as `jpg.` or `jpeg.` or `png.` )
- About
- and every other facilities you wanna contribute ;)

`by e2i.ir`
`18/06/22`
