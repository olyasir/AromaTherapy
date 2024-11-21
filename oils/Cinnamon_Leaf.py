from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Cinnamon(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = None
    name = "Cinnamon"
    fragnance = FRAGNANCE.SPICY
    oil_type = OILS.CINNAMON_LEAF
    properties = [PROPERTY.Hot, PROPERTY.Detoxing, PROPERTY.Antiviral, PROPERTY.immune_system]
    note = NOTES.BASE
    def __init__(self):
        super().__init__(self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

