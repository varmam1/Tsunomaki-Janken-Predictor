import unittest

class TestMarkovModel(unittest.TestCase):

    def test_markov_model_with_empty_data(self):
        self.assertEqual(markov_chains.rpsMarkovModel([]), {}, "Should be empty dict")

if __name__ == '__main__':
    unittest.main()