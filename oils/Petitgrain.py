from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Petitgrain(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = None
    name = "Petitgrain"
    fragnance = FRAGNANCE.FLORAL
    oil_type = OILS.PETITGRAIN
    properties = [PROPERTY.SEDATIVE, PROPERTY.RELAXING]
    note = NOTES.MIDDLE
    def __init__(self):
        super().__init__( Petitgrain.part, Petitgrain.name, Petitgrain.properties, Petitgrain.aroma_strength)

