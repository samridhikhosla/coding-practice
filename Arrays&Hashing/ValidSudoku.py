class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        column_flag = True

        for i in board: #column checking
            valid = set()
            for j in i:
                if j in valid and j != ".":
                    column_flag = False
                else:
                    valid.add(j)
        

        row_flag = True
            
        for i in range(len(board)): #row checking
            valid = set()
            for j in range(len(board)):
                row = board[j][i]
                if row in valid and row != ".":
                    row_flag = False
                else:
                    valid.add(row)

        
        square_flag = True
        current_row = 0
        current_col = 0

        for cycles in range(9): #square checking
            valid = set()

            for i in range(current_row, current_row + 3):
                for j in range(current_col, current_col + 3):
                    val = board[i][j]  
                    if val != ".":
                        if val in valid:
                            square_flag = False
                        else:
                            valid.add(val)

            current_col += 3

            if current_col == 9:
                current_col = 0
                current_row += 3

        return row_flag and column_flag and square_flag


def main():
    x = Solution()
    x.isValidSudoku(

[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

)
main()