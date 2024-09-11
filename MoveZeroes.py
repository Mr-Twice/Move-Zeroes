 pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
        for a in range(pos,len(nums)):
            nums[a] = 0       
