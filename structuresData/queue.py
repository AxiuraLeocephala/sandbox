from baseStructure import BaseStructure

class Queue(BaseStructure):
    '''
    FIFO - first in first out
    '''
    __index_extracted_item = 0

    def __init__(self):
        super().__init__(self.__index_extracted_item)

queue = Queue()
