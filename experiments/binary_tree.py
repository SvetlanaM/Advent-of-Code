class Node:
  def __init__(self, data):
    self.left = None
    self.right = None 
    self.data = data
  
  def insert(self, data):
    if self.data:
      if data < self.data:
        if self.left is None:         
          self.left = Node(data)
        else:     
          self.left.insert(data)
      elif data > self.data:
        if self.right is None:
          self.right = Node(data)
        else:
          self.right.insert(data)
    else:
      self.data = data


  def print_tree(self):
    if self.left:
      self.left.print_tree()
    if self.right:
      self.right.print_tree()

  def inorderTraversal(self, root):
    res = []
    if root:
      res = self.inorderTraversal(root.left)
      res.append(root.data)
      res = res + self.inorderTraversal(root.right)
    return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.print_tree()
# print(root.inorderTraversal(root)) 