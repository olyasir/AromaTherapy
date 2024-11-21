from properties import PLANT_PART, PROPERTY, NOTES, OILS, FRAGNANCE
from base_oil import Base

class LemonEucaliptus(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = None
    name = "Lemon Eucaliptus"
    fragnance = FRAGNANCE.CITRUS
    oil_type = OILS.LEMON_EUCALIPTUS
    properties = []
    note = NOTES.MIDDLE
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

