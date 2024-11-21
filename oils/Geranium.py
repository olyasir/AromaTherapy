from properties import NOTES, PLANT_PART, PROPERTY, OILS, AROMA_STRENGTH, FRAGNANCE
from base_oil import Base

class Geranium(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = AROMA_STRENGTH.Strong
    name = "Geranium"
    note = NOTES.MIDDLE
    oil_type = OILS.GERANIUM
    fragnance = FRAGNANCE.FLORAL
    properties = [PROPERTY.SKINCARE, PROPERTY.Hormone_Balance, PROPERTY.Anti_inflammatory, PROPERTY.Wound_healing, PROPERTY.RELAXING]
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

