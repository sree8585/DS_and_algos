# We have a collection of stones, each stone has a positive integer weight.
#
# Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y
# with x <= y.  The result of this smash is:
#
# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.

# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

class Solution:
    def lastStoneWeight(self, stones) -> int:
        stones.sort()
        while len(stones) > 1:
            # print(stones)
            x = stones[-1]
            y = stones[-2]
            if x - y == 0:
                stones = stones[:-2]
                continue
            else:
                val = x - y
                assert val >= 0
                subStones = stones[:-2]
                if len(subStones) == 0:
                    return val

                if val <= subStones[0]:
                    stones = [val] + subStones
                elif val >= subStones[-1]:
                    stones = subStones + [val]
                else:
                    idx = self.searchIndex(subStones, val)
                    subStones.insert(idx, val)
                    stones = subStones
                    continue

        return stones[0] if len(stones) == 1 else 0

    def searchIndex(self, stones, val):
        left = 0
        right = len(stones) - 1
        while left < right:

            mid = (left + right) // 2
            # print(val, left, right, mid, stones[mid])
            if stones[mid] == val or (stones[mid - 1] <= val < stones[mid]):
                return mid
            elif stones[mid] < val <= stones[mid + 1]:
                return mid + 1
            else:
                if stones[mid - 1] > val:
                    right = mid - 1
                else:
                    left = mid + 1


s = Solution()

print (s.lastStoneWeight(stones = [434,667,378,919,212,902,240,257,208,996,411,222,557,634,425,949,755,833,785,886,40,159,932,157,764,916,85,300,130,278]))


print (s.lastStoneWeight(stones =[2,7,4,1,8,1]))