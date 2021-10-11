from SLListModule import Node

class LinkedList():
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
        i = self.head
        while i != None:
            print(i.value)
            i = i.next
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
        return None
    def frontValue(self):
        if self.head != None:
            print(f"Value of the head Node is {self.head.value}")
            return self
        return None
    def length(self):
        if self.head == None:
            return self
        print(f"List length: {self.size}")
        return self
    def max(self):
        i = self.head
        max = self.head.value
        while i != None:
            if i.value > max:   
                max = i.value
            i = i.next
        print(f"Max: {max}")
        return self
    def min(self):
        min = self.head.value
        i = self.head
        while i != None:
            if i.value <= min:
                min = i.value
            i = i.next
        print(f"Min: {min}")
        return self
    def avg(self):
        sum = 0
        i = self.head
        while i != None:
            sum += i.value
            i = i.next
        avg = sum/self.size
        print(f"Avg: {avg}")
        return self
    def lastValue(self):
        if self.head == None:
            return self
        i = self.head
        while i.next != None:
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
        if not self.head or not self.head.next:
            return self
        min = self.head.value
        i = self.head
        j = self.head
        while i != None:
            if i.value < min:
                min = i.value
                j = i
            i = i.next
        print(f"Min value: {min}")
        # starting at min
        # will need a before/previous variable node and current(loop needed to get both?)
        
        # set previous.next to min.next cutting min out of the list
        # set min.next to self.head
        # and make min the head
        return self
    def max2Back(self):
        if not self.head or not self.head.next:
            return self
        max = self.head.value
        i = self.head
        while i != None:
            if i.value > max:
                max = i.value
            i = i.next
        print(f"Max value: {max}")
        # 
        return self

thisList = LinkedList()
# thisList.addFront(2).addFront(4).addFront(6).addFront(3).addFront(1).deleteFront().contains(4).display().frontValue()

# thisList.addFront(2).addFront(4.3).addFront(6).addFront(-3.5).addFront(1).display().length().max().min().avg().min2Front().display()

thisList.addFront(9).addFront(-4).addFront(6).addFront(3.5).addFront(1).addLast(7).display()