# Read in file
fileName = "input2.txt"
f = open(fileName, "r")

total = 0
total2 = 0

'''
# Part 1
for line in f.read().split('\n'):
    nums = [int(n) for n in line.split()]
    final_nums = []

    while set(nums) != set([0]):
        final_nums.append(nums[-1])
        nums = [nums[i] - nums[i-1] for i in range(1, len(nums))]

    total += sum(final_nums)

print(total)
'''

# Part 2
for line in f.read().split('\n'):
    nums = [int(n) for n in line.split()]
    first_nums = []

    while set(nums) != set([0]):
        first_nums.append(nums[0])
        nums = [nums[i] - nums[i-1] for i in range(1, len(nums))]

    for i, num in enumerate(first_nums):
        total += num if i % 2 == 0 else -num

print(total)