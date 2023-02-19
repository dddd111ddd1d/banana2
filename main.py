class Tree:
  height = 256.2414
  leafs = 6666667
  age = 101.5
  width = 5.1
  
  def __init__(self, type):
    self.type = type

  def get_older(self):
    self.age += 0.25

  def leafs_fall(self):
    self.leafs += 101
    
  def more_height(self):
    self.height += 1.99


my_tree = Tree("baobab")

print(my_tree.age)
print(my_tree.type)

my_tree.get_older()
print(my_tree.age)