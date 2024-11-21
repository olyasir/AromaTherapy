from properties import NOTES, PLANT_PART, PROPERTY, OILS, AROMA_STRENGTH, FRAGNANCE
from base_oil import Base

class Spearmint(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = AROMA_STRENGTH.Medium
    name = "Spearmint"
    oil_type = OILS.SPEARMINT
    note = NOTES.TOP
    fragnance = FRAGNANCE.HERBAL
    properties = [PROPERTY.Digestion, PROPERTY.Antioxidant, PROPERTY.Hormone_Balance, PROPERTY.Memory,
                  PROPERTY.Antibacterial, PROPERTY.Stress_Relief]
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

