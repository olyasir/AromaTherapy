from properties import NOTES,PLANT_PART, PROPERTY, OILS, FRAGNANCE
from base_oil import Base

class GermanCamomile(Base):
    part = PLANT_PART.FLOWER
    aroma_strength = None
    name = "German Chamomile"
    oil_type = OILS.GERMAN_CAMMOMILE
    properties = [PROPERTY.Anti_inflammatory, PROPERTY.Cool]
    fragnance = FRAGNANCE.HERBAL
    note = NOTES.MIDDLE
    def __init__(self):
        super().__init__(self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

