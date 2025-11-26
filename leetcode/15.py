# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

 

 

# 示例 1：

# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
        # 这是一个优化项，没有也没问题，因为数组已排序，第一个数>0 时，后面所有数都 ≥它，三数之和必定 > 0，如果没有这个可能会做一些无用功。
            if nums[i] > 0:
                break

            # 第一个数去重，continue是跳过本次循环    
            if i > 0 and nums[i] == nums[i-1]:
                continue    # 跳过本次循环，i 直接到下一个

            # 转化为两数之和
            target = -nums[i]

            # 前面for循环固定第一个数，j从第二个数开始，k从最右侧开始，这样就保证绝对不会索引重复
            j = i + 1
            k = len(nums) - 1

            while j < k:
                current_sum = nums[j] + nums[k]
                if current_sum == target:
                    result.append([nums[i], nums[j], nums[k]])

                    # 去重：跳过重复的j
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    # 去重：跳过重复的k
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1

                    # 可能不只有一组，所以还需要继续迭代
                    j += 1
                    k -= 1
                elif current_sum < target:
                    j += 1
                else:
                    k -= 1
        return result