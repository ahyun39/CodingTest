class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while True:
            if val not in nums: break
            else: nums.remove(val)