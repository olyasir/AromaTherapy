from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Pine(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = None
    name = "Pine"
    oil_type = OILS.PINE
    fragnance = FRAGNANCE.WOODY
    note = NOTES.TOP
    properties = []
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

