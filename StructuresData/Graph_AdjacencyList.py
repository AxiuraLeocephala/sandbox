from typing import List, Literal, SupportsIndex, Union
from uuid import uuid4, UUID

from LinkedList import LinkedList
from models.Vertex import Vertex
from models.ListEdges import ListEdges
from models.Edge import Edge

class Graph(LinkedList):
    '''
    Работает на основе списка смежности
    '''
    __instance = None
    __is_exist: bool = False
    __number_vertex: int = 0
    type_directed: Literal["ud", "d", "m"] = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    
    def __str__(self) -> str:
        current_vertex = self.head
        symbol_arrow = "<->" if self.type_directed else "->"
        output_string = ""

        while current_vertex:
            len_str_current_vertex = len(str(current_vertex.data.id))
            output_string += f"{current_vertex.data.id}"
            if current_vertex.data.list_edges:
                for edge in current_vertex.data.list_edges:
                    output_string += f" {symbol_arrow} {edge.incoming_vertex.data.id}\n{" " * len_str_current_vertex}"
                output_string = output_string[0 : -len_str_current_vertex]
            else:
                output_string += f" {symbol_arrow} []\n"
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

        Graph.type_directed = type_directed # Реализован singleton, поэтому атрибут класса меняется напрямую 
        
        super().__init__("doubly")

    @property
    def number_vertex(self):
        return Graph.__number_vertex

    def insert_at_begin(self, id: Union[UUID, int]) -> Vertex:
        Graph.__number_vertex += 1
        return super().insert_at_begin(ListEdges(id))

    def insert_at_index(self, id: Union[UUID, int]) -> Vertex:
        Graph.__number_vertex += 1
        return super().insert_at_index(ListEdges(id))

    def insert_at_end(self, id: Union[UUID, int]) -> Vertex:
        Graph.__number_vertex += 1
        return super().insert_at_end(ListEdges(id))

    def remove_first_vertex(self) -> None:
        raise TypeError("the method is not supported")

    def remove_last_vertex(self) -> None:
        raise TypeError("the method is not supported")

    def remove_vertex(self, target_vertex: Vertex) -> None:
        current_vertex = self.head
        
        while current_vertex:
            if current_vertex.data.id == target_vertex.data.id:
                for edge in current_vertex.data.list_edges:
                    self.remove_edge(current_vertex, edge.incoming_vertex)
                
                current_vertex.prev.next = current_vertex.next
                current_vertex.next.prev = current_vertex.prev
                break
            current_vertex.next
        else:
            raise ValueError("vertex not found")


    def create_edge(self, outgoing_vertex: Vertex, incoming_vertex: Vertex) -> None:
        outgoing_vertex.data.list_edges.append(Edge(outgoing_vertex, incoming_vertex))
        incoming_vertex.data.list_edges.append(Edge(incoming_vertex, outgoing_vertex))

    def remove_edge(self, outgoing_vertex: Vertex, incoming_vertex: Vertex) -> None:
        for i in range(len(outgoing_vertex.data.list_edges)):
            if outgoing_vertex.data.list_edges[i].incoming_vertex.data.id == incoming_vertex.data.id:
                outgoing_vertex.data.list_edges.pop(i)
                break
        else:
            raise ValueError("edge between the specified vertices was not found")
        
        for i in range(len(incoming_vertex.data.list_edges)):
            if incoming_vertex.data.list_edges[i].incoming_vertex.data.id == outgoing_vertex.data.id:
                incoming_vertex.data.list_edges.pop(i)
                break
        

if __name__ == "__main__":
    number_vertex = 4
    list_vertexes: List[Vertex] = []
    graph = Graph("ud")

    for i in range(number_vertex):
        # vertex = graph.insert_at_end(uuid4())
        vertex = graph.insert_at_end(i)
        list_vertexes.append(vertex)
    
    for i in range(number_vertex - 1):
        graph.create_edge(list_vertexes[i], list_vertexes[i+1])
    
    for i in range(0, int(number_vertex / 2) + 1):
        for j in range(i + 2, number_vertex):
            graph.create_edge(list_vertexes[i], list_vertexes[j])

    print(graph)

    # graph.remove_edge(list_vertexes[1], list_vertexes[3])
