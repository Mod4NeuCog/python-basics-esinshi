from Exam_II.NeuronalNetwork import NeuronalNetwork
from Exam_II.Neurons import NeuronalCell, PyramidalNeuron, OvoidNeuron

# Exercise 2: Instantiate neurons and make them interact.
neuron_1 = NeuronalCell("Generic Neuron", 1, 1)
neuron_2 = PyramidalNeuron(2, 1)
neuron_3 = OvoidNeuron(2, 1)

# Generic neuron receives input = 10 mV
neuron_1.update_MembranePotential(10)
output_spike = neuron_1.output()
print(output_spike)

# Pass the output_spike of neuronal_cell to pyramidal_neuron
neuron_2.update_MembranePotential(output_spike)
print(neuron_2.output())

# Create an instance of the neuronal network
neuronal_network1 = NeuronalNetwork([neuron_1, neuron_2, neuron_3])

# Create a cortex region
cortex = BrainRegion("Cortex", neuronal_network1)
outputCortex = cortex.update([5, 10, 5])
print(outputCortex)


