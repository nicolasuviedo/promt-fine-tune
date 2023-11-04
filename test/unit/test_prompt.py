from src.prompt import Example, Prompt
import pytest


def test_post_init_valid():
    # Test that a valid Example instance does not raise an assertion error
    example = Example(input="Test input", output="Test output")
    assert isinstance(example, Example)


def test_post_init_empty_input():
    # Test that an Example with an empty input string raises an assertion error
    with pytest.raises(AssertionError):
        Example(input="", output="Test output")


def test_post_init_empty_output():
    # Test that an Example with an empty output string raises an assertion error
    with pytest.raises(AssertionError):
        Example(input="Test input", output="")


def test_str_method():
    # Test the __str__ method returns the correct format
    example = Example(input="Test input", output="Test output")
    assert str(example) == "Test input -> Test output"


def test_post_init_default_params():
    # Test that a Prompt with default parameters has the correct initial state
    prompt = Prompt(prompt="Test prompt")
    assert prompt._params["instructions"] == ""
    assert prompt._params["examples"] == []
    assert prompt._params["format"] == ""


def test_post_init_invalid_params():
    # Test that invalid parameters for Prompt raise assertion errors
    with pytest.raises(AssertionError):
        Prompt(
            prompt="Test prompt",
            _params={"instructions": 123, "examples": "not a list", "format": 456},
        )


def test_fitness_not_implemented():
    # Test that the fitness method is not implemented
    prompt = Prompt(prompt="Test prompt")
    with pytest.raises(NotImplementedError):
        prompt.fitness()


def test_mutate_not_implemented():
    # Test that the mutate method is not implemented
    prompt = Prompt(prompt="Test prompt")
    with pytest.raises(NotImplementedError):
        prompt.mutate(mutation_rate=0.01)


def test_crossover_not_implemented():
    # Test that the crossover static method is not implemented
    with pytest.raises(NotImplementedError):
        Prompt.crossover(
            parent1=Prompt(prompt="Parent 1"), parent2=Prompt(prompt="Parent 2")
        )
