class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSeen = [set() for _ in range(9)]
        colSeen = [set() for _ in range(9)]
        boxSeen = [set() for _ in range(9)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rowSeen[r] or val in colSeen[c] or val in boxSeen[(r // 3) * 3 + (c // 3)]:
                    return False
                
                rowSeen[r].add(board[r][c])
                colSeen[c].add(board[r][c])
                boxSeen[(r // 3) * 3 + (c // 3)].add(board[r][c])
        return True
