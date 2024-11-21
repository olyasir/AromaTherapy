from properties import NOTES,PLANT_PART, PROPERTY, OILS, FRAGNANCE

from base_oil import Base
class Clary_Sage(Base):
    part = PLANT_PART.LEAVE
    note = NOTES.TOP
    aroma_strength = None
    name = "Clary_Sage"
    oil_type = OILS.CLARY_SAGE
    fragnance = FRAGNANCE.HERBAL
    properties = [PROPERTY.Antidepressant,
                  PROPERTY.Antifungal, PROPERTY.Antioxidant,
                  PROPERTY.SKINCARE, PROPERTY.Digestion, PROPERTY.Hormone_Balance]
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

