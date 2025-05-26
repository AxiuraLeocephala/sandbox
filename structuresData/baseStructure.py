from typing import Any

class BaseStructure():
    def __init__(self, index_extracted_item: int) -> None:
        self.collection = []
        self.__index_extracted_item = index_extracted_item

    def put(self, item: Any) -> None:
        self.collection.append(item)

    def get(self) -> Any:
        return self.collection.pop(self.__index_extracted_item)
    
    @property
    def size(self):
        return len(self.collection)
