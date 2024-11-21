from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE

from base_oil import Base
class Ginger(Base):
    part = PLANT_PART.ROOT
    aroma_strength = None
    name = "Ginger"
    oil_type = OILS.GINGER
    fragnance = FRAGNANCE.SPICY
    properties = [PROPERTY.Grounding, PROPERTY.Digestion,
                  PROPERTY.Detoxing, PROPERTY.UPLIFTING, PROPERTY.UPLIFTING,
                  PROPERTY.SKINCARE, PROPERTY.Aphrodisiac, PROPERTY.Sleep]
    note = NOTES.BASE
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

