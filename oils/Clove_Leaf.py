from properties import NOTES,PLANT_PART, PROPERTY, OILS, AROMA_STRENGTH, FRAGNANCE

from base_oil import Base
class Clove_Leaf(Base):
    part = PLANT_PART.LEAVE
    note = NOTES.MIDDLE
    aroma_strength = AROMA_STRENGTH.Medium
    name = "Clove Leaf"
    oil_type = OILS.CLOVE_LEAF
    fragnance = FRAGNANCE.SPICY
    properties = [PROPERTY.immune_system,
                  PROPERTY.Digestion,
                  PROPERTY.SKINCARE]
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

