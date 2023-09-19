"""
Esin Bahar Akcay
19 September 2023

Exercise 4: code of 2 IO neurons using a method

"""

import sys


def main():
    # Initialize the membrane potential
    V_membrane = float(-75)

    # Ask the user to input a spike value
    spike_value = float(sys.argv[1])

    # Update the membrane potential
    V_membrane += spike_value


if __name__ == "__main__":
    main()
