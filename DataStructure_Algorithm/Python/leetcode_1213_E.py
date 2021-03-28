# 1213. Intersection of Three Sorted Arrays
# Brute fruce is definitely not recommended so we do not discuss here

# Solution 1: three pointers
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        p1, p2, p3 = 0, 0, 0
        res = []
        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            if arr1[p1] == arr2[p2] == arr3[p3]:
                res.append(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
            elif arr1[p1] < arr2[p2]:
                p1 += 1
            elif arr2[p2] < arr3[p3]:
                p2 += 1
            else:
                p3 += 1
        return res