from typing import Any

class BaseStructure():
    def __init__(self):
        self._collection = []

    def put_item(self, item: Any) -> None:
        self._collection.append(item)

    def get_item(self, index_item: int) -> Any:
        return self._collection[index_item]
    
    def extract_item(self, index_item: int) -> Any:
        return self._collection.pop(index_item)

    def get_all_items(self) -> list:
        return self._collection
    
    @property
    def is_empty(self) -> int:
        return len(self._collection) == 0
    
    @property
    def size(self) -> int:
        return len(self._collection)
    