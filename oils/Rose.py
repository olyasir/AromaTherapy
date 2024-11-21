from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Rose(Base):
    part = PLANT_PART.FLOWER
    aroma_strength = None
    name = "Rose"
    oil_type = OILS.ROSE
    properties = []
    fragnance = FRAGNANCE.FLORAL
    note = NOTES.BASE
    def __init__(self):
        super().__init__(self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

