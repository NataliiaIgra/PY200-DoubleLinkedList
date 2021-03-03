import sys
import weakref
from typing import Any, Optional
from linked_list import Node, LinkedList


class DoubleNode(Node):
    def __init__(
            self, data: Any, next_node: Optional["Node"] = None, prev_node: Optional["Node"] = None
    ):
        super().__init__(data, next_node)
        self.prev_node = prev_node

    @property
    def prev_node(self):
        return self._prev_node()

    @prev_node.setter
    def prev_node(self, data):
        super()._check_instance(data)
        if data is not None:
            self._prev_node = weakref.ref(data)
        else:
            self._prev_node = data


class DoubleLinkedList(LinkedList):
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
        ...





def main():
    dll = DoubleLinkedList()
    a = DoubleNode('brrra')
    dll.append("a")
    dll.append("b")
    dll.append("c")
    dll.append("d")
    dll.append("e")
    dll.append("f")
    dll.append("g")
    print(dll.head.next_node.prev_node)


if __name__ == '__main__':
    main()