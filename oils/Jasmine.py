from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Jasmine(Base):
    part = PLANT_PART.FLOWER
    aroma_strength = None
    name = "Jasmine"
    oil_type = OILS.JASMINE
    note = NOTES.BASE
    fragnance = FRAGNANCE.FLORAL
    properties = [PROPERTY.SKINCARE,
                  PROPERTY.Antibacterial, PROPERTY.Skin]
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

