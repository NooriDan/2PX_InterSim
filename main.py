from InterSim import Simulation

def main():
    sim = Simulation(1000)
    sim.run()
    #sim.output_times()
    sim.output_to_CSV("trialFromMain")
    

main()
