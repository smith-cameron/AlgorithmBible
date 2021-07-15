from SLListModule import Node

class SLLMethods():
    def __init__(self):
        self.head = List.head
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
        min = self.head
        i = self.head
        while (i != None):
            if i.value <= min.value:
                min = i
            i = i.next
        # print(min.value)
        return self
thisList = SLLMethods()
thisList.addFront(9).addFront(-4).addFront(6).addFront(3.5).addFront(1).addLast(7).display().min2Front()