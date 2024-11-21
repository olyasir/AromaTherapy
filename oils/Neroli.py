from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Neroli(Base):
    part = PLANT_PART.FLOWER
    aroma_strength = None
    name = "Neroli"
    fragnance = FRAGNANCE.CITRUS
    oil_type = OILS.NEROLI
    note = NOTES.BASE
    properties = [PROPERTY.Hormone_Balance, PROPERTY.Skin, PROPERTY.SKINCARE, PROPERTY.Anti_inflammatory,
                  PROPERTY.Stress_Relief, PROPERTY.Antioxidant]
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

