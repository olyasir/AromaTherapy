from properties import PLANT_PART, PROPERTY, NOTES, OILS, FRAGNANCE
from base_oil import Base

class Citronela(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = None
    name = "Citronela"
    fragnance = FRAGNANCE.HERBAL
    oil_type = OILS.CITRONELA
    properties = []
    note = NOTES.MIDDLE
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

