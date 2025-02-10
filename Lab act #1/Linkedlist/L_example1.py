class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  


class LinkedList:
    def __init__(self):
        self.head = None  

   
    def prepend(self, data):
        new_node = Node(data)  
        new_node.next = self.head 
        self.head = new_node 

    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()

linked_list.prepend("me")
linked_list.prepend("my_self")
linked_list.prepend("and i")

linked_list.print_list()
