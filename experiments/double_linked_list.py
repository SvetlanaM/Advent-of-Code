from tkinter.tix import DirList


class Node:
  def __init__(self, data):
    self.data = data 
    self.next = None
    self.prev = None 

class doubly_linked_list:
  def __init__(self) -> None:
      self.head = None

  def push(self, NewVal):
    NewNode = Node(NewVal)
    NewNode.next = self.head 
    if self.head is not None:
      self.head.prev = NewNode 
    self.head = NewNode 

  def listprint(self, node):
    while (node is not None):
      print(node.data)
      last = node
      node = node.next

dllist = doubly_linked_list()
dllist.push(12)
dllist.push(8)
dllist.push(4)
dllist.listprint(dllist.head)