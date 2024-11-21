from properties import PLANT_PART, PROPERTY, OILS, NOTES, FRAGNANCE
from base_oil import Base

class Black_Pepper(Base):
    part = PLANT_PART.SEEDS
    aroma_strength = None
    name = "Black Pepper"
    oil_type = OILS.BLACK_PEPPER
    fragnance = FRAGNANCE.SPICY
    properties = [PROPERTY.Antioxidant, PROPERTY.Stress_Relief, PROPERTY.Digestion,
                  PROPERTY.Anti_Pain, PROPERTY.ENERGY]
    note = NOTES.MIDDLE
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

