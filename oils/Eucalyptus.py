from properties import NOTES, PLANT_PART, PROPERTY, OILS, AROMA_STRENGTH,FRAGNANCE
from base_oil import Base

class Eucalyptus(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = AROMA_STRENGTH.Strong
    name = "Eucalyptus"
    oil_type = OILS.EUCALYPTUS
    fragnance = FRAGNANCE.HERBAL
    note = NOTES.TOP
    properties = [PROPERTY.Wound_healing, PROPERTY.Antibacterial, PROPERTY.Clear_Mind, PROPERTY.Breathing, PROPERTY.immune_system]
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

