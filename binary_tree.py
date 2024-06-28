class TreeNode:
    
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
    
"""
Build tree
"""
def build_tree():
    node_1 = TreeNode(8)
    node_2 = TreeNode(3)
    node_3 = TreeNode(10)
    node_4 = TreeNode(1)
    node_5 = TreeNode(6)
    node_6 = TreeNode(14)
    node_7 = TreeNode(4)
    node_8 = TreeNode(7)
    node_9 = TreeNode(13)
    
    """
        node_1
        /   |
    node_2  node_3
    """
    node_1.left = node_2
    node_1.right = node_3
    
    node_2.left = node_4
    node_2.right = node_5
    
    node_3.right = node_6
    
    node_5.left = node_7
    node_5.right = node_8
    
    node_6.left = node_9
    
    return node_1


def pre_order_traverse_tree(root):
    # if root is None => return
    if not root:
        return
    print(root.val, end=" ")
    
    pre_order_traverse_tree(root.left)
    pre_order_traverse_tree(root.right)
    
def in_order_traverse_tree(root):
    # if root is None => return
    if not root:
        return
    
    
    in_order_traverse_tree(root.left)
    print(root.val, end=" ")
    in_order_traverse_tree(root.right)
    
def post_order_traverse_tree(root):
    # if root is None => return
    if not root:
        return
    
    
    post_order_traverse_tree(root.left)
    post_order_traverse_tree(root.right)
    print(root.val, end=" ")
    



if __name__ == '__main__':
    root = build_tree()
    print("Pre-order traverse: ")
    pre_order_traverse_tree(root)
    
    print("In-order traverse: ")
    in_order_traverse_tree(root)
    
    print("Post-order traverse: ")
    post_order_traverse_tree(root)