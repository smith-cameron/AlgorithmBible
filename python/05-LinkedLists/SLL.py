from SLLNode import Node

class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0
        self.min = None
        self.max = None
        self.tail = None
    def addFront(self , value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        print (f"{value} had been added as list head")
        return self
    def display(self):
        i = self.head
        count = 1
        while i != None:
            print (f"Node #{count}: {i.value}")
            i = i.next
            count += 1
        return self
    def contains(self, value):
        i = self.head
        count = 0
        while i != None:
            count += 1
            if i.value == value:
                print (f"{value} is at Node #{count}")
                return self
            i = i.next
        return self
    def deleteFront(self):
        if self.head != None:
            self.head = self.head.next
            self.size -= 1
            return self
        print("*List Is Empty*")
        return self
    def frontValue(self):
        if self.head != None:
            print(f"Value of the head Node is {self.head.value}")
            return self
        print("*List Is Empty*")
        return self
    def length(self):
        if self.head == None:
            return self
        print(f"List length: {self.size}")
        return self
    def maxValue(self):
        i = self.head
        x = i.value
        while i.next != None:
            if i.value >= x:   
                x = i.value
                self.max = i
            i = i.next
        print(f"Max: {self.max.value}")
        return self
    def minValue(self):
        i = self.head
        x = i.value
        while i.next != None:
            if i.value <= x:
                x = i.value
                self.min = i
            i = i.next
        print(f"Min: {self.min.value}")
        return self
    def avgValue(self):
        sum = 0
        i = self.head
        while i.next != None:
            sum += i.value
            i = i.next
        avg = sum/self.size
        print(f"Avg: {avg}")
        return self
    def lastValue(self):
        if self.head == None:
            print("*List Is Empty*")
            return self
        i = self.head
        while i.next != None:
            i = i.next
        self.tail = i
        print(f"Tail: {self.tail.value}")
        return self
    def removeLast(self):
        if self.head == None:
            print("*List Is Empty*")
            return self
        elif self.head.next == None:
            self.head = None
            return self
        i = self.head
        while i.next.next != None:
            i = i.next
        self.tail = i
        i.next = None
        return self
    def addLast(self, value):
        newNode = Node(value)
        if self.head == None:
            self.addFront(value)
            return self
        i = self.head
        while i.next != None:
            i = i.next
        i.next = newNode
        self.tail = i.next
        self.size += 1
        print (f"{value} added at Node #{self.size}")
        return self
    def min2Front(self):
        return self
    def max2Back(self):
        return self
    def prependValueAt(self, value, target):
        newNode = Node(value)
        if self.head == None:
            self.addFront(value)
            print(f"Node: {value} has been added as the head node.")
            return self
        i = self.head
        x = None
        while i.next != None and i.value != target:
            x = i
            i = i.next
        newNode.value = value
        newNode.next = i
        x.next = newNode
        print(f"Node Value: {value} has been added before {i.value}")
        self.size += 1
        return self
    def appendValueAt(self, value, target):
        newNode = Node(value)
        if self.head == None:
            self.addFront(value)
            print(f"Node: {value} has been added as the head node.")
            return self
        i = self.head
        while i.next != None and i.value != target:
            i = i.next
        newNode.value = value
        newNode.next = i.next
        i.next =  newNode
        print(f"Node Value: {value} has been added after {i.value}")
        self.size += 1
        return self
    def createList(self, input):
        x = 0
        while x < len(input):
            self.addLast(input[x])
            x += 1
        self.display()
        return self
    def deleteValue(self, target):
        if self.head == None:
            print("*List Is Empty*")
        i = self.head
        x = None
        while i.next != None and i.value != target:
            x = i
            i = i.next
        x.next = i.next
        i.next = None
        return self

