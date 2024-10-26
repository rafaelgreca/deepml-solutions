import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    sum_exp = sum([math.exp(score) for score in scores])
    return [round(math.exp(score)/sum_exp, 4) for score in scores]
