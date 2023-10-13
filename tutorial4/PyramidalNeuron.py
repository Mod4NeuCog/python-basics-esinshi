import Lecture4.NeuronCell as NeuronCell


class PyramidalNeuron(NeuronCell):
    def __init__(self, dendrites, axon):
        super().__init__("Pyramidal Neuron", dendrites, axon)


pyramidal_cell = PyramidalNeuron(2, 1)
