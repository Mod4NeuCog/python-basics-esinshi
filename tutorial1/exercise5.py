"""
Esin Bahar Akcay
19 September 2023

Exercise 5: code of 1 IO neuron with a parameter

"""

import sys


def main():
    # Initialize the membrane potential
    V_membrane = float(-75)

    # Take as input from command line 2 parameter values: spike and weight
    spike_value = float(sys.argv[1])
    synaptic_weight = float(sys.argv[2])

    # Update the membrane potential with a new method to calculate
    V_membrane += spike_value * synaptic_weight

    print(V_membrane)


if __name__ == "__main__":
    main()
