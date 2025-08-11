from typing import List, Literal, Type, Union
from uuid import uuid4, UUID

from LinkedList import Node, LinkedList
from StructuresData.models.ListEdges import ListEdges

class Graph(LinkedList):
    '''
    Работает на основе списка смежности
    '''
    __instance: Type["Graph"] = None
    __is_exist: bool = False
    __number_vertex: int = 0

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    
    def __str__(self) -> str:
        current_vertex = self.head
        output_string = ""

        while current_vertex:
            output_string += f"{current_vertex.data.id} -> {current_vertex.data.adjacency_list}\n"
            current_vertex = current_vertex.next


        return output_string

    def __del__(self):
        self.__instance = None
    
    def __init__(self, type_directed: Literal["ud", "d", "m"]):
        '''
            При попытке повторного создания экземпляра класса будет возвращен 
            ранее созданный экземпляр с теми же атрибудами, что и при первом создании.
            Singeton в чистом виде

            Args:
                type_directed: 
                    ud (undirected) - неориентированный граф;
                    d (directed) - ориентированный граф;
                    m (mix) - смешанный граф;
        '''
        if self.__is_exist: 
            return
        else: 
            self.__is_exist = True

        self.type_directed = type_directed
        
        super().__init__("doubly")

    @property
    def number_vertex(self):
        return Graph.__number_vertex

    def insert_at_begin(self, id: Union[UUID, int]) -> None:
        Graph.__number_vertex += 1
        super().insert_at_begin(ListEdges(id))

    def insert_at_index(self, id: Union[UUID, int]) -> None:
        Graph.__number_vertex += 1
        super().insert_at_index(ListEdges(id))

    def insert_at_end(self, id: Union[UUID, int]) -> None:
        Graph.__number_vertex += 1
        super().insert_at_end(ListEdges(id))

    def remove_first_node(self) -> None:
        try:
            super().remove_first_node()
        except Exception as e:
            raise e
        else: 
            Graph.__number_vertex -= 1

    def remove_node(self) -> None:
        try:
            super().remove_node()
        except Exception as e:
            raise e
        else: 
            Graph.__number_vertex -= 1

    def remove_last_node(self) -> None:
        try:
            super().remove_last_node()
        except Exception as e:
            raise e
        else: 
            Graph.__number_vertex -= 1


if __name__ == "__main__":
    number_vertex = 5
    vertexs_id = [uuid4() for _ in range(number_vertex)]
    graph = Graph("ud")

    for id in vertexs_id:
        graph.insert_at_end(id)

    