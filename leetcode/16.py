class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = nums[0] + nums[1] + nums[n-1]
        for i in range(n-2):
            left = i+1
            right = n - 1
            x = nums[i]
            # if( x + nums[right-1] + )
            res = res if abs(res - target) < abs(x + nums[left] + nums[right] - target) else x + nums[left] + nums[right]
            while left < right:

                tmp = (x + nums[left] + nums[right] - target)
                #print(f"tmp:{tmp},,sub:{sub},res:{res},{x} + {nums[left]} + {nums[right]}")
                if abs(tmp) < abs(res - target):
                    res = x + nums[left]+ nums[right]
                if tmp < 0:
                    left+=1
                else:
                    right-=1
        return res

# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

# 返回这三个数的和。

# 假定每组输入只存在恰好一个解。

 

# 示例 1：

# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。
# 示例 2：

# 输入：nums = [0,0,0], target = 1
# 输出：0
# 解释：与 target 最接近的和是 0（0 + 0 + 0 = 0）。

'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff = inf
        for i in range(n - 2):
            x = nums[i]
            if i and x == nums[i - 1]:
                continue  # 优化三

           # 优化一
            s = x + nums[i + 1] + nums[i + 2]
            if s > target:  # 后面无论怎么选，选出的三个数的和不会比 s 还小
                if s - target < min_diff:
                    ans = s  # 由于下一行直接 break，这里无需更新 min_diff
                break

            # 优化二
            s = x + nums[-2] + nums[-1]
            if s < target:  # x 加上后面任意两个数都不超过 s，所以下面的双指针就不需要跑了
                if target - s < min_diff:
                    min_diff = target - s
                    ans = s
                continue

            # 双指针
            j, k = i + 1, n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s == target:
                    return s
                if s > target:
                    if s - target < min_diff:  # s 与 target 更近
                        min_diff = s - target
                        ans = s
                    k -= 1
                    while j<k and nums[k+1]==nums[k]:
                        k-=1
                else:  # s < target
                    if target - s < min_diff:  # s 与 target 更近
                        min_diff = target - s
                        ans = s
                    j += 1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
        return ans

'''