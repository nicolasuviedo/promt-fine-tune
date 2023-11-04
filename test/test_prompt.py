import unittest
from prompt import Example, Prompt


class TestExample(unittest.TestCase):
    def setUp(self):
        self.example = Example(input="input", output="output")

    def test_post_init(self):
        self.assertEqual(self.example.input, "input")
        self.assertEqual(self.example.output, "output")
        self.assertTrue(callable(self.example.format))

    def test_str(self):
        self.assertEqual(str(self.example), "input -> output")


class TestPrompt(unittest.TestCase):
    def setUp(self):
        self.prompt = Prompt(prompt="prompt")

    def test_prompt(self):
        self.assertEqual(self.prompt.prompt, "prompt")


if __name__ == "__main__":
    unittest.main()
