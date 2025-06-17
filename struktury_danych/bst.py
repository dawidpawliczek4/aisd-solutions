from typing import List, Tuple, Union
opt = Union[None, 'Node']


class Node: 
    def __init__(self, val: int, l: opt = None, r: opt = None):
        self.val = val 
        self.l = l 
        self.r = r

class BST:
    def __init__(self):
        self.root: opt = None
        
    def insert(self, val: int) -> None:
        def _insert(node: opt) -> Node:
            if node == None:
                return Node(val)
            elif val < node.val:
                return Node(node.val, _insert(node.l), node.r)
            else:
                return Node(node.val, node.l, _insert(node.r))
            
        self.root = _insert(self.root)
    
    def delete(self, val: int) -> None:
        def _get_min(node: Node) -> int:
            if node.l:
                return _get_min(node.l)
            else:
                return node.val
        
        def _delete(node: Node, val) -> opt:
            if val == node.val: 
                if node.l == None and node.r == None: # both sons are Nil
                    return None
                elif node.l == None:                  # l son is Nil
                    return node.r 
                elif node.r == None:                  # r son in Nil
                    return node.l 
                else:                                 # non of sons are Nil
                    min_val = _get_min(node.r)
                    return Node(min_val, node.l, _delete(node.r, min_val))
                
            elif val < node.val and node.l:
                return Node(node.val, _delete(node.l, val), node.r)
            
            elif node.r:
                return Node(node.val, node.l, _delete(node.r, val))
        
        if self.root and self.contains(val): 
            self.root = _delete(self.root, val)
    
    def contains(self, val: int) -> bool:
        def _contains(node: opt) -> bool:
            if node == None:
                return False 
            elif node.val == val:
                return True 
            elif val < node.val:
                return _contains(node.l)
            else:
                return _contains(node.r)
       
        return _contains(self.root) 
    
    def print(self) -> None:
        def _print(node: opt) -> str: 
            if node == None:
                return "()"
            else:
                return f"[{node.val}, {_print(node.l)}, {_print(node.r)}]"
            
        print(_print(self.root))

if __name__ == '__main__':
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(9)
    bst.print()
    
    bst.delete(5)
    bst.print()
    
    