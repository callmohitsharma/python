class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        head = self
        length = 0
        node = self
        if index < 0:
            return -1
        elif type(index) is not int:
            return -1
        while head.next != None:
            head = head.next
            length +=1
        if index > length-1:
            return -1
        for i in range(index + 1):
            if node.next != None:
                node = node.next
        if node != None:
            return node.val
        else:
            return None

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = MyLinkedList()
        node.val = val
        node.next = self.next
        self.next = node


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        head = self
        while head.next != None:
            head = head.next
            if head.next == None:
                node = MyLinkedList()
                node.val = val
                node.next = None
                head.next = node
                break

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list,
        the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        head = self
        head1 = self
        length=0
        #get length of linked list
        while head.next != None:
            head = head.next
            length +=1

        if length >0 and index > length+1:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == length:
            self.addAtTail(val)
        else:
            for i in range(index):
                head1 = head1.next
            node = MyLinkedList()
            node.val = val
            k = head1.next
            node.next = k
            head1.next = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        head = self
        head1 = self
        length = 0
        current_node = None
        priv_node = None
        # get length of linked list

        while head.next != None:
            head = head.next
            length += 1
        if index > length - 1:
            return
        if index<0:
            return
        if index == 0:
            node = head1.next
            node = node.next
            head1.next = node
            return

        for i in range(index + 1):
            if i == index-1:
                priv_node = head1.next
                head1 = head1.next
            elif i == index:
                current_node = head1.next
            else:
                head1 = head1.next
                continue

        priv_node.next = current_node.next

obj = MyLinkedList()
#param_1 = obj.get(1)
obj.addAtHead(7)
obj.addAtHead(2)
obj.addAtHead(1)
obj.addAtIndex(3,0)
obj.deleteAtIndex(2)
obj.addAtHead(6)
obj.addAtTail(4)
print(obj.get(4))
obj.addAtHead(4)
obj.addAtIndex(5,0)
obj.addAtHead(6)
#obj.addAtTail(3)
#obj.addAtIndex(0,10)
#obj.addAtIndex(0,20)
#obj.addAtIndex(1,30)
#print(obj.get(0))
#obj.deleteAtIndex(0)
#print(obj.get(0))

