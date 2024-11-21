from properties import NOTES, PLANT_PART, PROPERTY, OILS, AROMA_STRENGTH, FRAGNANCE
from base_oil import Base

class Lavender(Base):
    part = PLANT_PART.FLOWER
    aroma_strength = AROMA_STRENGTH.Medium
    name = "Lavender"
    fragnance = FRAGNANCE.FLORAL
    oil_type = OILS.LAVANDER
    properties = [PROPERTY.SEDATIVE, PROPERTY.RELAXING,
                  PROPERTY.Anti_inflammatory, PROPERTY.Stress_Relief, PROPERTY.SKINCARE]
    note = NOTES.MIDDLE
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

