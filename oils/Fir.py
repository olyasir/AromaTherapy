from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Fir(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = None
    name = "Fir"
    oil_type = OILS.FIR
    fragnance = FRAGNANCE.HERBAL
    note = NOTES.MIDDLE
    properties = []
    def __init__(self):
        super().__init__(self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

