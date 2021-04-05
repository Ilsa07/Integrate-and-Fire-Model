import matplotlib.pyplot as plt


def integrate_and_fire_model(external_current:float, simulation_length:float) -> type(None):
    # Neuron Parameters
    spiking_threshold = 10
    time_constant = 10
    conductance = 1

    # Simulation Parameters
    dt = 1

    membrane_potential = [0]
    for t in range(0, simulation_length, dt):
        # Euler Method to obtain Neuron Voltage
        v = membrane_potential[-1] + (dt/time_constant)*(-membrane_potential[-1] + conductance*external_current)

        # Reset the voltage to 0 if it reached the spiking thrshold
        # simulating the firing of the neuron
        if(v>spiking_threshold):
            v = 0
        
        # Add the voltage to the array containing the membrane potentials over time
        membrane_potential.append(v)
    
    return membrane_potential

# Run the simulatoin and plot the results
voltage = integrate_and_fire_model(15, 100)
plt.plot(voltage)
plt.show()