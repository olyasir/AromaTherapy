from properties import PROPERTY, NOTES, PLANT_PART, OILS,  FRAGNANCE
from base_oil import Base

class Birch(Base):
    part = PLANT_PART.WOOD
    aroma_strength = 1
    name = "Birch"
    fragnance = FRAGNANCE.WOODY
    oil_type = OILS.BIRCH
    properties = [PROPERTY.Antidepressant,
                  PROPERTY.Detoxing,
                  PROPERTY.Antidepressant]
    note = NOTES.TOP

    def __init__(self):
        super().__init__( Birch.part, Birch.name, Birch.properties, Birch.aroma_strength)

