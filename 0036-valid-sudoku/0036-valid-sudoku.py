class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    # Create tuple keys for row, column, and box
                    row_key = (i, element)
                    col_key = (element, j)
                    box_key = (i // 3, j // 3, element)
                    
                    # Check if any of these keys are already in the set
                    if row_key in seen or col_key in seen or box_key in seen:
                        return False
                    
                    # Add the keys to the set
                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(box_key)
        
        return True
