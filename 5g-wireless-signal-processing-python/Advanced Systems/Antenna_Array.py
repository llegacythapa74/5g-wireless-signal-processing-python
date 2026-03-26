"""
Antenna Array Beamforming Simulator
Simulating how a phased antenna array steers its beam by applying
complex phase shifts to each element — the foundation of 5G mmWave beamforming.
Author: Pujan Thapa Magar
"""

import math
import cmath

class AntennaArray:

    def __init__(self, num_antennas: int, spacing_d: float):
        # 0.5 spacing means half wavelength apart, standard for antenna arrays
        self.num_antennas = num_antennas
        self.spacing_d = spacing_d

    def steering_vector(self, angle_deg):
        # sin() needs radians not degrees so converting first
        theta_rad = angle_deg * (math.pi / 180)
        phase_vector = []

        for n in range(self.num_antennas):
            # antenna 0 gets 0 shift, antenna 1 gets a bit, antenna 2 gets more and so on
            phase_shift = n * (math.pi * 2) * self.spacing_d * math.sin(theta_rad)

            # turning the phase angle into complex form e^(j*phase)
            phase_shift_complex = cmath.exp(1j * phase_shift)
            phase_vector.append(phase_shift_complex)

        return phase_vector

    def beam_pattern(self, angles):
        array_factor = []

        for a in angles:
            angle_vector = self.steering_vector(a)

            # summing all complex numbers — if they align the result is big, if not they cancel
            vec_sum = sum(angle_vector)

            # abs() gives me the actual strength, not the complex number
            result = abs(vec_sum)
            array_factor.append(result)

        return array_factor


# testing with 10 antennas and half wavelength spacing
array = AntennaArray(10, 0.5)

angles = list(range(-90, 91))
pattern = array.beam_pattern(angles)

# at 0 degrees magnitude should be 10 because all 10 antennas are perfectly in phase
for a, p in zip(angles, pattern):
    print(f"Angle: {a}, Magnitude: {p:.2f}")