from properties import NOTES, PLANT_PART, PROPERTY, OILS, AROMA_STRENGTH, FRAGNANCE
from base_oil import Base

class Lemongrass(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = AROMA_STRENGTH.Medium
    name = "Lemongrass"
    fragnance = FRAGNANCE.HERBAL
    oil_type = OILS.LEMONGRASS
    properties = [PROPERTY.Antibacterial, PROPERTY.Antifungal, PROPERTY.Anti_inflammatory, PROPERTY.Digestion]
    note = NOTES.TOP
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

