class Node:
    """ddatatring for node"""
    def __init__(self, data):    ## Constructor
        self.data = data
        self.next = None
        self.perv = None


    def Get_data(self):        ## Get data
        return self.data

    def Set_data(self, data):  ## Set data
        self.data = data


    def Get_next(self):        ## Get next
        return self.next

    def Set_next(self, node):        ## Set next
        self.next = node


#--------------- Link List ---------------#

class doubly_LinkList:
    """docstring for ClassName"""
    def __init__(self):       # Constructor
        self.head = None

    def isEmpty(self):       # Link List is Empty or not
        if self.head == None:
            return True


    def add(self, data):    # Adding nodes
        if self.head == None:
            node = Node(data)
            self.head = node
            return
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(data)
            temp.next.next = None
            temp.next.perv = temp



    def remove(self, data):   ## Remove First accurance of node
        temp = self.head
        while temp.next is not self.head:
            if(temp.next.Get_data() == data):
                temp2 = temp.next
                temp.Set_next(temp.next.Get_next())
                temp.next.perv = temp2.perv
                return

    def traversal(self):   ## Traverse the link list
        temp = self.head
        while temp is not None:
            print(temp.Get_data(temp))
            temp = temp.Get_next()
        return
    



def main():
    dll = doubly_LinkList()
    dll.add(3)
    dll.add(4)
    dll.add(5)
    # dll.traversal()
    # dll.remove(4)
    # dll.traversal()
    return


if __name__== "__main__":
  main()