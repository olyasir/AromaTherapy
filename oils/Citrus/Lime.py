from properties import NOTES, PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class Lime(Base):
    part = PLANT_PART.PEEL
    aroma_strength = None
    name = "Lime"
    oil_type = OILS.LIME
    note = NOTES.TOP
    fragnance = FRAGNANCE.CITRUS
    properties = [PROPERTY.UPLIFTING, PROPERTY.Light]

    def __init__(self):
        super().__init__(self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

