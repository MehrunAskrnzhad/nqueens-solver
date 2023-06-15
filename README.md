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
