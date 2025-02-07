def spy_game(nums):
    sequence = [0, 0, 7]
    seq_index = 0
    
    for num in nums:
        if num == sequence[seq_index]:
            seq_index += 1
            if seq_index == len(sequence):
                return True
    
    return False
    
print(spy_game([4, 6, 0, 2, 4, 0, 6, 7,])) 