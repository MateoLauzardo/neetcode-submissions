class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:



        # rows 
        for i in range(9):
            hashset = set()
            for j in range(9):

                value = board[i][j]

                if value in hashset:
                    return False 

                elif value != ".":
                    hashset.add(value)


        # column
        for i in range(9):
            hashset = set()
            for j in range(9):
                
                # the second value is the one increase 9
                # times before we reset, first one is where
                # we wait 
                value = board[j][i]

                if value in hashset:
                    return False 

                elif value != ".":
                    hashset.add(value)



        # boxes
        start = [
            (0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6)
        ]

        for i, j in start: 

            s = set()

            for row in range(i, i+3):
                for col in range(j, j+3):

                    item = board[row][col]
                    
                    if item in s:
                        return False 

                    elif item != ".":
                        s.add(item)

        return True 

        