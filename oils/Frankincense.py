from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Frankincense(Base):
    part = PLANT_PART.RESIN
    aroma_strength = None
    name = "Frankincense"
    fragnance = FRAGNANCE.WOODY
    oil_type = OILS.FRANKINCENSE
    note = NOTES.BASE
    properties = []
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

