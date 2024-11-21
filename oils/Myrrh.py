from properties import PLANT_PART, PROPERTY, OILS, NOTES, FRAGNANCE
from base_oil import Base

class Myrrh(Base):
    part = PLANT_PART.RESIN
    aroma_strength = None
    name = "Myrrh"
    oil_type = OILS.MYRHH
    note = NOTES.BASE
    fragnance = FRAGNANCE.SPICY
    properties = [PROPERTY.Anti_inflammatory, PROPERTY.Antioxidant,
                  PROPERTY.Digestion, PROPERTY.Wound_healing]
    def __init__(self):
        super().__init__(self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

