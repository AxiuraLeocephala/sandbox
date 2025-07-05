class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertToBigin(self, data) -> None:
        new_node = Node(data)
        if (self.head):
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node

    def insertToIndex(self, data, new_node_index: int) -> None:
        if (new_node_index == 0): 
            self.insertToBigin(data) 
            return

        current_node = self.head
        current_node_index = 0

        while (current_node.next != None and current_node_index != new_node_index):
            print(current_node_index, current_node.data, current_node.next != None, current_node_index != new_node_index)
            current_node = current_node.next
            current_node_index += 1

        print("> ", current_node_index, current_node.data, current_node.next != None, current_node_index != new_node_index)

        if (current_node_index == new_node_index):
            print(current_node.data)
        else:
            raise IndexError("Index is`t present")



linked_list = LinkedList()
linked_list.insertToBigin("Элемент_5")
linked_list.insertToBigin("Элемент_4")
linked_list.insertToBigin("Элемент_3")
linked_list.insertToBigin("Элемент_2")
linked_list.insertToBigin("Элемент_1")
linked_list.insertToBigin("Элемент_0")
linked_list.insertToIndex("Элемент_6", 5)