def sum_is_zero(nums):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result

def main():
    strng = input("Enter a list of integers: ")
    nums = list(map(int, strng.split()))
    print(sum_is_zero(nums))

main()

# Example usage
# [-1, 0, 1, 2, -1, -4]
# [-4, -2, 1, 0, 2, 3, -1, 4, -2]
# [0, 0, 0, 0]
