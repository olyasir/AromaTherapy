from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Juniper(Base):
    part = PLANT_PART.SEEDS # this is from berried - the friut?
    aroma_strength = None
    name = "Juniper"
    oil_type = OILS.JUNIPER
    fragnance = FRAGNANCE.WOODY
    properties = [PROPERTY.Detoxing]
    note = NOTES.MIDDLE
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

