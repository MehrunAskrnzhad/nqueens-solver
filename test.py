from nqueenssolver import NQueensSolver
import unittest

class NQueensSolverTestCase(unittest.TestCase):
    def testSolutionExists(self):
        """
        Test case to verify that a solution exists for a valid board size.
        """
        solver = NQueensSolver(4)
        self.assertIsNotNone(solver.solution)

    def testGetChessboard(self):
        """
        Test case to verify the correctness of the chessboard representation.
        """
        solver = NQueensSolver(4)
        expectedChessboard = (
            "+---+---+---+---+\n"
            "|   | Q |   |   |\n"
            "+---+---+---+---+\n"
            "|   |   |   | Q |\n"
            "+---+---+---+---+\n"
            "| Q |   |   |   |\n"
            "+---+---+---+---+\n"
            "|   |   | Q |   |\n"
            "+---+---+---+---+\n"
        )
        self.assertEqual(solver.getChessboard(), expectedChessboard)

    def testGetSolutionMatrix(self):
        """
        Test case to verify the correctness of the solution matrix representation.
        """
        solver = NQueensSolver(4)
        expectedMatrix = [
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [1, 0, 0, 0],
            [0, 0, 1, 0],
        ]
        self.assertEqual(solver.getSolutionMatrix(), expectedMatrix)


if __name__ == "__main__":
    unittest.main()
