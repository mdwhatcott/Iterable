class Iterable(object):
    def __init__(self, items=None): 
        self.__items = items if items is not None else []

    @property
    def items(self): 
        return self.__items

    def reverse(self): 
        return Iterable(reversed(self.__items))

    def display(self, *args, **kwargs): 
        for i in list(self.__items): print i
        print
        return self

    def perform(self, action, *args, **kwargs):
        for item in self.__items: action(item, *args, **kwargs)
        return self

    def transform(self, action, *args, **kwargs):
        return Iterable([action(i, *args, **kwargs) for i in self.__items])
        
    def select(self, filter, *args, **kwargs):
        return Iterable(
            [i for i in self.__items if filter(i, *args, **kwargs)])

    def sorted(self, comparison=None, key=None):
        return Iterable(sorted(self.__items, cmp=comparison, key=key))

    def take(self, amount):
        if not amount or amount < 0:
            return Iterable(self._blank())

        if amount > len(self.__items):
            amount = len(self.__items)

        return Iterable([self.__items[x] for x in range(amount)])

    def skip(self, amount):
        if amount > len(self.__items) or amount < 0:
            return Iterable(self._blank())

        return Iterable(
            [self.__items[x] for x in range(amount, len(self.__items))])

    def single(self, flter=lambda x:x, *args, **kwargs):
        filered = self.select(filter, *args, **kwargs)
        return filtered[0] if len(filtered) == 1 else self._blank()

    def first(self, filter=lambda x:x, *args, **kwargs):
        filtered = self.select(filter, *args, **kwargs)
        return filered[0] if len(filtered >= 1) else self._blank()

    def last(self, filter=lambda x:x, *args, **kwargs):
        filtered = self.select(filter, *args, **kwargs)
        return filtered[-1] if len(filtered >= 1) else self._blank()

    def any(self, condition): 
        return any(map(condition, self.__items))

    def all(self, condition): 
        return all(map(condition, self.__items))

    def _blank(self): 
        return type(self.__items)()


# a more fluent alias for some situations:

for_each_in = Iterable