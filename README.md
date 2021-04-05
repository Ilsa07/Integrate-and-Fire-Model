# Integrate and Fire Neuron Model

This project illustrates the basic integrate and fire neuron model, which is given by the equation:

![neuron model](https://latex.codecogs.com/gif.latex?%5Ctau_v%20%5Cfrac%7Bdv%7D%7Bdt%7D%20%3D%20-v%20&plus;%20RI)

In this simplified model the neuron spikes if the voltage reaches a threshold and then resets to the resting potential. This model illustrates the of the idea of neurons spiking and resetting in a regular fashion and does not involve adoption or plasticity. The above equation for the integrate and fire model can be rewritten with the Euler Method and solved iteratively with the equation below, which is used by the algorithm.

![iterative solution](https://latex.codecogs.com/gif.latex?v%28t&plus;1%29%3Dv%28t%29&plus;%20%5Cfrac%7B%5CDelta%20t%7D%7B%5Ctau_v%7D%28-v%28t%29&plus;RI%28t%29%29)

## Getting Started
1. Clone the project and create a virtual environment
2. Install the required packages in the virtual environment
   ```
   pip3 install -r requirements.txt
   ```
