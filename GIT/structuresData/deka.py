from queue import Queue
from stack import Stack

class Deka(Queue, Stack):
    '''
    FIFO & LIFO. Сочетает в себе принцип получения элемента как с начала, так и с конца
    MRO - Method Resolution Order
    '''

    def get_first_item(self):
        return Queue.get_item(self)

    def get_last_item(self):
        return Stack.get_item(self)