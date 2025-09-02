

class Queue:

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if len(self._items) == 0:
            return None
        elif len(self._items) != 0:
            i = self._items.pop(0)
            return i
    
    def first(self):
        if len(self._items) == 0:
            return None
        elif len(self._items) != 0:
            return(self._items[0])
    
    def is_empty(self):
        if len(self._items) == 0:
            return True
        elif len(self._items) != 0:
            return False
        
    def size(self):
        return len(self._items)
    
    def __str__(self):
        return str(self._items)
     





