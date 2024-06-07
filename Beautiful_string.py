def min_operations(STR):
  """
  This function calculates the minimum number of operations required to make a binary string beautiful.

  Args:
      STR: A binary string containing only '0' and '1' characters.

  Returns:
      The minimum number of operations required to make the string beautiful.
  """

  # Initialize counters for starting with either 0 or 1
  count_0 = 0
  count_1 = 0

  # Iterate through the string
  for i in range(len(STR)):
    # If the character at index i doesn't match the expected pattern (0 at even index, 1 at odd index), increment the corresponding counter
    if (i % 2 == 0 and STR[i] == '1') or (i % 2 == 1 and STR[i] == '0'):
      count_0 += 1
    else:
      count_1 += 1
    print(f"value of i is: {i}")
    print(f"first condition values: {i%2} {STR[i]}, result: {i%2==0 and STR[i]=='1'}")
    print(f"first condition values: {i%2} {STR[i]}, result: {i%2==1 and STR[i]=='0'}")
    print(f"Count_0 is : {count_0}, Count_1 is: {count_1}")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

  # Return the minimum count of operations needed
  return min(count_0, count_1)

# Example usage
STR = "0010"
min_ops = min_operations(STR)
print(f"Minimum operations to make '{STR}' beautiful:", min_ops)

