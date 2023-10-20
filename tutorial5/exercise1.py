# Define a base class NeuronalCell
class NeuronalCell:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def describe(self):
        return f"Name: {self.name}, Location: {self.location}"


# Define a subclass PyramidalNeuron, inheriting from NeuronalCell
class PyramidalNeuron(NeuronalCell):
    def __init__(self, name, location, dendrite_count, axon_length):
        super().__init__(name, location)
        self.dendrite_count = dendrite_count
        self.axon_length = axon_length

    def describe(self):
        base_description = super().describe()
        return f"{base_description}, Dendrite Count: {self.dendrite_count}, Axon Length: {self.axon_length}"


# Define another subclass OvoidNeuron, also inheriting from NeuronalCell
class OvoidNeuron(NeuronalCell):
    def __init__(self, name, location, shape, size):
        super().__init__(name, location)
        self.shape = shape
        self.size = size

    def describe(self):
        base_description = super().describe()
        return f"{base_description}, Shape: {self.shape}, Size: {self.size}"


# Creating instances of PyramidalNeuron and OvoidNeuron
pyramidal_cell = PyramidalNeuron("Pyramidal Neuron 1", "Cerebral Cortex", 100, 150)
ovoid_cell = OvoidNeuron("Ovoid Neuron 1", "Spinal Cord", "Ovoid", 120)

# Testing the describe method for both cell types
print("Pyramidal Neuron:")
print(pyramidal_cell.describe())

print("\nOvoid Neuron:")
print(ovoid_cell.describe())
