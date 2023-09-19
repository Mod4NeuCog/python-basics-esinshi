"""
Esin Bahar Akcay
19 September 2023

Exercise 6: code of 1 IO neuron separating model and simulator

"""
# Type on command line  py exercise6.py Method2 -75 8 90 as an example

import sys


def Method1(V_membrane, spike):
    V_membrane += spike
    return V_membrane


def Method2(V_membrane, spike, weight):
    V_membrane += spike * weight
    return V_membrane


def Simulate(method):

    V_membrane = float(sys.argv[2])
    spike_value = float(sys.argv[3])

    if method == 'Method1':
        V_membrane = Method1(V_membrane, spike=spike_value)
    elif method == 'Method2':
        synaptic_weight = float(sys.argv[4])
        V_membrane = Method2(V_membrane, spike=spike_value, weight=synaptic_weight)

    print(V_membrane)


def main():
    method_type = sys.argv[1]
    Simulate(method_type)


if __name__ == "__main__":
    main()
