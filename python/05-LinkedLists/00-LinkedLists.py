from SLListModule import Node

class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0
    def addFront(self , value):
        newNode = Node(value)
        runner = self.head
        newNode.next = runner
        self.head = newNode
        self.size += 1
        return self
    def display(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self
    def contains(self, value):
        runner = self.head
        count = 0
        while (runner != None):
            count += 1
            if runner.value == value:
                print (value, count)
                return self
            runner = runner.next
        return self
    def deleteFront(self):
        if self.head != None:
            self.head = self.head.next
            self.size -= 1
            return self
        return None
    def frontValue(self):
        if self.head != None:
            print(self.head.value)
            return self
        return None
    def length(self):
        if self.head == None:
            return self
        print(self.size)
        return self
    def max(self):
        runner = self.head
        max = self.head.value
        while (runner != None):
            if runner.value > max:   #TypeError: '>' not supported between instances of 'str' and 'int'??
                max = runner.value
            runner = runner.next
        print(max)
        return self
    def min(self):
        min = self.head.value
        runner = self.head
        while (runner != None):
            if runner.value <= min:
                min = runner.value
            runner = runner.next
        print(min)
        return self
    def avg(self):
        sum = 0
        runner = self.head
        while (runner != None):
            sum += runner.value
            runner = runner.next
        avg = sum/self.size
        print(avg)
        return self
    def lastValue(self):
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
thisList = LinkedList()
thisList.addFront('2').addFront('4').addFront('6').addFront('3').addFront('1').deleteFront().contains('4').display().frontValue()

thisList.addFront(-2).addFront(4.3).addFront(6).addFront(3.5).addFront(1).display().length().max().min().avg()

thisList.addFront(9).addFront(-4).addFront(6).addFront(3.5).addFront(1).addLast(7).display().min2Front()