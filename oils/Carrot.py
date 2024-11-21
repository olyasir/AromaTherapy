from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Carrot(Base):
    note = NOTES.MIDDLE
    part = PLANT_PART.SEEDS
    aroma_strength = None
    name = "Carrot"
    oil_type = OILS.CARROT
    fragnance = FRAGNANCE.WOODY
    properties = [PROPERTY.SKINCARE, PROPERTY.Anti_inflammatory]
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

