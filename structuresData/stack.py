from baseStructure import BaseStructure

class Stack(BaseStructure):
    '''
    LIFO - last in first out
    '''
    __index_extracted_item = -1

    def __init__(self):
        super().__init__(self.__index_extracted_item)

stack = Stack()
