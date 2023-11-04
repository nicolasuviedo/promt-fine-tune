from typing import TypeVar, Callable, ClassVar, Dict
from dataclasses import dataclass, field


@dataclass
class Example:
    """
    Represents an example of a prompt's input and output.
    Each Example is a pair of strings, one representing the input and the other the output.
    The format method is used to display the example in a human-readable format.
    input: str
    output: str
    format:ClassVar[Callable] = lambda i,o: f"{i} -> {o}"
    """

    input: str
    output: str
    format: ClassVar[Callable] = lambda i, o: f"{i} -> {o}"

    def __post_init__(self):
        assert (
            isinstance(self.input, str) and self.input.strip()
        ), "input must be a non-empty string"
        assert (
            isinstance(self.output, str) and self.output.strip()
        ), "output must be a non-empty string"
        assert callable(self.format), "format must be a callable function"

    def __str__(self):
        return self.format(self.input, self.output)


@dataclass
class Prompt:
    """
    Represents an individual in the population.
    Each Prompt is a string that represents a potential solution.

    Depending on the problem, the string could encode various types of data.
    For example, it could encode binary data, a sequence of parameters, etc.
    The encoding and decoding methods (if necessary) are problem-dependent.
    """

    prompt: str
    _params: Dict[str, Union[str, List[Example]]] = field(default_factory=dict)

    def __post_init__(self):
        self._params = {"instructions": "", "examples": [], "format": ""}

        # Type checking
        assert isinstance(
            self._params["instructions"], str
        ), "instructions must be a string"
        assert all(
            isinstance(example, Example) for example in self._params["examples"]
        ), "examples must be a list of Example objects"
        assert isinstance(self._params["format"], str), "format must be a string"

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
