from typing import Any, Union, Literal, SupportsIndex

from _generate_random_numbers import generate_random_numbers

class Node:
    def __init__(self, data, *, next = None, prev = None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self, type_list: Literal["singly", "doubly"]):
        self.type_list = type_list
        self.is_looped = False
        self.head = None
        self.tail = None

    def __call__(self) -> str:
        output_string = "" 

        current_node = self.head
        while current_node:
            output_string += f'{current_node.data} -> ' 
            current_node = current_node.next
        output_string += f"None\n\033[0;33;40m type:\033[0;37;40m {self.type_list}\n\033[0;33;40m is looped:\033[0;37;40m {self.is_looped}"
                
        return output_string

    def __str__(self) -> str:
        return self()
    
    @property
    def is_empty(self) -> bool:
        return self.head is None

    @property
    def length(self) -> int:
        i = 0
        current_node = self.head

        while current_node:
            i += 1
            current_node = current_node.next

        return i 


    def insert_at_begin(self, data: Any) -> None:
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            if self.type_list == "doubly":
                self.head.prev = new_node
        
        self.head = new_node

        if not self.tail:
            self.tail = self.head

    def insert_at_index(self, data: Any, index: SupportsIndex) -> None:
        if not index: 
            self.insert_at_begin(data)
            return
        if self.is_empty:
            raise TypeError("linked list is empty")
                
        new_node = Node(data)
        i = 0
        current_node = self.head

        while i < index:
            current_node = current_node.next
            if not current_node:
                if i + 1 == index:
                    del new_node
                    self.insert_at_end(data)
                    return
                raise ValueError("index out of range")
            i += 1

        current_node.prev.next, new_node.next = new_node, current_node
        if self.type_list == "doubly":
            current_node.prev, new_node.prev = new_node, current_node.prev

    def insert_at_end(self, data: Any) -> None:
        new_node = Node(data)

        if self.tail:
            self.tail.next = new_node
            if self.type_list == "doubly":
                new_node.prev = self.tail

        self.tail = new_node
        
        if not self.head:
            self.head = self.tail

    def change_data(self, new_data: Any, index: SupportsIndex) -> None:
        if self.is_empty:
            raise TypeError("linked list is empty")
        i = 0
        current_node = self.head

        while i < index:
            current_node = current_node.next
            if not current_node:
                raise ValueError("index out of range")
            i += 1

        current_node.data = new_data

    def remove_first_node(self) -> None:
        if self.is_empty:
            raise TypeError("linked list is empty")
        
        next_node = self.head.next
        if next_node:
            next_node.prev = None
        else:
            self.tail = None
        
        self.head = next_node

    def remove_node(self, index: SupportsIndex) -> None:
        if not index:
            self.remove_first_node()
            return
        if self.is_empty:
            raise TypeError("linked list is empty")
        
        i = 0
        current_node = self.head

        while i < index:
            current_node = current_node.next
            if not current_node.next:
                if i + 1 == index:
                    self.remove_last_node()
                    return
                raise ValueError("index out of range")
            i += 1

        current_node.prev.next = current_node.next
        if self.type_list == "doubly":
            current_node.next.prev = current_node.prev

    def remove_last_node(self) -> None:
        if self.is_empty:
            raise TypeError("linked list is empty")
        
        prev_node = self.tail.prev
        if prev_node:
            prev_node.next = None
        else:
            self.head = None

        self.tail = prev_node

    def search(self, required_data: Any) -> Union[Node, None]:
        if self.is_empty:
            raise TypeError("linked list is empty")
        
        current_node = self.head
        while current_node:
            if current_node.data == required_data:
                return current_node
            current_node = current_node.next
        
        return

if __name__ == "__main__":
    linked_list = LinkedList("doubly")
    
    number_nodes = 6
    for d in range(5, -1, -1):
        linked_list.insert_at_end(f'data_{d}.0')

    print(linked_list)
