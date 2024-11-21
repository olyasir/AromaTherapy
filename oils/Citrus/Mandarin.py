from properties import NOTES, PLANT_PART, PROPERTY, OILS, AROMA_STRENGTH, FRAGNANCE
from base_oil import Base

class Mandarin(Base):
    part = PLANT_PART.PEEL
    aroma_strength = AROMA_STRENGTH.Medium
    name = "Mandarin"
    note = NOTES.TOP
    oil_type = OILS.MANDARIN
    fragnance = FRAGNANCE.CITRUS


    properties = [PROPERTY.UPLIFTING, PROPERTY.Light, PROPERTY.RELAXING, PROPERTY.Antiseptic,
                  PROPERTY.Antifungal, PROPERTY.Digestion]

    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

