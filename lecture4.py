class NeuronCell:
    def __init__(self, cell_type, dendrites, axon):
        self.cell_type = cell_type
        self.dendrites = dendrites
        self.axon = axon
        self.membranePotential = -75

    def UpdateMemPotential(self, inputSpikes):
        self.membranePotential = self.membranePotential + inputSpikes
        return self.membranePotential

    def output(self):
        if self.membranePotential >= -65:
            self.membranePotential = -75
            return 5
        else:
            return 0


class PyramidalNeuron(NeuronCell):
    def __init__(self, dendrites, axon):
        super().__init__("Pyramidal Neuron", dendrites, axon)


class OvoidNeuron(NeuronCell):
    def __init__(self, dendrites, axon):
        super().__init__("Ovoid Neuron", dendrites, axon)


neuronal_cell = NeuronCell("Generic Neuron", 1, 1)
pyramidal_cell = NeuronCell("Neuronal Cell", 1, 2)
ovoid_cell = NeuronCell("Ovoid Cell", 1, 2)
