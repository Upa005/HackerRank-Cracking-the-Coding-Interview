""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

a = []
def form_list(root):
    if root:
        form_list(root.left)
        a.append(root.data)
        form_list(root.right)
    return  

def check_binary_search_tree_(root):
    form_list(root)
    #print a
    for i in range(len(a)-1):
        if a[i]>= a[i+1]:
            return False
    return True    
  