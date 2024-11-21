from enum import Enum


class FRAGNANCE(Enum):
    CITRUS = 1
    FLORAL = 2
    HERBAL = 3
    SPICY = 4
    WOODY = 5


class PROPERTY(Enum):

    Antioxidant = 64
    cough = 63
    RELAXING = 2
    BLUE = 3
    ENERGY =4
    BALANCE = 5
    STRENGTH =6
    CORE =7
    INWARD_GAZING = 8
    CONTEMPLATION = 9
    SUPPORT =10
    GROUND =11
    PROVIDE = 12
    STABILITY =13
    NAURISH =14
    STRENGTHEN =15
    SEDATIVE =16
    Anti_inflammatory =17#: German chamomile
    UPLIFTING=18 #Citrus oils
    Wound_healing=19# Helichrysum
    Antimicrobial=20# Thyme
    Antifungal=21# Palmarosa
    Grounding=22# Vetiver
    Detoxing=23# Juniper / Grapefruit
    Cool =24
    Hot=25
    Heavy =26
    Light =27
    Grouth =28
    Reproduction =29
    Possibility =30
    Healing =31
    PROTECT =32
    SKINCARE =33
    SPIRITUAL_HEALING =34
    energetic_healing =35
    Breathing =36
    Breathing_space=36
    transformation=37
    immune_system=38
    love =39
    compassion=40
    forgiveness=41
    gifting=42
    beauty=43
    comfort=44
    Cleansing =45
    Antidepressant = 46
    Brain_Function = 47
    Aphrodisiac = 48
    Sleep = 49
    Mood_Improvment = 50
    Antiseptic = 51
    Antiviral =52
    Antibacterial = 53
    Digestion = 54
    Skin = 55
    Learning =56
    Anti_Pain = 57
    Memory = 58
    Clear_Mind = 59
    Hormone_Balance = 60
    Stress_Relief = 61
    Alergy = 62

class AROMA_STRENGTH(Enum):
    Medium = 1

    Medium_Strong = 2
    Strong = 3


class NOTES(Enum):
    TOP = 1
    MIDDLE = 2
    BASE = 3


class PLANT_PART(Enum):
    ROOT =1
    STEM =2
    FLOWER =3
    WOOD = 4
    LEAVE =5
    SEEDS =6
    RESIN=7
    PEEL=8


class Chemistry(Enum):
    Monoterpenes=1
    Sesquiterpenes=2
    Alcohols=3
    Aldehydes=4
    Ketones=5
    Phenols=6
    Oxides=7


class Component(Enum):
    Linalol=1
    A_bisabolol=2
    Linalyl=3
    acetate=4
    Citronellal=5
    Linalyl_acetate =6


component_to_property: {Component.Linalol:[PROPERTY.SEDATIVE, PROPERTY.RELAXING],
                        Component.Linalyl_acetate:[PROPERTY.SEDATIVE, PROPERTY.RELAXING]}



SEED_PROPERTIES = [PROPERTY.NAURISH, PROPERTY.Reproduction, PROPERTY.Possibility]
ROOT_PROPERTIES = [PROPERTY.Grounding, PROPERTY.NAURISH, PROPERTY.STRENGTHEN, PROPERTY.SUPPORT, PROPERTY.STABILITY, PROPERTY.BALANCE]

WOOD_PROPERTIES = [PROPERTY.BALANCE, PROPERTY.STRENGTHEN, PROPERTY.SUPPORT, PROPERTY.CONTEMPLATION, PROPERTY.ENERGY]


RESIN_PROPERTIES = [PROPERTY.Wound_healing, PROPERTY.Healing, PROPERTY.PROTECT,
                    PROPERTY.SKINCARE, PROPERTY.SPIRITUAL_HEALING, PROPERTY.energetic_healing]


LEAVES_PROPERTIES= [PROPERTY.Breathing, PROPERTY.Breathing_space, PROPERTY.transformation, PROPERTY.immune_system]


FLOWER_PROPERTIES= [PROPERTY.love, PROPERTY.compassion, PROPERTY.forgiveness, PROPERTY.gifting,
                    PROPERTY.beauty, PROPERTY.comfort]


PEEL_PROPERTIES = [PROPERTY.PROTECT, PROPERTY.ENERGY, PROPERTY.UPLIFTING, PROPERTY.Cleansing]
PART_TO_PROPERTY = {PLANT_PART.SEEDS: SEED_PROPERTIES,
                    PLANT_PART.ROOT: ROOT_PROPERTIES,
                    PLANT_PART.RESIN:RESIN_PROPERTIES,
                    PLANT_PART.LEAVE: LEAVES_PROPERTIES,
                    PLANT_PART.FLOWER : FLOWER_PROPERTIES,
                    PLANT_PART.WOOD: WOOD_PROPERTIES,
                    PLANT_PART.PEEL:PEEL_PROPERTIES}


class OILS(Enum):
    BERGAMOT =1
    GRAPEFRUIT =2
    LIME =3
    MANDARIN =4
    ORANGE =5
    TANGERINE=6
    ANGELICA =7
    BASIL=8
    BIRCH=9
    CARAWAY=10
    CARDAMON=11
    CARROT=12
    CEDAR=13
    CEDARWOOD=14
    CINNAMON_LEAF=15
    CLARY_SAGE=16
    CYPRESS=17
    DILL=18
    ELEMI=19
    EUCALYPTUS=20
    FENNEL=21
    FIR=22
    FRANKINCENSE=23
    GERANIUM=24
    GERMAN_CAMMOMILE=25
    GINGER=26
    HELICHRYSUM=27
    HEMLOCK=28
    JASMINE=29
    JATAMANSI=30
    JUNIPER=31
    LAUREL=32
    LAVANDER=33
    MARJORAM=34
    MYRHH=35
    NARD=36
    NEROLI=37
    PALMAROSA=38
    PATCHOULI=39
    PEPPERMINT=40
    PETITGRAIN=41
    PINE=42
    ROMAN_CAMOMILE=43
    ROSE=44
    ROSEMARY=45
    SANDALWOOD=46
    SPEARMINT=47
    TEA_TREE=49
    THYME=50
    VERIVER=51
    YLANG_YLANG=52
    LEMON =53
    MYRTLE =54
    LEMONGRASS = 55
    CLOVE_LEAF = 56
    BLACK_PEPPER = 57
    CITRONELA = 58
    LEMON_EUCALIPTUS =59


if __name__ == "__main__":
    for e in PROPERTY:
        print(f"{e.name.lower()}, ", end="")