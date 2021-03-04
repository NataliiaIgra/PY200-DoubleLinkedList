from typing import Any, Optional
# ToDo Документация


class Node:
    def __init__(self, data: Any, next_node: Optional["Node"] = None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return f"({self.data})"

    def __repr__(self):
        return f"{type(self).__name__}({self.data})"

    @staticmethod
    def _check_instance(data):
        if data is not None and not isinstance(data, Node):
            raise TypeError('you can only use None or instances of class Node')

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, data):
        self._check_instance(data)
        self._next_node = data


class LinkedList:
    def __init__(self):
        self._size = 0
        self.head = None

    def __str__(self):
        return "->".join(str(node) for node in self._node_iter())

    def __repr__(self):
        string = ",".join(repr(node) for node in self._node_iter())
        return f"{type(self).__name__}[{string}]"

    def __len__(self):
        return self._size

    @staticmethod
    def _check_index(index):
        if not isinstance(index, int):
            raise TypeError('list indices must be integers')

    def _check_index_greater_equal(self, index):
        if index < 0 or index >= len(self):
            raise IndexError('list index is out of range')

    def _check_index_greater(self, index):
        if index < 0 or index > len(self):
            raise IndexError('list index is out of range')

    def __getitem__(self, index):
        self._check_index(index)
        self._check_index_greater_equal(index)

        for i, node in enumerate(self._node_iter()):
            if i == index:
                return node.data

    def __setitem__(self, index, data):  # обновляет именно данные в Node
        self._check_index(index)
        self._check_index_greater_equal(index)

        for i, node in enumerate(self._node_iter()):
            if i == index:
                node.data = data

    def __delitem__(self, key):
        self.delete(key)

    def __iter__(self):
        for node in self._node_iter():
            yield node.data

    def _node_iter(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next_node

    def append(self, data: Any):
        new_node = Node(data)

        for current_node in self._node_iter():
            if current_node.next_node is None:  # tail!
                current_node.next_node = new_node
                break
        else:
            self.head = new_node

        self._size += 1

    def insert(self, data: Any, index=0):
        self._check_index(index)
        self._check_index_greater(index)

        new_node = Node(data)
        self._size += 1
        if index == 0:
            new_node.next_node = self.head
            self.head = new_node
        else:
            for i, node in enumerate(self._node_iter()):
                if i == index - 1:
                    new_node.next_node = node.next_node
                    node.next_node = new_node

    def clear(self):
        self._size = 0
        self.head = None

    def index(self, data: Any):
        for i, node in enumerate(self._node_iter()):
            if node.data == data:
                return i

        raise ValueError(f'{data} is not in the list')

    def delete(self, index: int):
        self._check_index(index)
        self._check_index_greater_equal(index)

        self._size -= 1
        if index == 0:
            self.head = self.head.next_node
        else:
            for i, node in enumerate(self._node_iter()):
                if i == index - 1:
                    node.next_node = node.next_node.next_node

    def remove(self, data: Any):
        found_index = self.index(data)
        self.delete(found_index)

    def is_iterable(self):
        check = hasattr(self, '__iter__')
        return check


def main():
    a = Node("a")
    a.next_node = Node("b")
    ll = LinkedList()
    ll.append("a")
    ll.append("b")
    ll.append("c")


if __name__ == '__main__':
    main()
