from verificacao import verificaSubSetSum
import unittest

class TestSubsetSum(unittest.TestCase):

    def test_all(self):
        S = [3, 1, 1, 2, 2, 1]
        S1 = [1, 1, 1, 2]
        S2 = [2, 3]

        self.assertEqual(verificaSubSetSum(S, S1, S2), True)

        S1 = [3, 1, 1]
        S2 = [2, 2, 1]

        self.assertEqual(verificaSubSetSum(S, S1, S2), True)

        S1 = [5, 1, 1]
        S2 = [2, 2, 1]

        self.assertEqual(verificaSubSetSum(S, S1, S2), False)

        S1 = [1, 1, 1]
        S2 = [1, 1, 1]

        self.assertEqual(verificaSubSetSum(S, S1, S2), False)

        S1 = [2, 1, 1]
        S2 = [3, 2, 1]

        self.assertEqual(verificaSubSetSum(S, S1, S2), False)

        S1 = [2, 1, 1]
        S2 = [3, 1]

        self.assertEqual(verificaSubSetSum(S, S1, S2), False)



if __name__ == '__main__':
    unittest.main()