# Exercise 4: Dopamine stock share
from Exam_II.DopamineCell import DopamineCell
from Exam_II.NeuronalNetwork import NeuronalNetwork

neuron_1 = DopamineCell(1, 1)
neuron_2 = DopamineCell(1, 1)
neuron_3 = DopamineCell(1, 1)

neuronal_network1 = NeuronalNetwork([neuron_1, neuron_2, neuron_3])
neuronal_network1.updateNetwork([10, 10, 10])
