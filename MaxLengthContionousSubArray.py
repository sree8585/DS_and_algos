class Solution:
    def findMaxLength(self, nums) -> int:
        if len(nums) <= 3:
            return 2
        else:
            curCharacterChecking = nums[0]
            prevCharContinous = None
            curCharContinuous = 0
            maxSofar = 2

            for i in range(len(nums)):
                ch = nums[i]
                if ch == curCharacterChecking:
                    curCharContinuous += 1
                    print(i, curCharContinuous)
                else:
                    curCharacterChecking = ch
                    if prevCharContinous is not None:
                        contFormed = 2 * min(prevCharContinous, curCharContinuous)
                        if maxSofar < contFormed:
                            maxSofar = contFormed

                    prevCharContinous = curCharContinuous
                    curCharContinuous = 1
            contFormed = 2 * min(prevCharContinous, curCharContinuous)
            if maxSofar < contFormed:
                return contFormed
            else:
                return maxSofar


s = Solution()
print(s.findMaxLength([0,1,0,1,1,1,0,0,0]))