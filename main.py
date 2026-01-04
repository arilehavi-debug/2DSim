"""
this module is the main function to run the gol and present it to screen
it uses functions from gol_basic_simulation.py
"""
import gol_basic_simulation

if __name__ == '__main__':
    game_configuartion = gol_basic_simulation.load_starting_configuration("tests/cloverleaf.txt")
    total_iterations = int(input("Please enter valid iterations number: "))

    for current_iteration in range(total_iterations + 1):
        gol_basic_simulation.print_simulation(game_configuartion, current_iteration)
        game_configuartion = gol_basic_simulation.update_iteration(game_configuartion)
        current_iteration += 1
