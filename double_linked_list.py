import weakref
from typing import Any, Optional
from linked_list import Node, LinkedList
# ToDo Документация


class DoubleNode(Node):
    def __init__(
            self, data: Any, next_node: Optional["Node"] = None, prev_node: Optional["Node"] = None
    ):
        super().__init__(data, next_node)
        self.prev_node = prev_node

    @property
    def prev_node(self):
        if self._prev_node is not None:
            return self._prev_node()
        else:
            return self._prev_node

    @prev_node.setter
    def prev_node(self, data):
        super()._check_instance(data)
        if data is not None:
            self._prev_node = weakref.ref(data)
        else:
            self._prev_node = data


class DoubleLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        self.tail = None

    def __str__(self):
        return "<->".join(str(node) for node in self._node_iter())

    def append(self, data: Any):
        new_node = DoubleNode(data)
        temporary_tail = self.tail

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            new_node.prev_node = temporary_tail
            temporary_tail.next_node = new_node

        self._size += 1

    def insert(self, data: Any, index=0):
        super()._check_index(index)
        super()._check_index_greater(index)

        new_node = DoubleNode(data)

        self._size += 1

        if index == len(self) - 1:
            self.tail = new_node
        if index == 0:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node
        else:
            for i, node in enumerate(self._node_iter()):
                if i == index - 1:
                    if node.next_node is not None:
                        node.next_node.prev_node = new_node
                        new_node.next_node = node.next_node
                    node.next_node = new_node
                    new_node.prev_node = node

    def delete(self, index: int):
        super()._check_index(index)
        super()._check_index_greater_equal(index)

        self._size -= 1
        if index == 0:
            self.head = self.head.next_node
        else:
            for i, node in enumerate(self._node_iter()):
                if i == index - 1:
                    if node.next_node.next_node is None:
                        self.tail = node
                        self.tail.prev_node = node.prev_node
                        self.tail.next_node = None
                    else:
                        node.next_node = node.next_node.next_node
                        node.next_node.next_node.prev_node = node

    def clear(self):
        super().clear()
        self.tail = None


def main():
    dll = DoubleLinkedList()
    dll.append("a")
    dll.append("b")
    dll.append("c")
    dll.append("d")
    dll.append("e")
    dll.append("f")
    dll.append("g")
    dll[6] = 'brrr'
    print(dll)
    print(dll.tail)
    print(repr(dll))
    print(dll.is_iterable())
    dll.remove("brrr")
    print(dll, dll.tail)
    dll.clear()
    print(dll.tail)


if __name__ == '__main__':
    main()
