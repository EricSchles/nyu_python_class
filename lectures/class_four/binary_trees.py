class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return repr(self.data)

def BinaryTree:
    def __init__(self):
        self.head = Node(None)

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            self._append(cur,data)
            
    def _append(self,cur,data):
        if cur:
            if cur.right:
                if not cur.left:
                    cur.left = Node(data)
                else:
                    self._append(cur.right,data)
            else:
                cur.right = Node(data)

    def printer(self):
        if self.head:
            cur = self.head
            self._printer(cur)
            
    def _printer(self,cur):
        if cur.left:
            self._printer(cur.left)
        print(cur)
        if cur.right:
            self._printer(cur.right)
            
