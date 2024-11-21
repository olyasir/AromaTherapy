from properties import NOTES, PLANT_PART, PROPERTY, OILS, AROMA_STRENGTH, FRAGNANCE

from base_oil import Base
class YlangYlang(Base):
    part = PLANT_PART.FLOWER
    aroma_strength = AROMA_STRENGTH.Medium
    fragnance = FRAGNANCE.FLORAL
    name = "YlangYlang"
    oil_type = OILS.YLANG_YLANG
    properties = [PROPERTY.Aphrodisiac, PROPERTY.Sleep, PROPERTY.Anti_inflammatory, PROPERTY.RELAXING,
                  PROPERTY.Digestion, PROPERTY.Wound_healing, PROPERTY.Skin, PROPERTY.Antibacterial]
    note = NOTES.BASE
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

