'''
https://leetcode.com/problems/two-sum/

Topics: Array, Hash Table

Time: O(n)
Space: O(n)
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i, n in enumerate(nums):
            complement = target - n
            if n in complements:
                return [complements[n], i]
            complements[complement] = i

        raise Exception("No solution was found")
