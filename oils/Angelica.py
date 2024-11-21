from properties import NOTES, PLANT_PART, OILS, FRAGNANCE
from base_oil import Base
from properties import PROPERTY
class Angelica(Base):
    part = PLANT_PART.ROOT
    aroma_strength =1
    name = "Angelica"
    oil_type = OILS.ANGELICA
    fragnance = FRAGNANCE.HERBAL
    properties = [PROPERTY.Digestion, PROPERTY.Breathing, PROPERTY.immune_system, PROPERTY.Detoxing]
    note = NOTES.MIDDLE


    def __init__(self):
        super().__init__(Angelica.part, Angelica.name, Angelica.properties, Angelica.aroma_strength)
        
