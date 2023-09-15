"""
Esin Bahar Akcay
15 September 2023
"""

import sys


def main():
    # Initialize the membrane potential
    V_membrane = float(-75)

    # Ask the user to input a spike value
    spike_value = float(sys.argv[1])
    # Update the membrane potential
    V_membrane += spike_value

    if V_membrane >= -65:
        print("5")
        membrane_potential = 0  # Reset the membrane potential
    else:
        print("0")


if __name__ == "__main__":
    main()
