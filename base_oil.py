from properties import PLANT_PART, PROPERTY, PART_TO_PROPERTY

class Base:

    def __init__(self, plant_part:PLANT_PART, name :str, properties:list[PROPERTY], aroma_strength:int ):
        self._plant_part = plant_part
        self._name = name
        self._properties = properties
        self._aroma_strength = aroma_strength
        self._properties += PART_TO_PROPERTY[self._plant_part]


