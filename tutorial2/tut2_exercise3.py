"""
Esin Bahar Akcay
29 September 2023
"""

# Exercise 3: change the while loop in simulator into a for loop

V_threshold = -65
V_membrane = -75
V_rest = -75


def update_V_membrane(spike_value, V_membrane):
    V_membrane += spike_value
    return V_membrane


def check_threshold(V_mem):
    if V_mem >= V_threshold:
        global V_membrane
        V_membrane = V_rest
        return 5
    else:
        return 0


def simulator(spike_list, t_end, c):
    # time point
    t = 0
    # index of spike list
    n = 0

    global V_membrane

    # For Loop to the simulator part
    for n in range(int(t_end/c)+1):
        output_neuron = check_threshold(V_membrane)

        V_membrane = update_V_membrane(spike_list[n], V_membrane)

        print("t=", t, V_membrane, output_neuron)

        # Fraction the time with the given gap constant
        n = n + 1
        t = n * c

    return V_membrane


def main():
    inputSpikeList = [0,5,5,0,0,0,0,5]
    t_end = 3.5
    c = 0.5

    simulator(inputSpikeList, t_end, c)

if __name__ == "__main__":
    main()
