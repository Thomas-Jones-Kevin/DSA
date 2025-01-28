#Binary Tree
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self.val
    

A = TreeNode(4)
B = TreeNode(5)
C = TreeNode(2)
D = TreeNode(7)
E = TreeNode(3)

A.left = B
B.left = E
A.right = C
C.right = D

#in order
def inorder(root):
    if not root:
        return
   
    inorder(root.left)
    print(root.val)
    inorder(root.right)

print("Inorder : ")
inorder(A)

#pr eorder
def preorder(root):
    if not root:
        return 
    
    print(root.val)
    preorder(root.left)
    preorder(root.right)

print("Preorder : ")
preorder(A)

#post order
def postorder(root):
    if not root:
        return 
    
    postorder(root.left)
    postorder(root.right)
    print(root.val)

print("Postorder : ")
postorder(A)

#dfs
def dfs(root):
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

print("DFS : ")
dfs(A)

#bfs
from collections import deque
def bfs(root):
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

print("BFS : ")
bfs(A)

#search for an element
def search(root,target):
    if not root:
        return False
    
    if root.val==target:
        return True
    
    return search(root.left,target) or search(root.right,target)

print("Search : ")
print(search(A,7))



