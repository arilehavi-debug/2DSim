# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from code_from_previous_branches import gol_basic_simulation
import yaml
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # game_configuartion = gol_basic_simulation.load_starting_configuration("tests/beacon.txt")
    # total_iterations = int(input("Please enter valid iterations number: "))
    #
    # for current_iteration in range(total_iterations + 1):
    #     # print current state of screen
    #     gol_basic_simulation.print_simulation(game_configuartion, current_iteration)
    #     # update table
    #     game_configuartion = gol_basic_simulation.update_iteration(game_configuartion)
    #     # iterate forward
    #     current_iteration += 1
    # code for loading the info
    data = {""

        }

    with open('new_config.yaml', 'w') as file:
        yaml.dump(data, file, sort_keys=False)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
