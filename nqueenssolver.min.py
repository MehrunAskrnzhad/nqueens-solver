import sys

class NQueensSolver:
    def __init__(self,n):
        if n<=3: sys.exit("n Must be greater or equal to 4.") 
        self.n,self.solution=n,[]
        def p(r, q):
            if r==self.n:return q
            for c in range(self.n):
                if all(c!=q[l] and c!=q[l]+r-l and c!=q[l]-r+l for l in range(r)): 
                    q[r]=c
                    if(result:=p(r+1,q)): return result
            return None
        self.s=p(0,[None]*self.n)
    def get_chessboard(self):return ''.join([''.join(["+---"*self.n+"+\n",''.join(["| Q " if self.s[r]==c else "|   " for c in range(self.n)])+"|\n"]) for r in range(self.n)]) + "+---" * self.n + "+\n"
    def display_chessboard(self):print(self.get_chessboard())
    def get_solution_matrix(self):return [[1 if c==self.s[r] else 0 for c in range(self.n)] for r in range(self.n)]
    def display_solution_matrix(self):[print(' '.join(map(str,r))) for r in self.get_solution_matrix()]