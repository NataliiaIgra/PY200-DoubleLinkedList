import json
import pickle
from abc import ABC, abstractmethod
from typing import Sequence


# ToDo Документация


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Sequence:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер
        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Sequence) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер
        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class JsonFileDriver(IStructureDriver):
    def __init__(self, filename: str):
        self._filename = filename

    def read(self) -> Sequence:
        with open(self._filename) as file:
            return json.load(file)

    def write(self, data: Sequence) -> None:
        with open(self._filename, "w") as file:
            json.dump(data, file)


class PickleFileDriver(IStructureDriver):
    def __init__(self, filename: str):
        self._filename = filename

    def read(self) -> Sequence:
        with open(self._filename, "rb") as file:
            return pickle.load(file)

    def write(self, data: Sequence) -> None:
        with open(self._filename, "wb") as file:
            pickle.dump(data, file)


class DriverBuilder(ABC):
    @abstractmethod
    def build(self):
        ...


class JsonFileBuilder(DriverBuilder):
    DEFAULT_NAME = 'untitled.json'

    @classmethod
    def build(cls) -> IStructureDriver:
        filename = input('Введите название json файла (.json): ').strip()
        filename = filename or cls.DEFAULT_NAME
        if not filename.endswith('.json'):
            filename = f'{filename}.json'

        return JsonFileDriver(filename)


class PickleFileBuilder(DriverBuilder):
    DEFAULT_NAME = 'untitled.pickle'

    @classmethod
    def build(cls) -> IStructureDriver:
        filename = input('Введите название pickle файла (.bin): ').strip()
        filename = filename or cls.DEFAULT_NAME
        if not filename.endswith('.bin'):
            filename = f'{filename}.bin'

        return PickleFileDriver(filename)


class DriverFabric:
    DRIVER_BUILDER = {
        'json_file': JsonFileBuilder,
        'pickle_file': PickleFileBuilder
    }
    DEFAULT_DRIVER = 'json_file'

    @classmethod
    def get_driver(cls):
        driver_name = input("Введите название драйвера (json_file или pickle_file): ")
        driver_name = driver_name or cls.DEFAULT_DRIVER

        driver_builder = cls.DRIVER_BUILDER[driver_name]
        return driver_builder.build()
