class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        tail = 0

        for head in range(1, len(nums)):
            if nums[head] != nums[tail]:
                tail += 1
                nums[tail] = nums[head]

        return tail + 1
