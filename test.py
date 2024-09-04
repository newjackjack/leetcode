

# # Python3 program for the above approach
 
 
# def countSetBits(n):
#     count = 0
#     while n:
#         count += 1
#         n &= (n-1)
#     return count
 
# # Function that return count of
# # flipped number
 
 
# def FlippedCount(a, b):
 
#     # Return count of set bits in
#     # a XOR b
#     return countSetBits(a ^ b)
 
 
 
# # Driver code
# if __name__ == "__main__":
#   a = 5
#   b = 6
 
#   # Function call
#   print(FlippedCount(a, b))


# Roblox
# def is_block_free(memory, start_index, block_size):
#     # Check if the block of memory is free starting from start_index
#     if start_index + block_size > len(memory):
#         return False  # Block goes out of memory bounds
    
#     for j in range(block_size):
#         if memory[start_index + j] != 0:
#             return False  # Found an occupied memory unit
    
#     return True  # All memory units in the block are free

# def solution(memory, queries):
#     results = []
#     next_id = 1  # Start ID counter from 1
#     allocations = {}  # Dictionary to track allocated memory ranges by ID
    
#     for query in queries:
#         if query[0] == 0:  # alloc X
#             X = query[1]
#             start_index = -1  # Default to -1 if no block found
            
#             # Search for a block of X free units starting at an index divisible by 8
#             for i in range(0, len(memory), 8):
#                 if is_block_free(memory, i, X):
#                     # Found a valid block
#                     start_index = i
#                     # Mark memory as allocated
#                     for j in range(X):
#                         memory[i + j] = 1
#                     # Record the allocation with the next available ID
#                     allocations[next_id] = (start_index, X)
#                     next_id += 1
#                     break
            
#             results.append(start_index)
        
#         if query[0] == 1:  # erase ID
#             ID = query[1]
#             if ID in allocations:
#                 start, length = allocations.pop(ID)
#                 # Free the allocated memory block
#                 for i in range(start, start + length):
#                     memory[i] = 0
#                 results.append(length)
#             else:
#                 results.append(-1)
    
#     return results

# # Example usage:
# memory = [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0]
# queries = [[0, 2], [0, 1], [0, 1], [1, 1], [0, 3], [1, 4], [0, 4]]
# print(solution(memory, queries))

# Roblox q2
def count_subarrays_with_k_pairs(numbers, k):
    n = len(numbers)
    result = 0
    
    # Iterate through every possible starting point of subarray
    for start in range(n):
        freq = {}
        pair_count = 0
        
        # Iterate through every possible ending point for the subarray starting at 'start'
        for end in range(start, n):
            num = numbers[end]
            
            # Update frequency map
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            
            # Update pair count if we have at least two occurrences of this number
            if freq[num] % 2 == 0:
                pair_count += 1
            
            # If the current subarray has at least 'k' pairs, count it
            if pair_count >= k:
                result += 1
    
    return result

# Example usage:
numbers = [0, 1, 0, 1, 0]
k = 2
print(count_subarrays_with_k_pairs(numbers, k))  # Output should be 3

numbers = [2, 2, 2, 2, 2, 2]
k = 3
print(count_subarrays_with_k_pairs(numbers, k))  # Output should be 1

numbers = [1, 3, 3, 1]
k = 1
print(count_subarrays_with_k_pairs(numbers, k))  # Output should be 4

