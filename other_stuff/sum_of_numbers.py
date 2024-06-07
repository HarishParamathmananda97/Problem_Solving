""" IBM asked question for 2yrs experience """
""" Using inbuilt function sum """
i = 0
j = 5
k = -1

# Process flow from i to j
total = sum(range(i, j + 1))  # 15

# Process flow from j to k
total += sum(range(j - 1, k - 1, -1)) # 14

print("Total:", total)



"""Using maths formula ((b - a + 1) * (a + b)) / 2 """
i = 0
j = 5
k = -1

# Calculate sum from i to j
sum_i_to_j = ((j - i + 1) * (i + j)) // 2

# Calculate sum from j to k
sum_j_to_k = ((j- 1 - k + 1) * (j - 1 + k)) // 2

# Total sum
total = sum_i_to_j + sum_j_to_k

print("Total:", total)
