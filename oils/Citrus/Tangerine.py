from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE

from base_oil import Base

class Tangerine(Base):
    part = PLANT_PART.PEEL
    aroma_strength = None
    name = "Tangerine"
    fragnance = FRAGNANCE.CITRUS
    note = NOTES.TOP
    oil_type = OILS.TANGERINE
    properties = [PROPERTY.Antibacterial, PROPERTY.Wound_healing]
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

