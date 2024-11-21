from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Marjoram(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = None
    name = "Marjoram"
    oil_type = OILS.MARJORAM
    fragnance = FRAGNANCE.HERBAL
    properties = [PROPERTY.Anti_inflammatory, PROPERTY.Antimicrobial, PROPERTY.Anti_Pain,
                  PROPERTY.Aphrodisiac, PROPERTY.Antiseptic, PROPERTY.Antiviral]
    note = NOTES.MIDDLE
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

