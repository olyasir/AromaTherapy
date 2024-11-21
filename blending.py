from enum import Enum
from oils.Citrus import Mandarin
from oils import Geranium
from oils import YlangYlang
from all_oils import get_all_oils
from random import shuffle
from properties import NOTES, AROMA_STRENGTH

class DELIVERY_METHODS(Enum):
    oil=1
    Gel=2
    Creams=3
    lotions=4
    Salve=5
    Salt_scrub=6
    Inhaler_diffusor=7
    Baths_Hydrotherapy=8

'''
.5% infants
¨ 1% or less: children, face creams
¨ 1.5%: subtle aromatherapy, elderly/frail
¨ 2.5%: standard holistic aromatherapy
¨ 5%: treatment work, localized massage, wound
healing
¨ 10%: treatment work, localized application
¨ >10% acute conditions
'''

from base_oil import Base
from properties import PROPERTY
def print_blend(blend: dict[Base:int]):
    for oil, drops in blend.items():
        print(f'oil {oil.name}: {drops}')
        print(f"properties: {oil.properties}")


def filter_oils(all_oils, oils_to_use =[], oils_not_to_use=[]):
    if not oils_to_use and not oils_not_to_use:
        return all_oils
    filtered = []
    for oil in all_oils:
        if oil.oil_type in oils_to_use and oil.oil_type not in oils_not_to_use:
            filtered.append(oil)
    return filtered


def get_all_oils_notes(my_oils):
    ret = ""
    all_oils = get_all_oils()
    all_oils = filter_oils(all_oils, my_oils)
    for oil in all_oils:
        note= str(oil.note).split(".")[-1].lower()
        ret += (oil.name + f": {note} ,")
    return ret

def get_oils_by_properties(properties, oils_to_use, oils_not_to_use):

    properties = set(properties)
    all_oils = get_all_oils()
    all_oils= filter_oils(all_oils, oils_to_use, oils_not_to_use)
    possible_oils = []
    for oil in all_oils:
        common_properties = set(oil.properties).intersection(properties)
        if len(common_properties) >0:
            possible_oils.append( (oil,  common_properties))

    shuffle(possible_oils)
    possible_oils = sorted(possible_oils, key= lambda x: len(x[1]), reverse=True)
    return possible_oils



DEFAULT_TOP = Mandarin.Mandarin()
DEFAULT_MIDDLE = Geranium.Geranium()
DEFAULT_BASE = YlangYlang.YlangYlang()

def best_trio_by_notes(oil_list):
    from properties import NOTES
    top = None
    middle = None
    base = None
    for oil, properties in oil_list:
        if not hasattr(oil, 'note'):
            continue
        curr_note = oil.note
        if curr_note == NOTES.BASE and base == None:
            base = (oil, properties)
        if curr_note == NOTES.MIDDLE and middle == None:
            middle = (oil, properties)
        if curr_note == NOTES.TOP and top == None:
            top = (oil, properties)
        if top and middle and base:
            return {NOTES.TOP: top, NOTES.MIDDLE:middle, NOTES.BASE:base}

    if top == None:
        print("Setting default top")
        top = (DEFAULT_TOP, set([]))
    if middle == None:
        print("Setting default middle")
        middle = (DEFAULT_MIDDLE, set([]))
    if base == None:
        print("Setting default base")
        base = (DEFAULT_BASE, set([]))
    return {NOTES.TOP: top, NOTES.MIDDLE: middle, NOTES.BASE: base}



def set_amounts(triple):

    import numpy as np
    top_oil = triple[NOTES.TOP]
    middle_oil = triple[NOTES.MIDDLE]
    base_oil = triple[NOTES.BASE]
    strength_points= {AROMA_STRENGTH.Strong:3, AROMA_STRENGTH.Medium_Strong:6, AROMA_STRENGTH.Medium:14}

    properties_bias = 2
    top_bias = 2
    middle_bias = 1.5

    proportions = [strength_points[top_oil[0]._aroma_strength]+len(top_oil[1])*properties_bias,
                   strength_points[middle_oil[0]._aroma_strength] + len(middle_oil[1])*properties_bias,
                   strength_points[base_oil[0]._aroma_strength]+ len(base_oil[1])*properties_bias]
    proportions = np.array([top_bias*proportions[0], middle_bias*proportions[1], proportions[2]])
    final_proportions = proportions/ np.sum(proportions)
    final_proportions =  final_proportions
    return { top_oil[0]:final_proportions[0],  middle_oil[0]:final_proportions[1],
             base_oil[0]: final_proportions[2]}


