"""
Esin Bahar Akcay
06 October 2023
"""

# Exercise 4: Implement Euler method to discretize the V_membrane differential eqn

V_threshold = -65
V_membrane = -75
V_rest = -75
R_m = 5
tau_m = 0.5


def delta(input, V_mem, dt):
    V_mem = V_mem + dt * (V_rest - V_mem + (R_m * input)) / tau_m
    return (V_mem)


def lambda_dtss(V_mem):
    if (V_mem >= V_threshold):
        global V_membrane
        V_membrane = V_rest
        return (5)
    else:
        return (0)


## Define a function to simulate neuron behaviour
def simulate(inputSpikeList, t_end, c):
    t = 0
    n = 0
    global V_membrane
    for n in range(int(t_end / c)):
        output_neuron = lambda_dtss(V_membrane)
        V_membrane = delta(inputSpikeList[n], V_membrane, c)
        # print("V_membrane=",V_membrane)
        print("t=", t, V_membrane, output_neuron)
        n = n + 1
        t = n * c
        # print("n=",n,"t=",t)
    return (V_membrane)


def main():
    inputSpikeList = [0, 5, 5, 0, 0, 0, 0, 5]
    t_end = 3.5
    c = 0.5
    simulate(inputSpikeList, t_end, c)


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()