from properties import NOTES, PLANT_PART, PROPERTY, OILS, AROMA_STRENGTH, FRAGNANCE
from base_oil import Base

class Peppermint(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = AROMA_STRENGTH.Strong
    name = "Peppermint"
    fragnance = FRAGNANCE.HERBAL
    oil_type = OILS.PEPPERMINT
    note = NOTES.BASE
    properties = [PROPERTY.Cool, PROPERTY.Antimicrobial, PROPERTY.ENERGY, PROPERTY.UPLIFTING, PROPERTY.Breathing]
    def __init__(self):
        super().__init__(self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

