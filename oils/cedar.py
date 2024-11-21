from properties import PROPERTY, NOTES, PLANT_PART, OILS, FRAGNANCE
from base_oil import Base

class Cedar(Base):
    part = PLANT_PART.WOOD
    aroma_strength = 1
    name = "Cedar"
    oil_type = OILS.CEDAR
    fragnance = FRAGNANCE.WOODY
    properties = [PROPERTY.Anti_inflammatory, PROPERTY.RELAXING, PROPERTY.Detoxing, PROPERTY.SEDATIVE, PROPERTY.Antifungal]
    note = NOTES.BASE

    def __init__(self):
        super().__init__( Cedar.part, Cedar.name, Cedar.properties, Cedar.aroma_strength)

