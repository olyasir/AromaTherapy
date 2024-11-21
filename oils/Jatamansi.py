from properties import PLANT_PART, PROPERTY, OILS, NOTES, FRAGNANCE

from base_oil import Base
class Jatamansi(Base):
    part = PLANT_PART.ROOT
    aroma_strength = None
    oil_type = OILS.JATAMANSI
    name = "Jatamansi"
    fragnance = FRAGNANCE.WOODY
    properties = []
    note = NOTES.BASE

    def __init__(self):
        super().__init__(self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

