class Solution:
    def findMaxLength(self, nums) -> int:
        if len(nums) <= 3:
            return 2

        maxSofar = 2
        map01 = {0: 0, 1: 0}
        for i in range(len(nums)):
            map01[nums[i]] += 1
            if map01[0] == map01[1]:
                maxSofar = map01[0] + map01[1]
            else:
                maxSofar = max(maxSofar, 2 * min(map01[0], map01[1]))

        return maxSofar


s = Solution()
print(s.findMaxLength([1,0,0,1,0,0,0,1,1]))