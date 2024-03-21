import umbridge
import numpy as np

class Rosenbrock(umbridge.Model):
    """
    A class representing the 2D Rosenbrock function.

    Attributes:
        radius (float): The radius of the banana.
        sigma2 (float): The variance of the banana.

    Methods:
        __init__(self): Initializes the Rosenbrock class.
        get_input_sizes(self, config): Returns the input sizes.
        get_output_sizes(self, config): Returns the output sizes.
        __call__(self, parameters, config): Evaluates the Rosenbrock function.
        supports_evaluate(self): Checks if the class supports evaluation.
    """

    def __init__(self):
        super().__init__("posterior")

    def get_input_sizes(self, config):
        return [2]

    def get_output_sizes(self, config):
        return [1]

    def __call__(self, parameters, config):
        x = parameters[0][0]
        y = parameters[0][1]

        rosenbrock = (1 - x)**2 + 100 * (y - x**2)**2

        return [[-rosenbrock]]

    def supports_evaluate(self):
        return True

if __name__ == "__main__":
    model = Rosenbrock()
    umbridge.serve_models([model], 4243)
