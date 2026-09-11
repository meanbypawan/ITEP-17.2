class Node:
    def __init__(self):
        self.data = None
        self.next = None

class LinkedList:
    def __init__(self):
       self.head = None
   
    def insert(self,element):
        node = Node()
        node.data = element
        node.next = None
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
    def delete_end(self):
        if self.head.next is None:
            self.head = None
        else:    
            temp = self.head
            current = temp
            while temp.next is not None:
                current = temp
                temp = temp.next
            current.next = None

    def traverse(self):
       if self.head is not None:
            temp = self.head
            while temp:
                print(temp.data,end=" ")
                temp = temp.next            
            print()
       else:
           print("LinkedList is empty..")     
    def delete_beg(self):
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            self.head = self.head.next
            current.next = None

    def insert_at_pos(self,element,pos):
        node = Node()
        node.data = element
        node.next = None
        if pos == 1:
           node.next = self.head
           self.head = node    
        else:    
            temp = self.head
            prev = None
            while pos-1:
                prev = temp
                temp = temp.next
                pos -= 1
            prev.next = node
            node.next = temp

    def delete_at_position(self,pos):
        if pos == 1:
          self.head = self.head.next
        else:  
            temp = self.head
            prev = None
            while pos-1:
                prev = temp
                temp = temp.next
                pos -= 1
            prev.next = temp.next
            temp.next = None
    
    def middle_of_list(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)    

ll = LinkedList()
ll.insert(10)   
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)
ll.insert(60)
ll.traverse()
ll.middle_of_list()
#ll.insert_at_pos(1000,1)
#ll.delete_at_position(1)
#ll.traverse()