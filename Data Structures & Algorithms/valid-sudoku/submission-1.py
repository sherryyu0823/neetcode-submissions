class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            num = {1, 2, 3, 4, 5, 6, 7, 8, 9}

            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                elif int(board[i][j]) in num:
                    num.remove(int(board[i][j]))
                else:
                    return False
        
        for i in range(len(board)):
            num = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                elif int(board[j][i]) in num:
                    num.remove(int(board[j][i]))
                else:
                    return False
        

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                num = {1, 2, 3, 4, 5, 6, 7, 8, 9}

                for r in range(3):
                    for c in range(3):
                        v = board[i+r][j+c]
                        if v == ".":
                            continue
                        elif int(v) in num:
                            num.remove(int(v))
                        else:
                            return False

            
        return True

