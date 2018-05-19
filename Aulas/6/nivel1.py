N = int(input())
nums = input().split()
nums = [int(num) for num in nums]

if N == 1:
    print(1)
# N >= 2
# '1 1 '1 
count = 0
start = 0 # início da escadinha

while start < N-1: # 
    end = start + 1
    diff = nums[end]-nums[start]
    while end < N and nums[end]-nums[end-1] == diff:
        end += 1
    end -= 1 # final da escadinha
    count += 1
    start = end
    
print(count)
