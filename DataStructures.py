#lists are ordered collection of objects
a = [1,2,3,4]
print(type(a))
print(a)
#lists use indexing
print(a[1])

#tuples are ordered collection of objects
b = (1,2,3,4)
print(type(b))
print(b)
#lists use indexing
print(b[3])

d = dict()
d[5] = 'five'
d[2] = 'two'
d['pi'] = 3.14159
print(d)
print(d['pi'])

class Vector:
    def __init__(self, x, y):
        try:
            self.x = float(x)
        except ValueError:
            self.x = 0.0
        try:
            self.y = float(y)
        except ValueError:
            self.y = 0.0

    def norm(self):
        return (self.x**2 + self.y**2) ** 0.5
    
u = Vector("a", 6)
print(u.norm())
print(Vector(5,12).norm())

class Diary:
    def __init__(self, title):
        self.title = title
        self._entries = []
    
    def addentry(self,entry):
        self._entries.append(entry)
    
    def _lastentry(self):
        return self.entries[-1]

myDiary = Diary("Don't read this! ")
myDiary.addentry("It was a good day.")
print("This diary is called ", myDiary.title)

class Polygon:
    def __init__(self,sides,points):
        self._sides = sides
        self._points = list(points)
        if len(self._sides) != self._sides:
            raise ValueError("wrong number of points")

    def sides(self):
        return self._slides
    
class Triangle(Polygon):
    def __init__(self, points):
        Polygon.__init__(self, 3, points)
    
    def __str__(self):
        return "I'm a triangle"

class Square(Polygon):
    def __init__(self, points):
        Polygon.__init__(self, 4, points)
    
    def __str__(self):
        return "I'm a square"
    
#methods in a stack include push, pop, peek, length, size, isempty
#implementing the stack data sturcture as a list
#LIFO = Last in first out
class ListStack:
    def __init__(self):
        self._L = []
    #adding at end of list
    def push(self, item): # O(n)
        self._L.append(item)
    #removing from end of list
    def pop(self): # O(1)
        return self._L.pop()
    #look at last element
    def peek(self):
        return self._L[-1]
    #length
    def __len__(self):
        return len(self._L)
    #isempty
    def isempty(self):
        return len(self._L) == 0
    
    #inefficient if we add and remove from front of the list
    #both push and pop take O(1) time

#queues
#FIFO = first in first out
class ListQueueSimple:
    def __init__ (self):
        self._L = []
    def enqueue(self, item): # O(n)
        self._L.append(item)
    def dequeue(self): # O(n)
        return self._L.pop(0)
    def peek(self):
        return self._L[0]
    def __len__(self):
        return len(self._L)
    def isempty(self):
        return len(self._L) == 0

#queues without actually removing
class ListQueueFakeDelete:
    def __init__ (self):
        self._L = []
        self._head = 0

    def enqueue(self, item): # O(n)
        self._L.append(item)

    def dequeue(self): # O(n)
        item = self.peek()
        self._head += 1
        if self._head > len(self._L)//2:
            self._L = self._L[self._head: ] #updating; biting the bullet
            self._head = 0
        return item
    
    def peek(self):
        return self._L[self._head]
    
    def __len__(self):
        return len(self._L) - self._head
    def isempty(self):
        return len(self._L) == self._head
    
class Deque:
        #inserting and popping at index 0 takes O(N) time
    def __init__ (self):
        self._L = []
    def addfirst(self,item):
        self._L.insert(0, item)
    def addlast(self,item):
        self._L.append(item)
    def removefirst(self):
        return self._L.pop(0)
    def removefirst(self):
        return self._L.pop()
    def __len__ (self):
        return len(self._L)
    
class ListNode:
    def __init__ (self, item, link = None):
        self.item = item
        self.link = link
    
class LinkedList:
    def __init__(self):
        self._head = None
    def addfirst(self, item):
        self._head = ListNode(item, self._head)
    def removefirst(self,item):
        item = self._head.item
        self._head = self._head.link
        return item

#implementing queue with linkedlist where we have access to head
class LinkedList:
    def __init__ (self):
        self._head = None
    def addfirst(self, item):
        self._head = ListNode(item, self._head)
    def addLast(self, item):
        if self._head is None:
            self.addfirst(item)
        else:
            current = self._head
            while current.link is not None:
                current = current.link
            current.link = ListNode(item, None)
    def removefirst(self):
        item = self._head.item
        self._head = self._head.link
        return item
    def removelast(self):
        if self._head.link is None:
            return self.removefirst()
        else:
            current = self._head
            while current.link.link is not None:
                current = current.link
            item = current.link
            current.link = None
            return item
        
    #implementing queue with linkedlist where we have access to head and tail
