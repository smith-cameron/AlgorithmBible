class ListNode():
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList():

    def __init__(self):
        self.head = None
        self.size = 0
    def addFront(self , value):
        newNode = ListNode(value)
        runner = self.head
        newNode.next = runner
        self.head = newNode
        self.size += 1
        return self
    def contains(self, value):
        i = self.head
        count = 0
        while (i != None):
            count += 1
            if i.value == value:
                print (value, count)
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
            print(self.head.value)
            return self
        return None
    def printList(self):
        i = self.head
        while (i != None):
            print(i.value)
            i = i.next
        return self
thisList = LinkedList()
thisList.addFront('2').addFront('4').addFront('6').addFront('3').addFront('1').deleteFront().contains('4').printList().frontValue()