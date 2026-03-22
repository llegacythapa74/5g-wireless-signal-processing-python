"""
Measurement Dataset using Dictionaries
Author: Pujan Thapa Magar

Practicing Python dictionaries and lists by simulating
a dataset of 100 SNR/BER measurement samples.
"""

import random

samples = []

for i in range(100):
    snr = random.uniform(-5, 30)
    ber = 0.5 * (10 ** (-snr / 10))
    sample = {
        "sample_id": i,
        "snr_db": snr,
        "ber": ber
    }
    samples.append(sample)

# find the sample with lowest BER
best_sample = min(samples, key=lambda x: x["ber"])

print("Best sample (lowest BER):")
print("Sample ID:", best_sample["sample_id"])
print("SNR (dB):", round(best_sample["snr_db"], 2))
print("BER:", best_sample["ber"])