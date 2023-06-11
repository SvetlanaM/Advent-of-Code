class Node:
    def __init__(self, dataval: None) -> None:
        self.dataval = dataval
        self.nextval = None
    
class SLinkedList:
    def __init__(self):
        self.headval = None

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return 
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode

    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The node is absent")
            return
        
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    
    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def RemoveNode(self, RemoveKey):
        HeadVal = self.headval 

        if (HeadVal is not None):
            if (HeadVal.dataval == RemoveKey):
                self.headval = HeadVal.nextval
                HeadVal = None 
                return
        while (HeadVal is not None):
            if HeadVal.dataval == RemoveKey:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval
        
        if (HeadVal == None):
            return
        
        prev.nextval = HeadVal.nextval
        HeadVal = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list1.headval.nextval = e2
e2.nextval = e3

list1.AtBegining("Sun")
list1.AtEnd("Thu")
list1.Inbetween(list1.headval.nextval, "Fri")
list1.RemoveNode("Tue")
list1.listprint()