import math

def sigmoid(z: float) -> float:
    #Your code here
	return round(1 / (1 + math.exp(-1 * z)), 4)
