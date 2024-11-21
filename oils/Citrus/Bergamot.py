from properties import NOTES,PLANT_PART, PROPERTY, FRAGNANCE, OILS, AROMA_STRENGTH, FRAGNANCE
from base_oil import Base

class Bergamot(Base):
    part = PLANT_PART.PEEL
    oil_type = OILS.BERGAMOT
    aroma_strength = AROMA_STRENGTH.Medium
    name = "Bergamot"
    fragnance = FRAGNANCE.CITRUS
    properties = [PROPERTY.UPLIFTING, PROPERTY.Detoxing, PROPERTY.Light]
    note = NOTES.TOP
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

