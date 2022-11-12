from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        left = 0
        right = len(nums) - 1
        exists = []
        counter = 0
        while left < right:
            avg = (nums[left] + nums[right]) / 2.0
            left += 1
            right -= 1
            if avg not in exists:
                counter += 1
                exists.append(avg)

        return counter

if __name__ == '__main__':
    print(Solution().distinctAverages([4,1,4,0,3,5]))
