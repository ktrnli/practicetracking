class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = []
        old = 0
        for x in nums:
            sum.append(x + old)
            old += x
        return sum
    
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        sums = []
        for a in range(0, len(accounts)):
            sums.append(sum(accounts[a]))
        return max(sums)
    
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer=[]
        for i in range(1, n+1):
            if (i%3 + i%5 == 0):
                answer.append("FizzBuzz")
            elif (i%3 == 0):
                answer.append("Fizz")
            elif (i%5 == 0):
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer
    
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        while num != 0:
            if (num%2 == 0):
                num /= 2
            else:
                num -= 1
            count += 1
        return count
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)-1):
            for x in range(1, len(nums)):
                if nums[i] + nums[x] == target and x!=i:
                    return [i, x]