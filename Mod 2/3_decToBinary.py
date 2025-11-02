# import random

# # Step 1: Take integer input
# num = int(input("Enter an integer: "))

# # Handle zero as a special case
# if num == 0:
#     binary = "0"
# else:
#     binary = ""
#     temp = num

#     # Step 2: Convert to binary manually
#     while temp > 0:
#         remainder = temp % 2          # Get last bit
#         binary = str(remainder) + binary  # Prepend bit
#         temp //= 2                    # Divide by 2

# # Step 3: Display binary result
# print("Binary equivalent:", binary)

# # Step 4: Pick random bit position
# position = random.randint(0, len(binary) - 1)

# # Step 5: Check the bit (from rightmost side)
# bit = binary[-(position + 1)]
# result = (bit == '1')

# # Step 6: Print results
# print(f"Random position: {position}")
# print(f"Bit at position {position}: {bit}")
# print(f"Result: {result}")

import random

# Step 1: Take an integer input
num = int(input("Enter an integer: "))

# Step 2: Convert to binary (without '0b' prefix)
binary_str = bin(num)[2:]
print(f"Binary equivalent: {binary_str}")

# Step 3: Take a random position within the binary string
position = random.randint(0, len(binary_str) - 1)
print(f"Random position chosen: {position}")

# Step 4: Check if the bit at that position is 1 or 0
bit_value = binary_str[position]
print(f"Bit at position {position}: {bit_value}")

# Step 5: Print True if bit is 1, otherwise False
result = bit_value == '1'
print("Result:", result)
