from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Lemon(Base):
    part = PLANT_PART.PEEL
    aroma_strength = None
    name = "Lemon"
    oil_type = OILS.LEMON
    note = NOTES.TOP
    fragnance = FRAGNANCE.CITRUS

    properties = [PROPERTY.UPLIFTING, PROPERTY.Light, PROPERTY.Breathing, PROPERTY.Alergy, PROPERTY.cough,
                  PROPERTY.immune_system, PROPERTY.Anti_inflammatory, PROPERTY.Antibacterial,
                  PROPERTY.Antioxidant]

    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

