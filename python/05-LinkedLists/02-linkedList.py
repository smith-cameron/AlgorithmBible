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
        runner = self.head
        newNode.next = runner
        self.head = newNode
        self.size += 1
        return self
    def length(self):
        if self.head == None:
            return self
        # count = 1
        # runner = self.head
        # while runner.next != None:
        #     runner = runner.next
        #     count += 1
        #print(count)
        print(self.size)
        return self
    def max(self):
        max = self.head.value
        runner = self.head
        while (runner != None):
            if runner.value >= max:
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
    def display(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self

thisList = SinglyLinkedList()
thisList.addFront(-2).addFront(4.3).addFront(6).addFront(3.5).addFront(1).display().length().max().min().avg()