from properties import NOTES, PLANT_PART, PROPERTY, OILS, AROMA_STRENGTH, FRAGNANCE
from base_oil import Base

class Grapefruit(Base):
    part = PLANT_PART.PEEL
    aroma_strength = AROMA_STRENGTH.Medium
    name = "Grapefruit"
    oil_type = OILS.GRAPEFRUIT
    note = NOTES.TOP
    fragnance = FRAGNANCE.CITRUS
    properties = [PROPERTY.UPLIFTING, PROPERTY.Detoxing, PROPERTY.Light]

    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

