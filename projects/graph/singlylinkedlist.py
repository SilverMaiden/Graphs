class Node :
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def setValue(self, value):
        self.value = value
    
    def setNext(self, next):
        self.next_node = next
    
    def getValue(self):
        print(self.value)
    
    def getNext(self):
        print(self.next)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def setHead(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def addNode(self, node):
        if self.head is None:
            self.head = node
        else: 
            current_node = self.head

            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
    
    
            

