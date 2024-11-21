from properties import PROPERTY, NOTES, PLANT_PART, OILS, FRAGNANCE
from base_oil import Base

class Sandalwood(Base):
    part = PLANT_PART.WOOD
    aroma_strength = 1
    name = "Sandalwood"
    oil_type = OILS.SANDALWOOD
    fragnance = FRAGNANCE.WOODY
    properties = [PROPERTY.Stress_Relief, PROPERTY.Wound_healing, PROPERTY.Anti_inflammatory, PROPERTY.Sleep, PROPERTY.PROTECT,
                  PROPERTY.Antioxidant, PROPERTY.SKINCARE, PROPERTY.Antiseptic, PROPERTY.Antiviral]
    note = NOTES.BASE
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

