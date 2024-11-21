from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Cardamon(Base):
    note = NOTES.MIDDLE
    part = PLANT_PART.SEEDS
    aroma_strength = None
    name = "Cardamon"
    fragnance = FRAGNANCE.SPICY
    oil_type = OILS.CARDAMON
    properties = [PROPERTY.Aphrodisiac, PROPERTY.Antibacterial, PROPERTY.Antifungal,
                  PROPERTY.Detoxing, PROPERTY.Antidepressant]
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

