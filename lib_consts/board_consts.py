from types import NoneType

from objects.plant import Plant
from objects.human import Human
from objects.predator import Predator
from objects.herbivore import Herbivore

CONST_DICT = {1: Plant, 2: Herbivore, 3: Predator, 4: Human}
PRINT_DICT = {Plant: "T", Herbivore: "H", Predator: "P", Human: "O", NoneType: "N"}
TYPE_CODING = {"T": Plant, "H": Herbivore, "P": Predator, "O": Human, "N": NoneType}
STR_TYPE_DICT = {1: "Plant", 2: "Herbivore", 3: "Predator", 4: "Human"}
TEST_FILE_NAME = "test_file.yml"
