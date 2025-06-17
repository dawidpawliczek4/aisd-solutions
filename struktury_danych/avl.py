from typing import Tuple, List, Union 
opt = Union[None, 'Node']

class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.l: opt = None 
        self.r: opt = None 
        
        self.h = 1
    
    #! rotations  
    def rotate_left(self) -> 'Node':
        if self.r == None:
            return self 
        
        other: Node = self.r 
        self.r = other.l 
        
        other.l = self 
        
        self.update_h()
        other.update_h() 
        return other
    
    def rotate_right(self) -> 'Node':
        if self.l == None:
            return self
        
        other: Node = self.l 
        self.l = other.r 
        
        other.r = self
        
        self.update_h()
        other.update_h() 
        return other
    
    #! getters
    @staticmethod 
    def get_h(node: opt) -> int:
        if node:
            return node.h 
        else: 
            return 0
        
    def get_bf(self) -> int:
        lh = Node.get_h(self.l)
        rh = Node.get_h(self.r)
        return rh - lh

    #! utils
    def update_h(self) -> None:
        lh = Node.get_h(self.l)
        rh = Node.get_h(self.r)
        
        self.h = max(lh, rh) + 1
        
    def update_balance(self) -> 'Node':
        self.update_h()
        bf = self.get_bf()
        
        if bf < -1:
            if self.l and self.l.get_bf() > 0:
                self.l = self.l.rotate_left()
            return self.rotate_right()
        elif bf > 1:
            if self.r and self.r.get_bf() < 0:
                self.r = self.r.rotate_right()
            return self.rotate_left()
        
        return self

class AVL: 
    def __init__(self) -> None:
        self.root: opt = None
        
    def insert(self, val: int) -> None:
        def _insert(node: opt) -> Node:
            if node == None:
                return Node(val)
            elif val < node.val:
                node.l = _insert(node.l) 
            else:
                node.r = _insert(node.r)
                
            node = node.update_balance()
            node.update_h()
            
            return node 
        
        self.root = _insert(self.root)
    
    def delete(self, val: int) -> None:
        
        def _get_min(node: Node) -> int:
            if node.l: 
                return _get_min(node.l) 
            else:
                return node.val
            
        def _delete(node: opt, val) -> opt:
            if node == None:
                return None
            
            elif node.val == val: 
                if node.l == None and node.r == None: # both sons are Nil
                    return None 
                elif node.l == None: # l son is Nil 
                    return node.r 
                elif node.r == None: # r son is Nil
                    return node.l 
                else:
                    min_val = _get_min(node.r)
                    
                    new_node = Node(min_val)
                    new_node.l = node.l 
                    new_node.r = _delete(node.r, min_val)
                    
                    return new_node
            
            elif node.l and val < node.val:
                node.l = _delete(node.l, val)
            
            elif node.r:
                node.r = _delete(node.r, val)

            if node: 
                node = node.update_balance()
                node.update_h()
                
            return node
            
        if self.contains(val):
            self.root = _delete(self.root, val)
    
    def contains(self, val: int) -> bool:
        def _contains(node: opt) -> bool:
            if node == None:
                return False 
            elif val == node.val:
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
    avl = AVL()
    avl.insert(5)
    avl.insert(2)
    avl.print()
    
    avl.insert(1)
    avl.print()
    
    avl.delete(2)
    avl.print()
    