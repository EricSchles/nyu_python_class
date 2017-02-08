class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
        
    def __str__(self):
        return repr(self.data)

head = Node(0)
x = 1
cur = head
while x <= 20:
    cur.next = Node(x)
    x += 1
    cur = cur.next

cur = head
while cur:
    print(cur)
    cur = cur.next

listing = list(range(21))
for i in listing:
    print(i)
