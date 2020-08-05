class SimpleList():
    def __init__(self, items):
        self.all_items  = list(items)

    def add (self, item):
        self.all_items.append(item)
        print('Simple ADD')

    def __getitem__(self, index):
        return self.all_items[index]

    def sort (self):
        return self.all_items.sort()
    
    def __len__(self):
        return len(self.all_items)

    def delete(self, item):
        self.all_items.remove(item)

    def __repr__(self):
        return "SimpleList({!r})".format(self.all_items)

class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add (self, item):
        super().add(item)
        self.sort()
        print('sort ADD')
    
    def __repr__(self):
        return "SortedList({!r})".format(list(self))


class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items: self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError(x, ' não é inteiro')
    
    def add(self, item):
        self._validate(item)
        super().add(item)
        print('INT ADD')

    def __repr__(self):
        return "Int List ({!r})".format(list(self))
        

class SortedIntList(IntList, SortedList):
    def __repr__(self):
        return "SortedINT LIST ({!r})".format(list(self))