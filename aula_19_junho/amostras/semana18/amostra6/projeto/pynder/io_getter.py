from abc import ABC, abstractmethod


class IoGetter(ABC):
    @abstractmethod
    def get_io(self):
        """ Returns an iterrable with lines from file"""
        pass


class GenericIoGetter(IoGetter):
    def get_io(self, file_name):
        return open(file_name, "r")


class XlsIoGetter(IoGetter):
    def get_io(self, file_name):
        return NotImplementedError()
