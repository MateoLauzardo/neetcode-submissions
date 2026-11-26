class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        

        # row 
        for i in range(9):
            
            hashset = set() 

            for j in range(9):
            
                # first box represents up and down
                # second box represents left to right 
                value = board[i][j]

                if value in hashset:
                    return False 
                elif value != '.':
                    hashset.add(value)



        # columns 
        for i in range(9):
            
            hashset = set() 

            for j in range(9):
            
                # first box represents up and down
                # second box represents left to right 
                value = board[j][i]

                if value in hashset:
                    return False 
                elif value != '.':
                    hashset.add(value)
        


        # sub matrixs 
        first = [
            (0,0),(0,3),(0,6),
            (3,0),(3,3),(3,6),
            (6,0),(6,3),(6,6)
        ]

        # i represent first value in tuple, j is second 
        for i, j in first: 
            
            s = set()

            for row in range(i, i+3):
                for col in range(j, j+3):

                    value = board[row][col]
                    
                    if value in s:
                        return False 

                    elif value != '.':
                        s.add(value)

                    
        return True 


        
