# Implement NeuronalNetwork composition example running
# a loop to execute neuron potential computation transitions
class NeuronalNetwork:
    def __init__(self, neurons):
        self.neurons = neurons
        self.network_size = len(neurons)
        self.outputSpikeList = [0 for i in range(self.network_size)]

    def updateNetwork(self, inputSpikeList):
        # Iterate over each neuron in the network
        for i in range(self.network_size):
            neuron = self.neurons[i]  # Update ith neuron
            neuron.update_MembranePotential(inputSpikeList[i])  # Compute potential for each neuron
            self.outputSpikeList[i] = neuron.output()

        return self.outputSpikeList


# Define the BrainRegion class representing a region of the brain
class BrainRegion:
    def __init__(self, name, network):
        self.name = name
        self.network = network

    def update(self, inputSpikeList):
        output = self.network.updateNetwork(inputSpikeList)
        return output
