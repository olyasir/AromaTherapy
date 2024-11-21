from properties import PLANT_PART, PROPERTY, OILS, NOTES, FRAGNANCE
from base_oil import Base

class Caraway(Base):
    part = PLANT_PART.SEEDS
    aroma_strength = None
    name = "Caraway"
    fragnance = FRAGNANCE.HERBAL
    oil_type = OILS.CARAWAY
    properties = [PROPERTY.Digestion]
    note = NOTES.MIDDLE
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

