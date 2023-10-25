# Exercise 1: Make classes corresponding to NeuronalCell, PyramidalNeuron and OvoidNeuron
class NeuronalCell:
    def __init__(self, cell_type: str, dendrite_count: int, axon_length: int):
        self.cell_type = cell_type
        self.dendrites = dendrite_count
        self.axon = axon_length
        self.membranePotential = -75

    def update_MembranePotential(self, inputSpike):
        self.membranePotential = self.membranePotential + inputSpike
        return self.membranePotential

    def output(self):
        # If membrane potential reaches -65mv, emit a spike
        if self.membranePotential >= -65:
            self.membranePotential = -75
            return 5
        else:
            return 0


class PyramidalNeuron(NeuronalCell):
    def __init__(self, dendrites, axon):
        super().__init__("Pyramidal Neuron", dendrites, axon)


class OvoidNeuron(NeuronalCell):
    def __init__(self, dendrites, axon):
        super().__init__("Ovoid Neuron", dendrites, axon)


