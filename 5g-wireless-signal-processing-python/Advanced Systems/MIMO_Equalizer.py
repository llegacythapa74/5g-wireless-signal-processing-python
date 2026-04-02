"""
ZF vs MMSE Equalizer Comparison — 4x4 MIMO
==========================================
Implementing both equalizers for a 4x4 MIMO system and comparing
their Mean Squared Error at 15 dB SNR over an AWGN channel.
Author: Pujan Thapa Magar

Theory:

Both equalizers try to recover the transmitted symbols x from y = Hx + n.
ZF (Zero Forcing) inverts the channel directly — it eliminates interference
but amplifies noise in the process. Works well at high SNR, breaks down when
noise is significant.

MMSE (Minimum Mean Square Error) adds a noise term before inverting:
    x_hat = (H^H * H + sigma^2 * I)^-1 * H^H * y
The sigma^2 * I term regularizes the inversion so noise doesn't get amplified.
At high SNR sigma^2 approaches zero and MMSE collapses into ZF.
At low SNR MMSE pulls the solution away from ZF and wins on MSE.
"""

"""
ZF vs MMSE Equalizer Comparison — 4x4 MIMO
Author: Pujan Thapa Magar

Implementing both equalizers and comparing MSE to see
which one handles noise better at 15 dB SNR.
ZF ignores noise, MMSE accounts for it — curious to see the difference.
"""

import numpy as np

np.random.seed(42)

# 4x4 means 4 transmit and 4 receive antennas
N = 4
snr_db = 15
snr_linear = 10 ** (snr_db / 10)
noise_power = 1 / snr_linear

# complex gaussian channel — real world channels look like this
H = (np.random.randn(N, N) + 1j * np.random.randn(N, N)) / np.sqrt(2)

# QPSK has 4 possible symbols, normalized so average power = 1
qpsk = np.array([1+1j, -1+1j, 1-1j, -1-1j]) / np.sqrt(2)
x = np.random.choice(qpsk, size=N)

# additive white gaussian noise
n = np.sqrt(noise_power/2) * (np.random.randn(N) + 1j * np.random.randn(N))

# what the receiver actually gets
y = H @ x + n

# ZF — just inverts the channel, completely ignores that noise exists
# works well at high SNR, falls apart when noise is significant
H_H = H.conj().T
x_hat_zf = np.linalg.pinv(H) @ y

# MMSE — adds noise_power * I before inverting
# this term regularizes the inversion so noise doesn't get amplified
# the higher the noise, the more this term pulls the solution away from ZF
A = H_H @ H + noise_power * np.eye(N)
x_hat_mmse = np.linalg.solve(A, H_H @ y)

# MSE tells us how far the detected symbols are from the originals
mse_zf = np.mean(np.abs(x - x_hat_zf)**2)
mse_mmse = np.mean(np.abs(x - x_hat_mmse)**2)

print(f"SNR: {snr_db} dB")
print(f"ZF MSE:   {mse_zf:.6f}")
print(f"MMSE MSE: {mse_mmse:.6f}")
print(f"MMSE is better by: {10*np.log10(mse_zf/mse_mmse):.2f} dB")