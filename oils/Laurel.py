from properties import PLANT_PART, PROPERTY, OILS, NOTES, FRAGNANCE
from base_oil import Base

class Laurel(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = None
    name = "Laurel"
    oil_type = OILS.LAUREL
    fragnance = FRAGNANCE.HERBAL
    properties = [PROPERTY.Breathing, PROPERTY.Digestion, PROPERTY.Stress_Relief]
    note = NOTES.TOP
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

