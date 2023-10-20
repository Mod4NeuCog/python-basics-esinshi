import random

# Define the NeuronalCell, PyramidalNeuron, and OvoidNeuron classes (as shown in the previous response)

class NeuronalNetwork:
    def __init__(self):
        self.neurons = []

    def add_neuron(self, neuron):
        self.neurons.append(neuron)

    def simulate_transition(self, iterations):
        for iteration in range(iterations):
            print(f"Iteration {iteration + 1}:")
            for neuron in self.neurons:
                # Simulate potential computation (simplified as random potential)
                potential = random.uniform(0, 1)
                print(f"{neuron.name} in the {neuron.location} has potential: {potential:.2f}")
                # You can add more complex computation here

# Create a NeuronalNetwork
network = NeuronalNetwork()

# Create instances of PyramidalNeuron and OvoidNeuron and add them to the network
pyramidal_cell = PyramidalNeuron("Pyramidal Neuron 1", "Cerebral Cortex", 100, 150)
ovoid_cell = OvoidNeuron("Ovoid Neuron 1", "Spinal Cord", "Ovoid", 120)

network.add_neuron(pyramidal_cell)
network.add_neuron(ovoid_cell)

# Simulate transitions in neuron potential computation over multiple iterations
network.simulate_transition(iterations=5)
