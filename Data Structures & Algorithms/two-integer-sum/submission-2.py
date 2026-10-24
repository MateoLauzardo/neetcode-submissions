class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for key, value in enumerate(nums):

            dif = target - value

            if dif in hashmap:
                return [hashmap[dif],key]

            else:
                hashmap[value] = key

        