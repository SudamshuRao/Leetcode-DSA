class Solution(object):
    def singleNumber(self, nums):
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        return next(key for key,value in d.items() if value == 1)
        
        #result = 0
        # XOR all numbers in the array
        #for num in nums:
        #    result ^= num
        #return result
        #
        #
        #
        #
