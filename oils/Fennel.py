from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Fennel(Base):
    part = PLANT_PART.SEEDS
    aroma_strength = None
    name = "Fennel"
    note = NOTES.MIDDLE
    fragnance = FRAGNANCE.SPICY
    oil_type = OILS.FENNEL
    properties = []
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

