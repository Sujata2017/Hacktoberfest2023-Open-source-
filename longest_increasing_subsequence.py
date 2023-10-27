# Given an unsorted array of integers, find the length of longest increasing subsequence

def lengthOfLIS(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Example usage:
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
result = lengthOfLIS(arr)
print("Length of Longest Increasing Subsequence:", result)
