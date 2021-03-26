x = 4           # 4 = 0000 0100
y = 11          # 11 = 0000 1011
z = 0

# 4 | 11

z = x | y;      # 15 = 0000 1111

print("Line 1 - Value of z is ", z)


# 4 >> 11

z = x >> y;     # 0 = 0000 0000

print("Line 2 - Value of z is ", z)


# 4 ^ 11

z = x ^ y;      # 15 = 0000 1111

print("Line 3 - Value of Z is ", z)


# ~4

z = ~x;         # -5 = 0000 0011

print("Line 4 - Value of z is ", z)


# 11 & 4

z = y & x;      # 0 = 0000 0000

print("Line 5 - Value of z is ", z)