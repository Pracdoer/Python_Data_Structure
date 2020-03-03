class BST():
    """docstring for BST"""
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.root = None


    def insertion(self, data):   ## Inseration in Tree
    	if self.root == None:
    		self.root = BST(data)
    		return
    	if data < self.data:
    		if self.left is None:
    			self.left = BST(data)
    			return
    		else:
    			self.left.insertion(data)
    			return
    	if data > self.data:
    		if self.right is None:
    			self.right = BST(data)
    			return
    		else: 
    			self.right.insertion(data)
    			return
    	else:
    		self.data = BST(data)
    		return

    def mytree(self):
    	root = self.root
    	mytree = self.root
    	return mytree


    
s1 = BST(6)
s1.insertion(2)
s1.insertion(3)
s1.insertion(4)
mytrr = s1.mytree()
print(mytrr)