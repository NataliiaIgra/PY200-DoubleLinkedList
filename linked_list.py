from typing import Any, Optional
import sys


class Node:
    def __init__(self, data: Any, next_node: Optional["Node"] = None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return f"({self.data})"

    def __repr__(self):
        return f"{type(self).__name__}({self.data})"

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise ValueError

        self._next_node = value


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
        self.tail = None  # ToDo добавить tail в LinkedList

    def __str__(self):
        return "->".join(str(node) for node in self._node_iter())

    def __repr__(self):
        string = ",".join(repr(node) for node in self._node_iter())
        return f"{type(self).__name__}[{string}]"

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError('Linked list indices must be integers')

        if index >= len(self) or index < 0:
            raise IndexError('Linked list index is out of range')

        for i, node in enumerate(self._node_iter()):
            if i == index:
                return node.data

    def __setitem__(self, key, value):  # обновляет именно данные в Node
        if not isinstance(key, int):
            raise TypeError('Linked list indices must be integers')

        if key >= len(self) or key < 0:
            raise IndexError('Linked list index is out of range')

        for i, node in enumerate(self._node_iter()):
            if i == key:
                node.data = value

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
        if not isinstance(index, int):
            raise TypeError('Linked list indices must be integers')

        if index < 0 or index > self._size:
            raise ValueError('Linked list index is out of range')

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

        raise ValueError(f'{data} is not in linked list')

    def delete(self, index: int):
        if not isinstance(index, int):
            raise TypeError('Linked list indices must be integers')

        if index < 0 or index >= self._size:
            raise ValueError('Linked list index is out of range')

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

    def sort(self):
        sorted_list = sorted(self)
        for index, node in enumerate(sorted_list):
            self[index] = node

    def is_iterable(self):
        check = hasattr(self, '__iter__')
        return check

# ToDo Поменять append
# ToDo Документация


def main():
    ll = LinkedList()
    ll.append("a")
    ll.append("b")
    ll.append("c")
    ll.append("d")
    ll.append("e")
    ll.append("f")
    ll.append("g")
    print(sys.getrefcount(ll))


if __name__ == '__main__':
    main()
