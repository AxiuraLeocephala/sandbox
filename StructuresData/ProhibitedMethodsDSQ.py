class ProhibitedMethodsDSQ:
    '''
    Base class for queue, stack, and deka. Its prohibits the use of the 
    following methods: insert, remove, sort
    '''

    def insert(self, index, object) -> None:
        raise ValueError("it is not possible to insert a new element into the array, use the append method")
    
    def remove(self, value) -> None:
        raise ValueError("it is not possible to delete a specific item from the queue. use the pop method")
    
    def sort(self, *, key, reverse) -> None:
        raise ValueError("the queue cannot be sorted")