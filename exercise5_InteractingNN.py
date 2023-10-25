# Create instances of neurons
from Exam_II.NeuronalNetwork import NeuronalNetwork, BrainRegion
from Exam_II.Neurons import NeuronalCell, PyramidalNeuron, OvoidNeuron

neuron_1 = NeuronalCell("Generic Neuron 1", 1, 1)
neuron_2 = PyramidalNeuron(2, 1)
neuron_3 = OvoidNeuron(2, 1)

# Create an instance of the neuronal network
neuronal_network1 = NeuronalNetwork([neuron_1, neuron_2, neuron_3])

# Create a cortex region
cortex = BrainRegion("Cortex",neuronal_network1)
outputCortex = cortex.update([5,10,5])
print(outputCortex)

# Create a hippocampus region
neuron_4 = NeuronalCell("Generic Neuron 1", 1, 1)
neuron_5 = PyramidalNeuron(1, 1)
neuron_6 = OvoidNeuron(1, 1)
neuronal_network2 = NeuronalNetwork([neuron_4, neuron_5,neuron_6])

hippocampus = BrainRegion("Cortex",neuronal_network2)
output_hippocampus = hippocampus.update(outputCortex)
print(output_hippocampus)