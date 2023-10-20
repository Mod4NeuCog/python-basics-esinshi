# Define the NeuronalCell, PyramidalNeuron, and OvoidNeuron classes (as shown in the previous response)

# Create instances of PyramidalNeuron and OvoidNeuron
pyramidal_cell = PyramidalNeuron("Pyramidal Neuron 1", "Cerebral Cortex", 100, 150)
ovoid_cell = OvoidNeuron("Ovoid Neuron 1", "Spinal Cord", "Ovoid", 120)

# Simulate an interaction between the neurons
def simulate_interaction(sender, receiver):
    # Imagine that the pyramidal neuron sends an electrical signal to the ovoid neuron
    signal = "Electrical Signal"
    print(f"{sender.name} sends an {signal} to {receiver.name} in the {sender.location}.")
    print(f"{receiver.name} receives the signal in the {receiver.location} and responds.")

# Perform the interaction
simulate_interaction(pyramidal_cell, ovoid_cell)
