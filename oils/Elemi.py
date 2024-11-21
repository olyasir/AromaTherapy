from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Elemi(Base):
    part = PLANT_PART.RESIN
    aroma_strength = None
    name = "Elemi"
    fragnance = FRAGNANCE.WOODY
    oil_type = OILS.ELEMI
    note = NOTES.TOP
    properties = [PROPERTY.ENERGY, PROPERTY.STRENGTH, PROPERTY.Cleansing, PROPERTY.Clear_Mind]
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

