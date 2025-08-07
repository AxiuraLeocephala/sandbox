import inspect
from typing import Any, Union, Literal, List, SupportsIndex

from _generate_random_numbers import generate_random_numbers

class Node:
    # def __init__(self, data, *, next: List = [], prev: List = []): 
    # Список - мутабельный объект, при использовании его в качестве 
    # дефолтного значения параметра он будет общим для всех экземпляров
    # класса. Изменяя значение, например, next у одного экземпляра,
    # это изменение будет видно и у других экземпляров - фактически
    # изменяется один и тот же объект 
    def __init__(self, data, *, next: List = None, prev: List = None):
        self.data = data
        self.next: List[Any] = next if next else []
        self.prev: List[Any] = prev if prev else []

class LinkedList:
    def __init__(self, type_list: Literal["singly", "doubly"]):
        self.type_list = type_list
        self.is_looped = False
        self.head = None
        self.tail = None

    def __call__(self) -> str:
        current_node = self.head
        output_string = ""

        def traversing(current_node: Node, output_string: str) -> str:
            output_string += current_node.data
            if current_node.next:
                for node in current_node.next:
                    if (not node.prev is []) and current_node in node.prev:
                        output_string += f" <-> {node.data}\n"
                    else:
                        output_string += f" -> {node.data}\n"
                
                for node in current_node.next:
                    output_string = traversing(node, output_string)

                return output_string
            else:
                output_string += " -> None"
                return output_string

        output_string = traversing(current_node, output_string)

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
            new_node.next.append(self.head)
            if self.type_list == "doubly":
                self.head.prev.append(new_node)
        
        self.head = new_node

        if not self.tail:
            self.tail = self.head

    def insert_at_index(self, data: Any, index: SupportsIndex) -> None:
        caller = ""
        flag = False
        i = 0

        for char in reversed(inspect.stack()[1].filename):
            if flag: 
                if char == "\\": break
                caller = char + caller

            if char == ".": flag = True

        if not index:
            if caller == "graph":
                new_node = Node(data)
                self.head.next.append(new_node)

                if self.type_list == "doubly":
                    new_node.prev.append(self.head)
            else:
                self.insert_at_begin(data)

            return
        if self.is_empty:
            raise TypeError("collection is empty")

        current_node = self.head
        i = 0
        def travesing(current_node: Node, i: int, index: int) -> Union[Node, None]:
            if current_node.next:
                for node in current_node.next:
                    i += 1
                    if i == index:
                        return node
                else:
                    for node in current_node.next:
                        node = travesing(node, i, index)
                        if node:
                            return node
                    return None
            else:
                nonlocal caller
                if i + 1 == index and caller == "linkedlist":
                    self.insert_at_end(data)
                    return
                return None

        current_node = travesing(current_node, i, index)

        if not current_node:
            if caller == "linkedlist":
                raise ValueError("index out of range")
            elif caller == "graph":
                raise ValueError("no node with the specified injector was found")
            else:
                raise ValueError("1. unknown name of caller\n2. index out of range") 

        new_node = Node(data)

        if caller == "linkedlist":
            current_node.prev[0].next = [new_node]
            new_node.next = [current_node]
            if self.type_list == "doubly":
                current_node.prev = [new_node] 
                new_node.prev = [current_node.prev[0]]
        elif caller == "graph":
            current_node.next.append(new_node)
            if self.type_list == "doubly":
                new_node.prev.append(current_node)
        else:
            raise TypeError("unknown name of caller")

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

    number_nodes = 5
    for d in range(number_nodes - 1, -1, -1):
        linked_list.insert_at_begin(f'{d}')

    print(linked_list)

    linked_list.insert_at_index("5", 4)

    print(linked_list)
