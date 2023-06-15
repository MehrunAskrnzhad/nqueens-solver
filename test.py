import unittest
from nqueenssolver import NQueensSolver


class NQueensSolverTestCase(unittest.TestCase):
    def test_solution_exists(self):
        """
        Test case to verify that a solution exists for a valid board size.
        """
        solver = NQueensSolver(4)
        self.assertIsNotNone(solver.solution)

    def test_get_chessboard(self):
        """
        Test case to verify the correctness of the chessboard representation.
        """
        solver = NQueensSolver(4)
        expected_chessboard = (
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
        self.assertEqual(solver.get_chessboard(), expected_chessboard)

    def test_get_solution_matrix(self):
        """
        Test case to verify the correctness of the solution matrix representation.
        """
        solver = NQueensSolver(4)
        expected_matrix = [
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [1, 0, 0, 0],
            [0, 0, 1, 0],
        ]
        self.assertEqual(solver.get_solution_matrix(), expected_matrix)


if __name__ == "__main__":
    unittest.main()
