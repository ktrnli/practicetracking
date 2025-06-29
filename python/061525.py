def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parenth = {")":"(", "}":"{", "]":"["}
        stack = []

        for char in s:
            if char in parenth:
                first = stack.pop() if stack else "#"
                if parenth[char] != first:
                    return False

            else:
                stack.append(char)
        return not stack


def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def smallest_word(array):
            smallest = None
            for t in array:
                if smallest == None:
                    smallest = t
                else:
                    if len(t) < len(smallest):
                        smallest = t
            return smallest
        
        def check_prefix(array, pref):
            successes = 0
            for word in array:
                if word.startswith(pref):
                    successes += 1
            if successes == len(array):
                return True
            return False

        smallestWord = smallest_word(strs)

        letters = ""
        common_prefix = ""

        for t in smallestWord:
            letters = letters + t
            if check_prefix(strs, letters):
                common_prefix = letters
            else:
                return common_prefix
        return common_prefix

def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, num in enumerate(nums):
            if num >= target:
                return i
        
        return len(nums)

def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        s = s.strip()
        i = len(s)-1
        while i >= 0:
            if s[i] == " ":
                break
            count += 1
            i -= 1
        return count

def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b

def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        backtrack(0,[])
        return res