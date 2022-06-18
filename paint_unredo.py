import paint_stack
from PyQt5.QtWidgets import * # for Qapplication.beep()

class unredo:
    Main = None
    Catch = None
    def __init__(self):
        self.Main = paint_stack.stack_base()
        self.Catch = paint_stack.stack_base()
    def push(self, value):
        self.Main.push(value)
        if not self.Catch.is_empty():
            self.Catch.clear()
    def undo(self):
        if(self.Main.size() > 1):
            self.Catch.push(self.Main.pop())
            return self.Main.Top()
        elif(self.Main.size() == 1):
            QApplication.beep() # beep
            return False
    def Catch_clear(self):
        self.Catch.clear()
    def redo(self):
        if(not self.Catch.is_empty()):
            self.Main.push(self.Catch.pop())
            return self.Main.Top()
        else:
            QApplication.beep() # beep
            # to notify user that the action is not continuable ...
            return False