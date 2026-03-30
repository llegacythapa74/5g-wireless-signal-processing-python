"""
Complex Gaussian Noise Generation
==============================================

Objective: Generate 10000 complex Gaussian noise samples and verify that 
the mean power is approximately 1.0 (i.e., mean of |noise|² ≈ 1).

Author: Pujan Thapa Magar
Date: 2026-03-30
Time Investment: 3 hours (theory + implementation + verification)

Theory:
-------
Complex Gaussian noise is constructed from two independent real Gaussian 
distributions: n = real + j*imag.

For unit mean power (E[|n|²] = 1):
    - Each component (real and imag) has variance = 0.5
    - scale = sqrt(0.5) ensures total power = 0.5 + 0.5 = 1.0
    - |n|² = (real)² + (imag)² represents instantaneous power
"""

import numpy as np

# Generating 10000 complex Gaussian noise samples
# and verify that the mean power is approximately 1.0
# (i.e., mean of |noise|² ≈ 1)

real_samples = np.random.normal(loc = 0, scale =np.sqrt(0.5), size = 10000)
imag_samples = np.random.normal(loc = 0, scale =np.sqrt(0.5), size = 10000)
Gaussian_noise = real_samples + 1j*imag_samples
mean_power = np.mean(np.abs(Gaussian_noise)**2)

if abs(mean_power - 1.0) < 0.1:
    print("   Mean power is approximately 1.0")
    print(f"   Measured value: {mean_power:.4f}")
else:
    print("   Mean power is NOT approximately 1.0")
    print(f"   Measured value: {mean_power:.4f}")