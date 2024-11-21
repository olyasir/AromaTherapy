from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE

from base_oil import Base
class Helichrysum(Base):
    part = PLANT_PART.FLOWER
    aroma_strength = None
    name = "Helichrysum"
    fragnance = FRAGNANCE.HERBAL
    oil_type = OILS.HELICHRYSUM
    properties = [PROPERTY.Wound_healing, PROPERTY.Antibacterial, PROPERTY.Antioxidant]
    note = NOTES.BASE
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