class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
    def addfirst(self, item):
        self._head = ListNode(item, self._head)
        if self._tail is None:
            self._tail = self._head
    def addlast(self, item):
        if self._head is None:
            self.addfirst(item)
        else:
            self._tail.link = ListNode(item, None)
            self._tail = self._tail.link

    def removefirst(self):
        item = self._head.item
        self._head = self._head.link
        if self._head is None:
            self._tail is None
        return item

    def removelast(self):
        if self._head is self._tail:
            return self.removefirst()
        else:
            item = self._tail.item
            current = self._head
            while current.link.link is not None:
                current = current.link
            current.link = None
            self._tail = current
            return item

class ListNode:
    def __init__ (self, data, prev = None, link = None):
        self.data = data
        self.prev = prev
        self.link = link
        #only link if prev and next is not None
        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def addfirst(self, item):
        if len(self) == 0:
            self._head = self._tail = ListNode(item, None, None)
        else:
            newNode = ListNode(item, None, self._head)
            self._head.prev = newNode
            self._head = newNode
        self._length += 1

    def addLast(self, item):
        #if self._head is None:
        if len(self) == 0:
            self._head = self._tail = ListNode(item, None, None)
        else:
            newNode = ListNode(item, self._tail, None)
            self._tail.link = newNode
            self._tail = newNode
        self._length += 1

    def __len__(self):
        return self._length
    
#doubly linked list which has feature to add and remove but not just at the ends
class DoublyLinkedList:
    def __init__ (self):
        self._head = None
        self._tail = None
        self._length = 0
    
    def __len__(self):
        return self._length
    
    #private method
    def _addbetween(self, item, before, after):
        newNode = ListNode(item, before, after)
        if after is self._head:
            self._head = newNode
        if before is self._tail:
            self._tail = newNode
        self._length += 1

    def addfirst(self, item):
        self._addbetween(item, None, self._head)
    
    def addlast(self,item):
        self._addbetween(item, self._tail, None)

    def _remove(self, node):
        item = node.data
        before = node.prev
        after = node.link
        if node is self._head:
            self._head = after
        else:
            before.link = after
        if node is self._tail:
            self._tail = before
        else:
            after.prev = before
        self.length -= 1
        return node.data
    
    def removefirst(self):
        return self._remove(self._head)
    
    def removelast(self):
        return self._remove(self._tail)
    
    #adding another linkedlist on
    def __iadd_(self, other):
        if other._head is not None:
            if self._head is None:
                self._head = other._head
            else:
                self._tail.link = other._head
                other._head.prev = self._tail
            self._tail = other._tail
            self._length = self._length + other._length
            other.__init__() #clean up other list
            return self
        
    #manual implementation of hashmap
class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __str__(self):
        return str(self.key) + ":"

def mapput(L, key, value):
    for e in L:
        if e.key == key:
            e.value = value
            return
    L.append(Entry(key,value))
    
def mapget(L, key):
    for e in L:
        if e.key == key:
            return e.value
    raise KeyError
    
m = []
mapput(m, 4, 'five')
mapput(m, 1, 'one')
mapput(m, 13, 'thirteen')
mapput(m, 4, 'four')
assert(mapget(m,1) == 'one')
assert(mapget(m,4) == 'four')
print(m)

class ListMapping:
    def __init__(self):
        self._entries = []
    
    def __str__(self):
        return "{" + ", ".join(str(e) for e in self._entries) + "}"
    
    def __len__(self):
        return len(self._entries)
    
    def __contains__(self, key):
        if self._entry(key) is None:
            return False
        else:
            return True
    
    def __iter__(self):
        return (e.key for e in self._entries)
    
    def values(self):
        return (e.value for e in self._entries)
    
    def items(self):
        return ((e.key, e.value) for e in self._entries)
    
    def _entry(self,key):
        for e in self._entries:
            if e.key == key:
                return e
        return None
    
    def put(self, key, value):
        e = self._entry(key)
        if e is not None:
            e.value = value
        else:
            self._entries.append(Entry(key,value))
    
    def get(self, key):
        e = self._entry(key)
        if e is None:
            raise KeyError
        else:
            return e.value
        
    def remove(self, key):
        e = self._entry(key)
        if e is None:
            raise KeyError
        else:
            self._entries.remove(e)


    
print(hash("valr"))