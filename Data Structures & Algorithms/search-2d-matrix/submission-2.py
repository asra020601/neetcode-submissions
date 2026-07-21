class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            left = 0
            right  =  len(matrix[i])-1
            if matrix[i][right]<target:#if the target is bigger than the biggest number in the array we skip the whole array
               continue
            #print(matrix[i][left],matrix[i][right])  
            while left<=right:
                mid = (left+right)//2
                if target<matrix[i][mid]:
                    right = mid-1
                if target > matrix[i][mid]:
                    left = mid+1
                if target == matrix[i][mid]:
                    return True
        return False
