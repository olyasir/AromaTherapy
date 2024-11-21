from properties import PLANT_PART, PROPERTY, OILS, NOTES, FRAGNANCE

from base_oil import Base
class Nard(Base):
    part = PLANT_PART.ROOT
    aroma_strength = None
    name = "Nard"
    oil_type = OILS.NARD
    fragnance = FRAGNANCE.WOODY
    properties = [PROPERTY.Grounding]
    note = NOTES.BASE
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

