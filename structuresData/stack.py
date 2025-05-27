from baseStructure import BaseStructure

class Stack(BaseStructure):
    '''
    LIFO - last in first out
    '''
    __index_last_item = -1

    def get_item(self):
        return BaseStructure.get_item(self.__index_last_item)