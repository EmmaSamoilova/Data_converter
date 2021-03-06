from enum import Enum, unique


@unique
class ScoringRuleEnum(Enum):
    PEP01 = 'PEP01'
    PEP02 = 'PEP02'
    PEP03_home = 'PEP03_home'
    PEP03_land = 'PEP03_land'
    PEP03_car = 'PEP03_car'
    PEP04_adr = 'PEP04_adr'
    PEP04_reg = 'PEP04_reg'
    PEP05 = 'PEP05'
    PEP07 = 'PEP07'
    PEP09 = 'PEP09'
    PEP10 = 'PEP10'
    PEP11 = 'PEP11'
    PEP13 = 'PEP13'
    PEP15 = 'PEP15'
    PEP16 = 'PEP16'
    PEP17 = 'PEP17'
    PEP18 = 'PEP18'
    PEP19 = 'PEP19'
    PEP20 = 'PEP20'
    PEP21 = 'PEP21'
    PEP22 = 'PEP22'
    PEP23 = 'PEP23'
    PEP24 = 'PEP24'
    PEP25 = 'PEP25'
    PEP26 = 'PEP26'
    PEP27 = 'PEP27'


ALL_RULES = {}


def register_rule(class_):
    ALL_RULES[class_.rule_id.value] = class_
    return class_
