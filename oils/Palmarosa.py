from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Palmarosa(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = None
    name = "Palmarosa"
    fragnance = FRAGNANCE.FLORAL
    oil_type = OILS.PALMAROSA
    properties = [PROPERTY.Antifungal, PROPERTY.Anti_inflammatory,
                  PROPERTY.Antiseptic, PROPERTY.RELAXING, PROPERTY.SKINCARE]
    note = NOTES.MIDDLE
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

