from dataclass import dataclass

@dataclass
class Prompt:

    value: str
    age: int
    """
    Represents an individual in the population.
    Each Prompt is a string that represents a potential solution.

    Depending on the problem, the string could encode various types of data.
    For example, it could encode binary data, a sequence of parameters, etc.
    The encoding and decoding methods (if necessary) are problem-dependent.
    """

    def fitness(self):
        """
        Calculate the fitness of the Prompt.

        The fitness function is problem-dependent and must be defined.
        It could be as simple as a direct evaluation or as complex as a simulation.
        """
        pass

    def mutate(self, mutation_rate):
        """
        Apply mutation to the Prompt.

        The implementation of mutation could involve flipping bits, changing characters,
        or any other problem-specific mutation operation.
        """
        pass

    @staticmethod
    def crossover(parent1, parent2):
        """
        Perform crossover between two parents to produce offspring.

        This method could be implemented in various ways, such as single-point crossover,
        multi-point crossover, or uniform crossover for bit strings.
        For string-based representations, crossover methods could involve splicing
        the strings at certain points or interweaving their characters.
        """
        pass