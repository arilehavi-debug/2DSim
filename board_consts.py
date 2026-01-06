"""
this module contains all constants for the game board's usage
"""
from types import NoneType
from plant import Plant
from human import Human
from predator import Predator
from herbivore import Herbivore

CONST_DICT = {1: Plant, 2: Herbivore, 3: Predator, 4: Human}
PRINT_DICT = {Plant: "T", Herbivore: "H", Predator: "P", Human: "O", NoneType: "N"}
TYPE_CODING = {"T": Plant, "H": Herbivore, "P": Predator, "O": Human, "N": NoneType}
STR_TYPE_DICT = {1: "Plant", 2: "Herbivore", 3: "Predator", 4: "Human"}
