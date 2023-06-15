# N-Queens Solver
 The N-Queens Solver is a Python program that solves the N-Queens problem using a recursive backtracking algorithm. Given a size `n`, the program finds a solution to place `n` queens on an `n x n` chessboard, such that no two queens threaten each other.

## Usage 

### Running the Program

1. Clone the repository:

    ```bash
    git clone https://github.com/MehrunAskrnzhad/N-Queens-Solver
    ```
2. Navigate to the project directory:

    ```bash
    cd N-Queens-Solver
    ```
3. Run the program:
    ```bash 
    python main.py
    ```

    By default, the program solves the 4-Queens problem. You can modify the `n` parameter in the `main.py` file to solve for a different value of `n`.


## Algorithm

The N-Queens Solver uses a recursive backtracking algorithm to find a valid solution. It starts by placing a queen in the first row and iterates through all possible positions in the second row. If a position is found where the queen is not threatened by any other queens, it continues to the next row. If no such position is found, it backtracks to the previous row and explores other positions.

The algorithm repeats this process until all `n` queens are placed on the chessboard or all possibilities are exhausted. It returns the first valid solution it finds or `None` if no solution exists.

## Example Output :
- If You Set The Argument `verbose=True` The Program Will Print Every Queen Placement 
```
Placing Queen at Row 0 and Column 0.
Placing Queen at Row 1 and Column 2.
Placing Queen at Row 1 and Column 3.
Placing Queen at Row 2 and Column 1.
Placing Queen at Row 0 and Column 1.
Placing Queen at Row 1 and Column 3.
Placing Queen at Row 2 and Column 0.
Placing Queen at Row 3 and Column 2.
```
- You Can View The Solve as Matrix 
```python
# ...
solve.displaySolutionMatrix()
```

`Output :`
```
0 1 0 0
0 0 0 1
1 0 0 0
0 0 1 0
```
- You Can View The Solve as Chessboard 
```python
# ...
solve.displayChessboard()
```

`Output :`
```
+---+---+---+---+
|   | Q |   |   |
+---+---+---+---+
|   |   |   | Q |
+---+---+---+---+
| Q |   |   |   |
+---+---+---+---+
|   |   | Q |   |
+---+---+---+---+
```

# License 
This project is licensed under the GNU General Public License v3.0. See LICENSE for more information.

---  

## Additional Files 
- `test.py` : contains a test case (just in case!)
- `nqueenssolver.min.py` : minified version of the code in 15 lines.
