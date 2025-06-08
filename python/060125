def differenceOfDistinctValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        rowtot = len(grid)
        coltot = len(grid[0])
        array = []
        for i in range(len(grid)):
            ls = []
            for j in range(len(grid[i])):
                le = set()
                re = set()
                x = i - 1
                y = j - 1
                while x >= 0 and y >= 0:
                    le.add(grid[x][y])
                    x -= 1
                    y -= 1
                x = i + 1
                y = j + 1
                while x < rowtot and y < coltot:
                    re.add(grid[x][y])
                    x += 1
                    y += 1
                ls.append(abs(len(le) - len(re)))
            array.append(ls)
        return array
        
def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import re
        array = re.sub(r"[^A-Za-z ]", " ", paragraph.lower()).split()
        counts = {}
        for x in array:
            if x not in banned:
                if x in counts.keys():
                    counts[x] += 1
                else:
                    counts[x] = 1
        for key, val in counts.items():
            if val == max(counts.values()):
                return key

def numberOfRounds(self, loginTime, logoutTime):
        """
        :type loginTime: str
        :type logoutTime: str
        :rtype: int
        """
        login_h, login_m = list(map(int, loginTime.split(":")))
        logout_h, logout_m = list(map(int, logoutTime.split(":")))
        total_hours = (logout_h - login_h) * 60
        if login_h > logout_h:
            total_hours += 24*60
        if login_h == logout_h and login_m > logout_m:
            total_hours += 24*60
        hours_session = total_hours // 15
        if login_m % 15 != 0:
            login_m = login_m // 15 * 15 + 15
        if logout_m % 15 != 0:
            logout_m = logout_m // 15 * 15
        
        mins_session = int((logout_m - login_m) / 15)
        rounds = hours_session + mins_session
        return rounds if rounds > 0 else 0

def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        start = 0
        end = x
        answer = 0
        while(start <= end):
            mid = start + (end - start) // 2
            if (mid * mid) == x:
                return mid
            elif (mid*mid) > x:
                end = mid - 1
            else: 
                start = mid + 1
                answer = mid
        return answer
        
def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a^= num
        return a

def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for x in range(0, len(nums)):
            if nums[x] == val:
                nums[x] = -1
        nums.sort(reverse=True)
        k = len(nums) - nums.count(-1)
        nums = nums[0:k]
        return k