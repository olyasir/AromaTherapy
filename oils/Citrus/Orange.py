from properties import NOTES, PLANT_PART, PROPERTY, OILS, AROMA_STRENGTH, FRAGNANCE
from base_oil import Base

class Orange(Base):
    part = PLANT_PART.PEEL
    aroma_strength = AROMA_STRENGTH.Medium
    name = "Orange"
    oil_type = OILS.ORANGE
    note = NOTES.TOP
    fragnance = FRAGNANCE.CITRUS
    properties = [PROPERTY.UPLIFTING, PROPERTY.Light, PROPERTY.Sleep, PROPERTY.Anti_Pain, PROPERTY.Skin,
                  PROPERTY.Digestion, PROPERTY.Stress_Relief, PROPERTY.Anti_inflammatory]

    def __init__(self):
        super().__init__(self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

