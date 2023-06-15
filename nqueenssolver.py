from typing import List

class NQueensSolver:
    def __init__(self, n: int, verbose: bool = False) -> None:
        """
        Initialize the NQueensSolver class with the specified board size (n) and verbosity option (verbose).

        Args:
            n: The size of the chessboard and the number of queens to be placed.
            verbose: Whether to print verbose output during the solution process. Defaults to False.
        """
        self.n = n
        self.solution = []

        def place_queen(row: int, queens: List[int]) -> List[int]:
            """
            Recursive function to place the queens on the chessboard and find a valid solution.

            Args:
                row: The current row being processed.
                queens: The list to store the positions of queens.

            Returns:
                The positions of queens if a valid solution is found, None otherwise.
            """
            if row == self.n:
                return queens

            for col in range(self.n):
                if all(
                    col != queens[c] and col != queens[c] + row - c and col != queens[c] - row + c
                    for c in range(row)
                ):
                    queens[row] = col
                    if verbose:
                        print(f"Placing Queen at Row {row} and Column {col}.")
                    if (result := place_queen(row + 1, queens)):
                        return result

            return None

        self.solution = place_queen(0, [None] * self.n)

    def get_chessboard(self) -> str:
        """
        Generate a string representation of the chessboard with queens placed.

        Returns:
            The string representation of the chessboard.
        """
        chessboard = ""
        for row in range(self.n):
            chessboard += "+---" * self.n + "+\n"
            for col in range(self.n):
                if self.solution[row] == col:
                    chessboard += "| Q "
                else:
                    chessboard += "|   "
            chessboard += "|\n"
        chessboard += "+---" * self.n + "+\n"
        return chessboard

    def display_chessboard(self) -> None:
        """
        Print the string representation of the chessboard with queens placed.
        """
        print(self.get_chessboard())

    def get_solution_matrix(self) -> List[List[int]]:
        """
        Generate a matrix representation of the chessboard with queens placed.

        Returns:
            The matrix representation of the chessboard.
        """
        matrix = [[0] * self.n for _ in range(self.n)]
        for row, col in enumerate(self.solution):
            matrix[row][col] = 1
        return matrix

    def display_solution_matrix(self) -> None:
        """
        Print the matrix representation of the chessboard with queens placed.
        """
        for row in self.get_solution_matrix():
            print(' '.join(map(str, row)))
