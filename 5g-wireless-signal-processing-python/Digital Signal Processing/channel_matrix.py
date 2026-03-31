"""
MIMO Channel Matrix Analysis
============================
Generate random complex channel matrix and verify Frobenius norm calculation.
Used in massive MIMO systems to assess total channel energy and capacity.

Author: Pujan Thapa Magar
Date: 2026-03-31

Theory:
-------
A 64x64 MIMO channel matrix H represents 64 transmit and 64 receive antennas.
Each entry h_ij = x + j*y models the complex gain between antenna pair (i,j).

Frobenius norm ||H||_F = sqrt(sum(|h_ij|^2)) measures total channel energy.
For unit-power entries, theoretical ||H||_F = sqrt(4096) = 64.

Verification against np.linalg.norm ensures our manual calculation is correct.
"""

import numpy as np

# Generating 64x64 complex Gaussian channel with unit power per element
real_part = np.random.normal(loc = 0, scale = np.sqrt(0.5), size = (64,64))
imag_part = np.random.normal(loc = 0, scale = np.sqrt(0.5), size = (64,64))
channel_matrix = real_part + 1j*imag_part

print(f"Channel Matrix Size: {channel_matrix.shape}")
print(f"Data Type: {channel_matrix.dtype}")
print(f"Mean of the channel matrix: {np.mean(np.abs((channel_matrix))**2):.4f}")

# Manual Frobenius norm: sqrt(sum of |h_ij|^2)
squared_magnitudes = np.abs(channel_matrix)**2
Frobenius_norm = np.sqrt(np.sum(squared_magnitudes))
print(f"Manual Frobenius norm: {Frobenius_norm:.4f}")

# Verification against built-in function
Frobenius_builtin = np.linalg.norm(channel_matrix, 'fro')
difference = abs(Frobenius_norm - Frobenius_builtin)
print(f"Actual differnece value: {difference:.4f}")

if difference < 1e-10:
    print(f"Verification passed")
else:
    print(f"Verification failed")