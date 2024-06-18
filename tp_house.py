import abc
import csv

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
    def loyer_per_m2_mean(self, loyer_per_m2) -> float: ...


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

    def filter(self, surface):
        loyers = []
        surfaces = []
        for i in range(len(self.surfaces)):
            if self.surfaces[i] < surface:
                loyers.append(self.loyers[i])
                surfaces.append(self.surfaces[i])
        self.loyers = loyers
        self.surfaces = surfaces

    def filter(self, surface_max):
        res = ((loyer, surface) for loyer, surface in zip(self.loyers, self.surfaces) if surface < surface_max)
        self.loyers = (loyer for loyer, surface in res)
        self.surfaces = (surface for loyer, surface in res)

    def loyer_per_m2(self) -> list[float]:
        res = (loyer / surface for loyer, surface in zip(self.loyers, self.surfaces))
        return res

    def loyer_per_m2_mean(self, loyer_per_m2) -> float:
        return sum(loyer_per_m2) / len(loyer_per_m2)





