from properties import NOTES, PLANT_PART, PROPERTY, OILS, AROMA_STRENGTH, FRAGNANCE
from base_oil import Base

class Rosemary(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = AROMA_STRENGTH.Medium_Strong
    name = "Rosemary"
    oil_type = OILS.ROSEMARY
    note = NOTES.MIDDLE
    fragnance = FRAGNANCE.HERBAL
    properties = [PROPERTY.Antibacterial, PROPERTY.Anti_inflammatory,
                  PROPERTY.Sleep, PROPERTY.Mood_Improvment,
                  PROPERTY.Learning, PROPERTY.RELAXING, PROPERTY.Anti_Pain, PROPERTY.Memory]
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

