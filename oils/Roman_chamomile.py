from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class RomanCamomile(Base):
    part = PLANT_PART.FLOWER
    aroma_strength = None
    name = "Roman chamomile"
    fragnance = FRAGNANCE.HERBAL
    oil_type = OILS.ROMAN_CAMOMILE
    properties = [PROPERTY.Anti_Pain, PROPERTY.Sleep, PROPERTY.SEDATIVE, PROPERTY.RELAXING]
    note = NOTES.MIDDLE
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

