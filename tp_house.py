import abc

class AbstractRepository(metaclass=abc.ABCMeta):


    def __init__(self):
        self.surfaces: list[float] = []
        self.loyers: list[float] = []

    @abc.abstractmethod
    def load(self, path): ...

    @abc.abstractmethod
    def filter(self, surface: float): ...

    @abc.abstractmethod
    def loyer_per_m2(self) -> list[float]: ...

    @abc.abstractmethod
    def loyer_per_m2_mean(self) -> float: ...
