def is_safe(row,col,board):
    for i in range(row):
        if board[i]==col or abs(board[i]-col)== abs(i-row):
            return False
    return True    

def solve_n_queens(n,row,board):
    if row==n:
        for i in range(n):
            for j in range(n):
                print("Q" if board[i]==j else ".",end="")
            print()
        print()
        return True
    solution_exists=False
    
    for col in range(n):
        if is_safe(row,col,board):
            board[row]=col
            solution_exists=solve_n_queens(n,row+1,board) or solution_exists
    return solution_exists 
    
def main():
    n=int(input("enter the value of N:"))
    board=[-1]*n
    if not solve_n_queens(n,0,board):
        print(f"solution does not exist for N={n}")

if __name__== "__main__":
    main()
