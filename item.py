#!/usr/bin/env python3



import enum

class InhabitantClass(enum.Enum):
        NONE = 0
        BEGGAR = 10
        PEASANT = 11
        CITIZEN = 12
        PATRICIAN = 13
        NOBLEMAN = 14
        NOMAD = 20
        ENVOY = 21

class ProductionBuilding:

        def __init__(
                        self,
                        beggar=-1,
                        peasant=-1,
                        citizen=-1,
                        patrician=-1,
                        nobleman=-1,
                        nomad=-1,
                        envoy=-1,
        ):
                self.inhab_cnt = {}
                self.set_beggar(beggar).set_peasant(peasant)\
                                .set_citizen(citizen)\
                                .set_patrician(patrician)\
                                .set_nobleman(nobleman)\
                                .set_nomad(nomad)\
                                .set_envoy(envoy)

        def __repr__(self):
                return '<%s(%d, %d, %d, %d, %d, %d, %d)>' % (
                                type(self).__name__,
                                self.get_beggar(),
                                self.get_peasant(),
                                self.get_citizen(),
                                self.get_patrician(),
                                self.get_nobleman(),
                                self.get_nomad(),
                                self.get_envoy(),
                )

        def set_class(self, cls, nbr):
                print('cls: ', cls, 'nbr: ', nbr)
                if type(cls) is not int:
                        cls = cls.value
                self.inhab_cnt[cls] = nbr

        def get_class(self, cls):
                if type(cls) is not int:
                        cls = cls.value
                if cls not in self.inhab_cnt:
                        return -1
                return self.inhab_cnt[cls]

        def set_beggar(self, nbr):
                self.set_class(InhabitantClass.BEGGAR, nbr)
                return self

        def set_peasant(self, nbr):
                self.set_class(InhabitantClass.PEASANT, nbr)
                return self

        def set_citizen(self, nbr):
                self.set_class(InhabitantClass.CITIZEN, nbr)
                return self

        def set_patrician(self, nbr):
                self.set_class(InhabitantClass.PATRICIAN, nbr)
                return self

        def set_nobleman(self, nbr):
                self.set_class(InhabitantClass.NOBLEMAN, nbr)
                return self

        def set_nomad(self, nbr):
                self.set_class(InhabitantClass.NOMAD, nbr)
                return self

        def set_envoy(self, nbr):
                self.set_class(InhabitantClass.ENVOY, nbr)
                return self

        def get_beggar(self):
                return self.get_class(InhabitantClass.BEGGAR)

        def get_peasant(self):
                return self.get_class(InhabitantClass.PEASANT)

        def get_citizen(self):
                return self.get_class(InhabitantClass.CITIZEN)

        def get_patrician(self):
                return self.get_class(InhabitantClass.PATRICIAN)

        def get_nobleman(self):
                return self.get_class(InhabitantClass.NOBLEMAN)

        def get_nomad(self):
                return self.get_class(InhabitantClass.NOMAD)

        def get_envoy(self):
                return self.get_class(InhabitantClass.ENVOY)

        def get_prod_building_percent(self, inhabs):
                cnt = 0.0
                for inhab_type, c in inhabs:
                        c = c/self.get_class(inhab_type)
                        if c < 0:
                                continue
                        cnt += c
                return cnt




FISH = ProductionBuilding(beggar=285, peasant=200, citizen=500,
                patrician=909, nobleman=1250)
SPICES = ProductionBuilding(citizen=500, patrician=909, nobleman=1250)
BREAD = ProductionBuilding(patrician=727, nobleman=1025)
MEAT = ProductionBuilding(nobleman=1136)

CIDER = ProductionBuilding(beggar=500, peasant=340, citizen=340,
                patrician=652, nobleman=1153)
BEER = ProductionBuilding(patrician=625, nobleman=1071)
WINE = ProductionBuilding(nobleman=1000)

LINEN = ProductionBuilding(citizen=476, patrician=1052, nobleman=2500)
LEATHER = ProductionBuilding(patrician=1428, nobleman=2500)
FUR = ProductionBuilding(nobleman=1562)
BROCADE = ProductionBuilding(nobleman=2112)

BOOKS = ProductionBuilding(patrician=1875, nobleman=3333)
CANDLES = ProductionBuilding(patrician=2500, nobleman=3333)
GLASSES = ProductionBuilding(nobleman=1709)

DATES = ProductionBuilding(nomad=450, envoy=600)
MARZIPAN = ProductionBuilding(envoy=2453)

MILK = ProductionBuilding(nomad=436, envoy=666)
COFFEE = ProductionBuilding(envoy=1000)

CARPET = ProductionBuilding(nomad=909, envoy=1500)
PEARL_NECKLACE = ProductionBuilding(envoy=751)
PARFUM = ProductionBuilding(envoy=1250)




if __name__ == '__main__':
        print(FISH.get_prod_building_percent([(10, 500)]))
        print(CIDER.get_prod_building_percent([(10, 500)]))
