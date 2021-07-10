class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def addFront(self , value):
        newNode = Node(value)
        i = self.head
        newNode.next = i
        self.head = newNode
        self.size += 1
        return self
    def display(self):
        if self.head == None:
            return self
        i = self.head
        while (i != None):
            print(i.value)
            i = i.next
        return self
    def last(self):
        if self.head == None:
            return self
        i = self.head
        while (i.next != None):
            i = i.next
        print(i.value)
        return self
    def removeLast(self):
        if self.head == None:
            return self
        elif self.head.next == None:
            self.head = None
            return self
        i = self.head
        while i.next.next != None:
            i = i.next
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
        self.size += 1
        return self
    def min2Front(self):
        min = self.head.value
        i = self.head
        while (i != None):
            if i.value <= min:
                min = i
            i = i.next
        min.next = self.head
        self.head = min
        return self
thisList = SinglyLinkedList()
thisList.addFront(9).addFront(-4).addFront(6).addFront(3.5).addFront(1).removeLast().addLast(7).last().min2Front().display()