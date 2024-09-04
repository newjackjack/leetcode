def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def maxSharedCategories(favoriteCategories):
    n = len(favoriteCategories)
    max_gcd = 0
    
    # Compare all pairs of elements in the array
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate the GCD of the pair (favoriteCategories[i], favoriteCategories[j])
            current_gcd = gcd(favoriteCategories[i], favoriteCategories[j])
            # Update max_gcd if current_gcd is larger
            max_gcd = max(max_gcd, current_gcd)
    
    return max_gcd

# Example usage:
favoriteCategories = [4, 2, 6, 8]
print(maxSharedCategories(favoriteCategories))  # Output should be 4