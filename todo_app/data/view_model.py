class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def done_items(self):
        """returns done items"""
        done_items = [item for item in self._items if item['status'] == 'Done']
        return done_items
    
    @property
    def doing_items(self):
        """returns doing items"""
        doing_items = [item for item in self._items
                       if item['status'] == 'Doing']
        return doing_items
    
    @property
    def to_do_items(self):
        """returns to_do items"""
        to_do_items = [item for item in self._items
                       if item['status'] == 'To do']
        return to_do_items
