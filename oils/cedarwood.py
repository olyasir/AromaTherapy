from properties import PROPERTY, NOTES, PLANT_PART, OILS, FRAGNANCE
from base_oil import Base

class Cedarwood(Base):
    part = PLANT_PART.WOOD
    aroma_strength = 1
    name = "Cedarwood"
    fragnance = FRAGNANCE.WOODY
    oil_type = OILS.CEDARWOOD
    properties = [PROPERTY.RELAXING, PROPERTY.Brain_Function, PROPERTY.Clear_Mind]
    note = NOTES.BASE
    def __init__(self):
        super().__init__(self.__class__.part, self.__class__.name, self.__class__.properties,
                         self.__class__.aroma_strength)


