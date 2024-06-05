def seq_search (nums, x):
    for i in range(len(nums)):#mencari di seluruh elemen nums
        if x == nums[i]:
            return i#mengembalikan index elemaen yang cocok dengan x
        
    return -1# ketika elemen tidak di temukan yang cocok dalam nums 

s = [11,37,45,26,59,28,17,53]
x = 19
pos = seq_search(s,x)
print (f"posisi bilangan {x} didalam list s adalah posisi nomor {pos}")