concentrations = {"body oil":(2.5, 100), "room_spray":(1,150), "frangnance_oil":(20,15), "salt_scrub" : (3, 50),
                  "body_butter":(1.6 ,200), "Eau de toilette": (4, 30),
                  "nabulating diffuser oil":(100, 2)}

#1 drop to 5 ml is 1%
ONE_PERCENT_DILUTION = 5 #ML

def drops(percent, carrier_amount):
    drops_amount = (carrier_amount/ONE_PERCENT_DILUTION)*percent
    return drops_amount

def get_all_concentrations(oils):
    oils_keys = list(oils.keys())
    for name, amounts in concentrations.items():
        percent, carrier = amounts
        total_drops = drops(percent, carrier)
        print(f"{name}: {oils_keys[0].name}: {round(total_drops*oils[oils_keys[0]])} drops,"
              f"{oils_keys[1].name}: {round(total_drops*oils[oils_keys[1]])} drops,"
              f"{oils_keys[2].name}: {round(total_drops*oils[oils_keys[2]])} drops",
              f"in {carrier} ML of carrier")
        print("=================================================================")

def do_blend(properties, oils_to_use = [], oils_not_to_use=[]):
    from oils.Citrus.Orange import Orange
    from oils.Citrus.Bergamot import Bergamot
    from oils.Black_Pepper import Black_Pepper
    from oils.Myrrh import Myrrh
    oil_list = get_oils_by_properties(properties, oils_to_use, oils_not_to_use)
    triple  = best_trio_by_notes(oil_list)

    triple = {NOTES.TOP: (Bergamot(),), NOTES.MIDDLE: (Black_Pepper(),), NOTES.BASE: (Myrrh(),) }

    blend_by_notes(triple)
    print(triple)
    # blend = set_amounts(triple)
    # get_all_concentrations(blend)
    # return blend


def blend_by_notes(triple):
    top = 0.3
    middle = 0.5
    bottom = 0.2
    blend  = get_all_concentrations({triple[NOTES.TOP][0]:top,
                            triple[NOTES.MIDDLE][0]: middle,
                           triple[NOTES.BASE][0]: bottom})
    return blend




def get_all_base_notes():
    from properties import NOTES
    all_oils = get_all_oils()
    ret = []
    for oil in all_oils:
        if oil.note ==  NOTES.BASE:
            ret.append(oil)
    return ret



if __name__ == '__main__':
    from olyas_oils import  my_oils, dennis_oils

    print(get_all_oils_notes(my_oils))

    # salt_blend = [PROPERTY.Healing, PROPERTY.comfort, PROPERTY.love, PROPERTY.NAURISH, PROPERTY.DROUND, PROPERTY.SUPPORT, PROPERTY.PROTECT,
    #               PROPERTY.PROVIDE, PROPERTY.Cleansing]
    #night_blend = [PROPERTY.RELAXING, PROPERTY.comfort, PROPERTY.SUPPORT, PROPERTY.SEDATIVE]
    morning_blend = [PROPERTY.ENERGY, PROPERTY.UPLIFTING,
                     PROPERTY.Possibility, PROPERTY.NAURISH, PROPERTY.Grouth, PROPERTY.Mood_Improvment,
                     PROPERTY.Light, PROPERTY.STRENGTH]

    concentration = [PROPERTY.Clear_Mind, PROPERTY.Brain_Function, PROPERTY.Learning, PROPERTY.Memory]

    #love = [PROPERTY.love, PROPERTY.beauty, PROPERTY.Aphrodisiac, PROPERTY.UPLIFTING, PROPERTY.ENERGY]
    morning_forest = [PROPERTY.UPLIFTING, PROPERTY.RELAXING, PROPERTY.ENERGY, PROPERTY.BALANCE, PROPERTY.CONTEMPLATION,
                      PROPERTY.GROUND, PROPERTY.STABILITY, PROPERTY.Grounding, PROPERTY.Breathing,
                      PROPERTY.beauty]
    dennis_blend = [PROPERTY.Breathing, PROPERTY.cough]
    oils = do_blend(dennis_blend, oils_to_use=my_oils)
    print("")



