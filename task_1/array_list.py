from array import array


# MutableSequence:
# __getitem__()
# __setitem__()
# __delitem__()
# __len__()
# insert()
# __contains__()
# __iter__()
# __reversed__()
# index()
# count()
# append()
# reverse()
# extend()
# pop()
# remove()
# __iadd__

# Available types:
# 'b'         signed integer
# 'B'         unsigned integer
# 'u'         Unicode character
# 'h'         signed integer
# 'H'         unsigned integer
# 'i'         signed integer
# 'I'         unsigned integer
# 'l'         signed integer
# 'L'         unsigned integer
# 'q'         signed integer
# 'Q'         unsigned integer
# 'f'         floating point
# 'd'         floating point


def _signed_integer(item):
    return isinstance(item, int)


def _unsigned_integer(item):
    return _signed_integer(item) and not item < 0


def _floating_point(item):
    return isinstance(item, float)


def _unicode_character(item):
    return isinstance(item, str) and len(item) == 1


_arr_types = {
    'b': _signed_integer,
    'B': _unsigned_integer,
    'u': _unicode_character,
    'h': _signed_integer,
    'H': _unsigned_integer,
    'i': _signed_integer,
    'I': _unsigned_integer,
    'l': _signed_integer,
    'L': _unsigned_integer,
    'q': _signed_integer,
    'Q': _unsigned_integer,
    'f': _floating_point,
    'd': _floating_point
}


class ArrayListIterator:
    def __init__(self, container, reverse=False):
        assert isinstance(container, array)
        self._container = container
        self._step = -1 if reverse else 1
        self._position = -1 if reverse else 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            elem = self._container[self._position]
        except IndexError:
            raise StopIteration
        self._position += self._step
        return elem


class ArrayList:
    _data: array
    _type: str

    def __init__(self, arr_type, iterable):
        if arr_type not in _arr_types:
            raise TypeError(
                f"Type '{arr_type}' is not supported."
                f"Supported types are: {_arr_types.keys()}"
            )
        self._type = arr_type
        self._type_check(*iterable)
        self._data = array(arr_type, iterable)

    def __getitem__(self, item):
        return self._data[item]

    def __setitem__(self, key, value):
        self._type_check(value)
        self._data[key] = value

    def __delitem__(self, key):
        self._data = self._data[:key] + self._data[key + 1:]

    def __len__(self):
        return len(self._data)

    def __contains__(self, item):
        return item in self._data

    def __iter__(self):
        return ArrayListIterator(self._data)

    def __reversed__(self):
        return ArrayListIterator(self._data,
                                 reverse=True)

    def insert(self, key, value):
        self._type_check(value)
        self._data = self._data[:key] + array(self._type, [value]) + self._data[key:]

    def index(self, item):
        for i, elem in enumerate(self._data):
            if item == elem: return i
        raise ValueError(f"{item} is not in list")

    def count(self, item):
        count = 0
        for elem in self._data:
            if elem == item: count += 1
        return count

    def append(self, item):
        self._type_check(item)
        self._data += array(self._type, [item])

    def reverse(self):
        self._data = self._data[::-1]

    def extend(self, other):
        if not isinstance(other, ArrayList):
            raise TypeError(f"Can only extend ArrayList with ArrayList"
                            f"(not '{type(other)}')")
        if self._type != other._type:
            raise TypeError(f"Can only extend ArrayLists of the same type"
                            f"('{self._type}' vs '{other._type}')")
        self._data += other._data

    def pop(self, key):
        item = self._data[key]
        if key < 0: key += len(self._data)
        self._data = self._data[:key] + self._data[key + 1:]
        return item

    def remove(self, item):
        for i, elem in enumerate(self._data):
            if elem == item:
                self._data = self._data[:i] + self._data[i + 1:]
                return

    def __iadd__(self, other):
        self.extend(other)
        return self

    def _type_check(self, *args):
        for elem in args:
            if not _arr_types[self._type](elem):
                raise TypeError(
                    f"Expected type '{self._type}'."
                    f"Found '{type(elem)}'"
                )
