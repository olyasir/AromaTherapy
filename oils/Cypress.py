from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Cypress(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = None
    name = "Cypress"
    oil_type = OILS.CYPRESS
    fragnance = FRAGNANCE.HERBAL
    properties = [PROPERTY.Clear_Mind, PROPERTY.ENERGY, PROPERTY.Cleansing, PROPERTY.Antibacterial]
    note = NOTES.MIDDLE
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

