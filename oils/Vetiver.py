from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE

from base_oil import Base
class Vetiver(Base):
    part = PLANT_PART.ROOT
    aroma_strength = None
    name = "Vetiver"
    oil_type = OILS.VERIVER
    fragnance = FRAGNANCE.WOODY
    properties = [PROPERTY.Grounding, PROPERTY.Heavy, PROPERTY.Stress_Relief,
                  PROPERTY.SKINCARE, PROPERTY.Skin, PROPERTY.Anti_Pain,
                  PROPERTY.immune_system, PROPERTY.Sleep, PROPERTY.Aphrodisiac,
                  PROPERTY.Wound_healing , PROPERTY.SEDATIVE]
    note = NOTES.BASE
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

