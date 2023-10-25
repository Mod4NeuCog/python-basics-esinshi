
class DopamineCell:
    # Define dopamine stock common for all dopamine neurons
    dopamine = 10

    def __init__(self, dendrites, axon):
        self.cell_type = "Dopamine"
        self.dendrites = dendrites
        self.axon = axon
        self.membranePotential = -75

    def update_MembranePotential(self, inputSpikes):
        self.membranePotential = self.membranePotential + inputSpikes
        print(self.membranePotential)

    def output(self):
        # If membrane potential reaches -65mv and dopamine stocks greater than 3, neuron fires.
        print("Dopamine stock remaining is", DopamineCell.dopamine)
        if (self.membranePotential >= -65) & (DopamineCell.dopamine > 3):
            self.membranePotential = -75
            DopamineCell.dopamine = DopamineCell.dopamine - 3  # Reduce dopamine stock by 3 everytime a neuron fires
            return 5
        else:
            return 0
