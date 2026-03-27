"""
Link Budget Calculator
Simulating how much signal is left after travelling through free space
and whether it is enough to communicate at a given distance.
Author: Pujan Thapa Magar
"""

import math

class LinkBudget:

    def __init__(self, TX_power, antenna_gain, freq_Hz, noise_figure):
        # storing all the system parameters, underscore means dont touch from outside
        self._TX_power = TX_power
        self._antenna_gain = antenna_gain
        self._freq_Hz = freq_Hz
        self._noise_figure = noise_figure

    def calculate_snr(self, distance_m):
        c = 3e8  # speed of light, needed for FSPL formula
        
        # FSPL in dB — signal gets weaker as distance and frequency increase
        FSPL = 20*math.log10(distance_m) + 20*math.log10(self._freq_Hz) + 20*math.log10(4*math.pi/c)
        
        # SNR = what I transmit + antenna gains - what I lost - noise at receiver
        SNR = self._TX_power + self._antenna_gain - FSPL - self._noise_figure
        return SNR

    def find_max_distance(self, target_snr):
        # rearranging the SNR formula to get FSPL first
        FSPL = self._TX_power + self._antenna_gain - self._noise_figure - target_snr
        
        # now rearranging the FSPL formula to isolate distance
        # log(d) = (FSPL - 20log(f) - 20log(4pi/c)) / 20
        log_d = (FSPL - 20*math.log10(self._freq_Hz) - 20*math.log10(4*math.pi/3e8)) / 20
        
        # 10**log_d just undoes the log to get actual distance in meters
        tar_distance = 10 ** log_d
        return tar_distance

    def __str__(self):
        # this prints nicely when I do print(object) instead of ugly memory address
        return (f"TX Power: {self._TX_power} dBm | "
                f"Antenna Gain: {self._antenna_gain} dBi | "
                f"Frequency: {self._freq_Hz/1e9} GHz | "
                f"Noise Figure: {self._noise_figure} dB")


# 75 GHz mmWave, high TX power and antenna gain to compensate for path loss
Case1 = LinkBudget(100, 100, 75e9, 25)
SNR_result = Case1.calculate_snr(120e3)
Req_distance = Case1.find_max_distance(20)

print(Case1)
print(f"SNR at 120km: {SNR_result:.2f} dB")
print(f"Max distance for 20dB SNR: {Req_distance/1e3:.2f} km")