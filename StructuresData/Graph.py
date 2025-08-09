from typing import Any, Literal, SupportsIndex, Union

from LinkedList import LinkedList

# TODO: вес ребер


class Graph(LinkedList):
    def __init__(self, type_directed: Literal["ud", "d", "m"] = "ud", is_weight: Union[True, False] = False):
        '''
        Args:
            type_directed:
                ud - undirected graph, ребра не имеют конкретного направления\n
                d - directed graph, ребра имеют конкретное направление (только одно направление)\n
                m - mixed graph, сочетает признаки ud и u
            is_weight: ребра взвешены или нет
        '''
        self.type_directed = type_directed
        self.is_weight = is_weight

        match self.type_directed:
            case "ud":
                type_linkeed_list = "doubly"
            case "d":
                type_linkeed_list = "singly"
            case "m":
                type_linkeed_list = "mix"
            case _:
                raise ValueError("unknown argument of type_direction")

        super().__init__(type_linkeed_list)

    def insert_at_begin(self, data: Any) -> None:
        super().insert_at_begin(data)
    
    def insert_after_index(self, data: Any, index: SupportsIndex) -> None:
        '''
        Args:
        data : Any
            Данные, которые будут храниться в узле.
        index : SupportsIndex
            Индекс узла, после которого будет вставлен новый узел. 
        '''
        super().insert_at_index(data, index)

    

if __name__ == "__main__":
    number_node = 5
    graph = Graph()

    for i in range(number_node - 1, -1, -1):
        graph.insert_at_begin(f"{i}")

    graph.insert_at_index("5", 4)
    graph.insert_at_index("6", 4)
    graph.insert_at_index("7", 4)
    graph.insert_at_index("8", {5, 6, 7})
    print(graph)
