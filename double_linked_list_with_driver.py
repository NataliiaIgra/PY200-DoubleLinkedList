from typing import Optional
from double_linked_list import DoubleLinkedList
from driver_fabric import *


# ToDo Документация


class DoubleLinkedListWithDriver(DoubleLinkedList):
    def __init__(self, driver: Optional["IStructureDriver"] = None):
        super().__init__()
        self.driver = driver

    @property
    def driver(self) -> IStructureDriver:
        if self._driver is None:
            some_driver = DriverFabric.get_driver()
            self._driver = some_driver
        return self._driver

    @driver.setter
    def driver(self, some_driver):
        if some_driver is not None and not isinstance(some_driver, IStructureDriver):
            raise TypeError('you can only use instances of class IStructureDriver')
        else:
            self._driver = some_driver

    def read(self):
        self.clear()
        for node in self.driver.read():
            self.append(node)

    def write(self):
        dll_as_list = [node for node in self]
        self.driver.write(dll_as_list)


def main():
    dll = DoubleLinkedListWithDriver(JsonFileDriver('lala.json'))
    dll.append('a')
    dll.append('b')
    dll.write()


if __name__ == '__main__':
    main()
