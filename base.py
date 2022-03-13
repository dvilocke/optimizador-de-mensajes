from abc import  ABC, abstractmethod

class Base(ABC):

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def time(self) -> int:
        pass

    @abstractmethod
    def can_run(self) -> bool:
        #can be executed
        pass
