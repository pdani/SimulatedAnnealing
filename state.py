import copy
import scipy
import math

def dist(p1, p2):
    """Calculates the distance between two points (p1 and p2)"""
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

class State(object):
    """
    Represents a state of the annealing. The configuration contains the 
    coordinates of 16 points.
    """
    
    def __init__(self):
        """
        Generates initial state: randomize 16 points each with 2 coordinate
        Each coordinate is between 0 and 399
        """
        self.points = scipy.random.randint(0, 400, (16, 2))
        
    def genNeighbour(self):
        """
        Generates a neighbour: randomize an offset vector with offsets -1, 0 or
        1, and adds to the current state in a bounded way
        """
        
        # Clones itself
        neighbour = copy.deepcopy(self)
        # Randomized offset vector
        offset = scipy.random.randint(-1, 2, (16, 2))
        # Add the offset to the cloned state
        neighbour.points += offset
        
        # Bound-check (coordinates must be between 0 and 398)
        ps = neighbour.points
        for i in xrange(ps.shape[0]):
            for j in xrange(ps.shape[1]):
                if ps[i, j] < 0:
                    ps[i, j] = 1
                elif ps[i, j] > 399:
                    ps[i, j] = 398
        return neighbour
    
    def getEnergy(self):
        """
        Calculates the energy of the state: for every point calculates the
        distance from the closest point, and sums them together
        """
        
        energy = 0
        for p1 in xrange(self.points.shape[0]):
            # Find the closest point (its distance) for p1
            mindistance = 10000
            for p2 in xrange(self.points.shape[0]):
                # Skips the same point
                if p1 == p2:
                    continue
                distance = dist(self.points[p1], self.points[p2])
                if distance < mindistance:
                    mindistance = distance
            energy += mindistance
            
        return energy
    