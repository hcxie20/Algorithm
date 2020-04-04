class treeNode:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.left = None
        self.right = None

def construct(ls):
  if not ls:
    return None
  
  def insertNode(cur, target):
    if target.a <= cur.a:
      if cur.left == None:
        cur.left = target
      else:
        insertNode(cur.left, target)
    
    else:
      if cur.right == None:
        cur.right = target
      else:
        insertNode(cur.right, target)
  
  ls.sort(key=lambda x: x[1])
  
  root = treeNode(ls[0][0], ls[0][1])
  
  for i in range(1, len(ls)):
    newNode = treeNode(ls[i][0], ls[i][1])
    insertNode(root, newNode)  
  
  return root

construct([[1, 3], [2, 2]])