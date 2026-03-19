"""
Bitwise Operations and Hamming Distance
Includes:
- AND, OR, XOR operations on binary sequences
- Hamming distance calculation
Author: Pujan Thapa Magar
"""

# ─────────────────────────────────────────
# 1. Bitwise Operations & Hamming Distance
# ─────────────────────────────────────────
# Hamming distance counts how many bits flipped.
# more bit errors = larger hamming distance = worse channel

data=0b10101010
pattern=0b11110000

AND_Result=data & pattern
OR_Result=data | pattern
XOR_result=data ^ pattern

Hamming_distance=bin(XOR_result).count('1')  # counts differing bits

print(f"AND result: {bin(AND_Result)}")
print(f"OR Result: {bin(OR_Result)}")
print(f"XOR result: {bin(XOR_result)}")
print(f"Hamming distance: {Hamming_distance}")  # 0 = identical, 8 = opposite