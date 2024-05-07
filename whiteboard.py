# 1. Read the problem out loud.
# 2. Making assumptions, ask clarifying questions. 
#   2 A. Communication is key
# 3. Coming up with the approach (drawing a mental picture for you and the interviewer) and talking through it
# dont leave us in the dust - verbalize your thought process
# 4. Write the code out (this should actually take a small amount of time)
# 5. Debug / re-evaluate 

# example whiteboard
# Check if Number and its double exists
# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
# More formally check if there exists two indices i and j such that :
# i != j 
# 0 <= i, j < len(arr)
# arr[i] == 2 * arr[j]
# Example 1:
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
# Example 2:
# Input: arr = [7,1,14,11]
# Output: true
# Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
# Example 3:
# Input: arr = [3,1,7,11]
# Output: false
# Explanation: In this case does not exist N and M, such that N = 2 * M.

# going to need a for loop to iterate through my list
# maybe a second for loop to check two numbers at the same time
# i dont think i need any extra variables, for a list or a counter

#             parameter which will hold the place of the above input examples
def dub_nums(arr):
    for x in arr:
        print(x)
        for y in arr:
            print(y)             #
            if x*2 == y:                
                return True
    return False

print(dub_nums([4, 3, 8, 12]))


