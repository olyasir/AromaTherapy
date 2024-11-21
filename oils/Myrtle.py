from properties import PLANT_PART, PROPERTY, OILS, NOTES, FRAGNANCE
from base_oil import Base

class Myrtle(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = None
    name = "Myrtle"
    oil_type = OILS.MYRTLE
    fragnance = FRAGNANCE.WOODY
    properties = []
    note = NOTES.MIDDLE
    def __init__(self):
        super().__init__(self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

