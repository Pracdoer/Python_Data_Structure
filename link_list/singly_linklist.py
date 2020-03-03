        
class Node:
    """ddatatring for node"""
    def __init__(self, data):    ## Constructor
        self.data = data
        self.next = None


    def Get_data(self):        ## Get data
        return self.data

    def Set_data(self, data):  ## Set data
        self.data = data


    def Get_next(self):        ## Get next
        return self.next

    def Set_next(self, node):        ## Set next
        self.next = node


#--------------- Link List ---------------#

class singly_LinkList:
    """docstring for ClassName"""
    def __init__(self):       ## Constructor
        self.head = None

    def isEmpty(self):       ## Link List is Empty or not
        if self.head == None:
            return True


    def add(self, data):    ## add a Node
        node = Node(data)
        node.Set_next(self.head)
        self.head = node

    def remove(self, data):   ## Remove First accurance of node
        temp = self.head
        while temp.next is not None:
            if(temp.next.Get_data() == data):
                temp.Set_next(temp.next.Get_next())
                return

    def search(self, data):    ## Search an element in node
    	temp = self.head
    	while temp is not None:
    		if(temp.Get_data() == data)
    			return True
    	else:
    		return False


    def traversal(self):   ## Traverse the nodes (Printing)
        temp = self.head
        while temp is not None:
            print(temp.Get_data())
            temp = temp.Get_next()
        return


  
# ------- Main function -----#

def main():
    ll = singly_LinkList()
    ll.add(3)
    ll.add(4)
    ll.add(5)
    ll.remove(4)
    return


if __name__== "__main__":
  main()