from properties import PLANT_PART, PROPERTY, NOTES, OILS, FRAGNANCE
from base_oil import Base

class Basil(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = None
    name = "Basil"
    fragnance = FRAGNANCE.HERBAL
    oil_type = OILS.BASIL
    properties = [PROPERTY.Antimicrobial, PROPERTY.SKINCARE, PROPERTY.Digestion]
    note = NOTES.TOP
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

