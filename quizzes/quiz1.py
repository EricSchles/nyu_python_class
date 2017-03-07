#Question 1 Implement a Node Class for a linked list (singly)

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    #To String 
    def __str__(self):
        return repr(self.data)

#Questions 2-4:

class LinkedList:
    def __init__(self):
        self.head = Node(None)
    #question 2
    def append(self,value):
        if not self.head.data:
            self.head = Node(value)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(value)

    #question 3
    def contains(self, value):
        cur = self.head
        while cur:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    #question 4
    def delete(self,value):
        if self.head.data and not self.head.next:
            self.head = Node(None)
        elif self.head.next.data == value:
            to_delete = self.head.next
            if to_delete.next:
                self.head.next = to_delete.next
                to_delete = None
            else:
                self.head.next = None
        else:
            cur = self.head
            prev = cur
            cur = cur.next
            while cur:
                if cur.value == value:
                    if cur.next:
                        prev.next = cur.next
                        cur = None
                    else: 
                        prev.next = None
                        cur = None
            

#Question 2: Implement an append method (for the end of the list)

#this is the wrong way
head = Node(None)

def append(head,value):
    if not head.data:
        head = Node(value)
    else:
        cur = head
        while cur.next:
            cur = cur.next
        cur.next = Node(value)
    return head


#Extra Credit

class Node:
    def __init__(self,data,next=None, prev=None):
        self.data = data
        self.next = None
        self.prev = None
    def __str__(self):
        return repr(self.data)


# As an exercise implement all the methods associated
