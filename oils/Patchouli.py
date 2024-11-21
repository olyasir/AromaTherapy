from properties import NOTES, PLANT_PART, PROPERTY, OILS, AROMA_STRENGTH, FRAGNANCE
from base_oil import Base


class Patchouli(Base):
    part = PLANT_PART.LEAVE
    aroma_strength = AROMA_STRENGTH.Medium #?
    name = "Patchouli"
    fragnance = FRAGNANCE.HERBAL
    oil_type = OILS.PATCHOULI
    note = NOTES.BASE
    properties = [PROPERTY.Antidepressant, PROPERTY.RELAXING, PROPERTY.Wound_healing,
                  PROPERTY.Brain_Function, PROPERTY.Aphrodisiac, PROPERTY.Antifungal, PROPERTY.Sleep,
                  PROPERTY.Mood_Improvment, PROPERTY.Antiseptic]
    def __init__(self):
        super().__init__( self.__class__.part, self.__class__.name, self.__class__.properties, self.__class__.aroma_strength)

