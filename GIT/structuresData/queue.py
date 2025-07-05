from baseStructure import BaseStructure

class Queue(BaseStructure):
    '''
    FIFO - first in first out
    '''
    __index_last_item = 0

    def get_item(self):
        return BaseStructure.get_item(self, self.__index_last_item)
