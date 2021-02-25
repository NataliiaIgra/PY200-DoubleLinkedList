from typing import Any, Optional
from linked_list import Node, LinkedList


class DoubleNode(Node):
    def __init__(
            self, data: Any, next_node: Optional["Node"] = None, prev_node: Optional["Node"] = None
    ):
        super().__init__(data, next_node)
        self.prev_node = prev_node

    def __str__(self):
        return f"[{self.data}]"

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise ValueError

        self._prev_node = value
