from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Thyme(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = None
    name = "Thyme"
    oil_type = OILS.THYME
    fragnance = FRAGNANCE.HERBAL
    note = NOTES.TOP
    properties = [PROPERTY.Antimicrobial]

    def __init__(self):
        super().__init__(self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

