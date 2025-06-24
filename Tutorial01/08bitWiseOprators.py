# Bitwise complement (~)
# ~ flips all the bits in the number's binary representation.
# In practice, ~n is equal to -(n+1)
print(~12)  # Output: -13 (because -(12+1) = -13)
print(~45)  # Output: -46 (because -(45+1) = -46)

# Bitwise AND (&)
# Compares each bit of two numbers; 1 if both bits are 1, else 0
print(12 & 13)  # Output: 12 (binary AND of 1100 & 1101 is 1100)

# Bitwise OR (|)
# Compares each bit of two numbers; 1 if at least one bit is 1
print(12 | 13)  # Output: 13 (binary OR of 1100 | 1101 is 1101)
print(25 | 83)  # Output: 91 (binary OR of 11001 | 1010011 is 1011011)

# Bitwise XOR (^)
# Compares each bit of two numbers; 1 if bits are different
print(12 ^ 13)  # Output: 1 (1100 ^ 1101 = 0001)
print(25 ^ 32)  # Output: 57 (11001 ^ 100000 = 111001)

# Left shift (<<)
# Moves bits to the left by the specified number of places.
# Every left shift is equivalent to multiplying by 2^shift_amount.
print(10 << 2)  # Output: 40 (10 * 2^2 = 40)
print(10 << 3)  # Output: 80 (10 * 2^3 = 80)
print(20 << 2)  # Output: 80 (20 * 2^2 = 80)

# Right shift (>>)
# Moves bits to the right by the specified number of places.
# Every right shift is equivalent to integer division by 2^shift_amount.
print(10 >> 2)  # Output: 2 (10 // 2^2 = 2)
