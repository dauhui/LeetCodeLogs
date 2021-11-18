class Solution(object):
    nums = [2,2]

    cnt = 1
    for i in nums:
        if (cnt in nums) == False:
            if nums[0] == 1:
                print([cnt,cnt])
            else:
                print([cnt+1,cnt])
            break
        cnt += 1