#
# Author: Alvin Thai
# Description: 
#     The code programs a robot with adjustable rocket launcher, torso, and leg heights.  Values are input into the first function, returned, and then used in the second function through multiple paramaters.
#
def read_robot_inputs():
    rocket_height = int(input("Enter rocket-launcher height: "))
    torso_height = int(input("Enter torso height: "))
    leg_height = int(input("Enter leg length: "))
    return (rocket_height, torso_height, leg_height)
# The return function stores input values to be used in another function.

def print_robot(rocket_height, torso_height, leg_height):
    rocket = ("    |oooo|        |oooo|")
    torso = (" <_>      |------|      <_>")
    leg = ("     || ||        || ||")
    print("     ____          ____")
    while rocket_height > 0: 
        print(rocket)
        rocket_height -= 1
    print("    |    | .----. |    |")
    print("    |    |/\\_||_/\\|    |")
    print("    `----' / __ \\ `----'")
    print("   __/ |#|/\\/__\\/\\|#| \\__")
    print("  / \\_/|_|| |/\\| ||_|\\_/ \\")
    print(" |_\\/    o\\=----=/o    \\/_|")
    while torso_height > 0:
        print(torso)
        torso_height -= 1
    print(" | |   ___|======|___   | |")
    print("//\\\\  / |O|======|O| \\  //\\\\")
    print("|\\/|  \\_+/        \\+_/  |\\/|")
    print("\\__/  _|||        |||_  \\__/")
    while leg_height > 0:
        print(leg)
        leg_height -= 1
    print("   __|\\_/|__    __|\\_/|__")
    print("  /___n_n___\\  /___n_n___\\")
# While loops allow the function to print extensions to the rocket launchers, torso, and legs.  The heights decrease by 1 every time a line is printed until it reaches 0.

def main():
    rocket_height, torso_height, leg_height = read_robot_inputs()
    print()
    print_robot(rocket_height, torso_height, leg_height)
main()
# Assigning rocket_height, torso_height, leg_height as a varaible allows it to be defined for the following print_robot function.