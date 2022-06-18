class stack_base:
    s = None
    def __init__(self):
        self.s= list()
    def push(self ,data):
        self.s.append(data)
        return True
    def pop(self):
        return self.s.pop()
    def is_empty(self): 
        if len(self.s)==0: # or it can be like this : if self.s==[]: ..... 
            return True
        else:
            return False
    def Top(self):
        return self.s[-1]
    def size(self):
        return len(self.s)
    def clear(self):
        self.s.clear() # or it can be like this : self.s=[]
    # parantheses are not important...