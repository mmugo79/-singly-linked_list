class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#linkedlist class to manage nodes
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, index ,data):
        if index == 0:
            self.insert_at_start(data)
            return

        new_node = Node(data)
        temp = self.head
        count = 0
        while temp and count < index -1:
            temp = temp.next
            count += 1
        if temp is None:
            print("index out of range")
            return
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_index(self,index):
        if self.head is None:
            print("list is empty")
            return
        if index == 0:
            self.head = self.head.next
            return
        temp = self.head
        count = 0
        while temp.next and count < index -1:
            temp = temp .next
            count +=1
        if temp.next is None:
            print("index out of range")
            return
        temp.next = temp.next.next
    def search(self, value):
        temp = self.head
        index = 0
        while temp:
            if temp.data == value:
                return index
            temp = temp.next
            index += 1
        return -1


    def display(self):
        temp = self.head
        if temp is None:
            print("list is empty")
            return
        while temp:
            print(temp.data, end= " -> " if temp.next else "\n")
            temp = temp.next

#example usage
ll = LinkedList()
ll.insert_at_end('a')
ll.insert_at_start('b')
ll.insert_at_index(1,'c')
ll.display()
print("index of 'c':", ll.search('c'))
ll.delete_at_index(1)
ll.display()
