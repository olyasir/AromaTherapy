from properties import NOTES, PLANT_PART, PROPERTY, OILS, AROMA_STRENGTH, FRAGNANCE
from base_oil import Base

class TeaTree(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = AROMA_STRENGTH.Medium_Strong
    name = "Tea Tree"
    oil_type = OILS.TEA_TREE
    fragnance = FRAGNANCE.HERBAL
    note = NOTES.TOP
    properties = [PROPERTY.Antiviral, PROPERTY.Antibacterial]
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

