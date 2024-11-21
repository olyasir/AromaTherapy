from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Dill(Base):
    part = PLANT_PART.SEEDS
    aroma_strength = None
    name = "Dill"
    oil_type = OILS.DILL
    fragnance = FRAGNANCE.HERBAL
    properties = [PROPERTY.Digestion, PROPERTY.Wound_healing, PROPERTY.STRENGTH]
    note = NOTES.MIDDLE
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

