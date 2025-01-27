def longest_increasing_subsequence(nums):
    n = len(nums)
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    max_length = max(lis)
    max_index = lis.index(max_length)

    second_lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and second_lis[i] < second_lis[j] + 1 and lis[j] + 1 < max_length:
                second_lis[i] = second_lis[j] + 1
    second_max_length = max(second_lis)
    second_max_index = second_lis.index(second_max_length)

    lis_subsequence = []
    second_lis_subsequence = []
    i = max_index
    while i >= 0 and max_length > 0:
        if lis[i] == max_length:
            lis_subsequence.append(nums[i])
            max_length -= 1
        i -= 1
    lis_subsequence.reverse()

    i = second_max_index
    while i >= 0 and second_max_length > 0:
        if second_lis[i] == second_max_length:
            second_lis_subsequence.append(nums[i])
            second_max_length -= 1
        i -= 1
    second_lis_subsequence.reverse()

    return lis_subsequence, second_lis_subsequence


with open('17(2).txt', "r") as file:
    nums = [int(num) for num in file.read().split()]

lis, second_lis = longest_increasing_subsequence(nums)
print("LIS:", len(lis))
print("2LIS:", len(second_lis))