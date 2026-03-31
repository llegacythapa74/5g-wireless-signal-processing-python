"""
BPSK Bit Error Rate Analysis
============================
Theoretical BER calculation for Binary Phase Shift Keying over AWGN channel.
Finds the SNR threshold where reliable communication begins (BER < 1e-5).

Author: Pujan Thapa Magar
Date: 2026-03-31

Theory:
-------
BPSK transmits bits as +1 or -1. The theoretical error probability is:

    BER = 0.5 * erfc(sqrt(Eb/N0))

where Eb/N0 is the SNR per bit (linear scale). The erfc decays rapidly—BER 
drops from 10^-3 to 10^-6 with just 3 dB more SNR. Systems target BER < 1e-5 
as the "reliable communication" threshold.
"""

import numpy as np
from scipy.special import erfc

snr_db = np.arange(-5, 30, 0.5)
SNR_linear = 10**(snr_db / 10)

# Theoretical BPSK BER formula
BER = 0.5 * erfc(np.sqrt(SNR_linear))

# Getting first SNR where BER drops below 1e-5
indices = np.where(BER < 1e-5)[0]

if len(indices) > 0:
    first_index = indices[0]
    snr_threshold = snr_db[first_index]
    print(f"BER drops below 1e-5 at SNR = {snr_threshold} dB")
    print(f"BER value at this point: {BER[first_index]:.2e}")
else:
    print("BER never drops below 1e-5 in the given SNR range")