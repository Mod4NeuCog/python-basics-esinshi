import Lecture4.NeuronCell as NeuronCell


class OvoidNeuron(NeuronCell):
    def __init__(self, dendrites, axon):
        super().__init__("Ovoid Neuron", dendrites, axon)


ovoid_cell = OvoidNeuron(2, 1)
