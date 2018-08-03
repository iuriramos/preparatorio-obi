'''Tree Datastructure'''

class TreeNode:
    '''Binary Tree Node Class'''
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class Tree:
    '''Binary Search Tree Class'''
    
    def __init__(self):
        self.root = None
        
    def get(self, key):
        node = self._get(self.root, key)
        return node.val if node else None
        
    def _get(self, node, key):
        if not node:
            return None
        node_key = node.key
        if node_key == key:
            return node
        elif node_key < key: # key is on the right subtree
            return self._get(node.right, key)
        else: # key < node_key, key is on the left subtree
            return self._get(node.left, key)
            
    def set(self, key, val):
        self.root = self._set(self.root, key, val)
        
    def _set(self, node, key, val):
        if not node:
            return TreeNode(key, val)
        node_key = node.key
        if node_key == key:
            node.val = val
        elif node_key < key: # key is on the right subtree
            node.right = self._set(node.right, key, val)
        else: # key is on the left subtree
            node.left = self._set(node.left, key, val)
        return node
        
    def exists(self, key):
        return self.get(key) is not None
        
    def remove(self, key):
        self.root = self._remove(self.root, key)
        
    def _remove(self, node, key):
        if not node:
            return None
        node_key = node.key
        if node_key < key: # right subtree
            node.right = self._remove(node.right, key)
            return node
        elif key < node_key: # left subtree
            node.left = self._remove(node.left, key)
            return node
        else: # found node
            if not node.left and not node.right: # leaf node
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            else: # has left and right subtrees
                next_node = node.right
                while next_node.left:
                    next_node = next_node.left
                node.key, next_node.key = next_node.key, node.key
                node.val, next_node.val = next_node.val, node.val
                node.right = self._remove(node.right, key)
                return node
        
    def previous(self, key):
        node = self._previous(self.root, key)
        return node.key if node else None
        
    def _previous(self, node, key):
        if not node:
            return None
        node_key = node.key
        if node_key >= key:
            return self._previous(node.left, key)
        else: # node_key < key:
            right = self._previous(node.right, key)
            return right or node    
        
