import random
import math

from state import State

class Annealing(object):
    """Class for the annealing algorithm"""
    
    def __init__(self, factor=20000):
        """
        Initializes random seed, state, and energy. Factor is controls the
        speed of annealing: lower values results faster, but imprecise results.
        """
        random.seed()
        self.state = State()
        self.iteration = 0
        self.energy = self.state.getEnergy()
        self.factor = factor

    def temperature(self):
        """
        Calculates the current temperature based on the current iteration count.
        """
        
        return 1.0 - math.tanh(float(self.iteration) / self.factor)
    
    def probability(self, neighbourEnergy):
        """
        Defines the probability of movement from the current state to a
        neighbour state. If the neighbour state is "better" (higher energy), 
        definitely moves to it. Otherwise, probability depends on the current
        temperature
        """
        
        if neighbourEnergy > self.energy:
            return 1.0
        return self.temperature()
    
    def iterate(self):
        """
        Called from outside periodically. Expands a neighbour state, calculates
        its energy, and decides whether move there or not.
        """
        
        neighbour = self.state.genNeighbour()
        energy = neighbour.getEnergy()
        if self.probability(energy) > random.random():
            self.state = neighbour
            self.energy = energy
            
        # Increasing iteration counter
        self.iteration += 1
        