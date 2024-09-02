class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.stack = [(list_of_list, 0)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            list_of_list, index = self.stack[-1]
            if index >= len(list_of_list):
                self.stack.pop()
            else:
                item = list_of_list[index]
                self.stack[-1] = (list_of_list, index + 1)
                if isinstance(item, list):
                    self.stack.append((item, 0))
                else:
                    return item
        raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()