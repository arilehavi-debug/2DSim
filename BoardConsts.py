from Plant import Plant
from Human import Human
from Predator import Predator
from Herbivore import Herbivore
from types import NoneType

class BoardConsts:
    CONST_DICT = {1: Plant, 2: Herbivore, 3: Predator, 4: Human}
    PRINT_DICT = {Plant: "T", Herbivore: "H", Predator: "P", Human: "O", NoneType: "N"}
    STR_TYPE_DICT = {1: "Plant", 2: "Herbivore", 3: "Predator", 4: "Human"}
    TOTAL_ROWS = 5
    TOTAL_COLS = 5