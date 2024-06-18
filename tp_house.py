import abc
import csv

class AbstractRepository(metaclass=abc.ABCMeta):


    def __init__(self):
        self.surfaces: list[float] = []
        self.loyers: list[float] = []

    @abc.abstractmethod
    def load(self, path): ...

    # @abc.abstractmethod
    # def filter(self, surface: float): ...
    #
    # @abc.abstractmethod
    # def loyer_per_m2(self) -> list[float]: ...
    #
    # @abc.abstractmethod
    # def loyer_per_m2_mean(self) -> float: ...


class HouseRepository(AbstractRepository):

    def __init__(self):
        super().__init__()

    def load(self, path):
        with open(path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                surface = int(row["surface"])
                loyer = int(row["loyer"])
                self.surfaces.append(surface)
                self.loyers.append(loyer)

