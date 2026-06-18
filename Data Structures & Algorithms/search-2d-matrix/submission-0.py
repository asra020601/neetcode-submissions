class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = 0
        b = len(matrix)-1
        while a<=b:
            current_list = (a+b)//2
            l = 0
            r = len(matrix[current_list])-1
            while l<=r:
                mid = (l+r)//2
                if target == matrix[current_list][mid]:
                    return True
                    break
                elif target<matrix[current_list][mid]:
                    r = mid -1
                else:
                    l = mid+1
            if target>max(matrix[current_list]):
                a = 1 + current_list
            else:
                b = current_list -1
        return False
   