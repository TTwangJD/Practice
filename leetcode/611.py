"""
Docstring for leetcode.611
#   错误： 双指针的单调性问题

# for i in range(n - 2):
        #     left = i+1
        #     right = n - 1
        #     x = nums[i]
        #     while left < right:
        #         print(f"{nums[i]},{nums[left]},{nums[right]}")
        #         if x + nums[left] > nums[right]:
        #             res += right - left
        #             print(f"{i},{left},{right},{res}")
        #             right -=1
        #             left = i + 1
        #         else:
        #             left += 1
        不应破坏单调性，否则退化复杂度O(n^3)
"""
#最大边
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(n-1,1,-1):
            left, right = 0, i-1
            x = nums[i]
            while left < right:
                if nums[right] + nums[left] > x:
                    res += right - left
                    right -=1
                else:
                    left +=1
        return res
    
#最小边
"""
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            a = nums[i]
            if a == 0:  # 三角形的边不能是 0
                continue
            j = i + 1
            for k in range(i + 2, n):
                while nums[k] - nums[j] >= a:
                    j += 1
                # 如果 a=nums[i] 和 c=nums[k] 固定不变
                # 那么 b 可以是 nums[j],nums[j+1],...,nums[k-1]，一共有 k-j 个
                ans += k - j
        return ans


"""