class Stack():
    """docstring for Stack"""
    def __init__(self, data):
        self.data = data
        self.next = None 
        


class Stack_Linklist():
    """docstring for Stack_Linklist"""
    def __init__(self):
        self.top = None
        self.stack = None
        
        
    def isEmpty():      ## is Stack empty
        if self.top == None:
            return True


    def push(self,data):    ## Push into Stack
        if self.top == None:
            node = Stack(data)
            node.next = None
            self.stack = node
            self.top = node
            return
        else:
            temp = self.stack
            while temp != self.top:
                temp = temp.next

            temp.next = Stack(data)
            temp.next.next = None
            self.top = temp.next
            return

    def pop(self):      ## Pop from stack
        temp = self.stack
        while temp.next != self.top:
            temp = temp.next
        self.top = temp
        temp.next = None
        return
    
    def top(self):    ## Top of Stack
        return self.top.data
        
        
s1 = Stack_Linklist()
s1.push(3)
s1.push(4)
s1.push(5)
s1.pop()