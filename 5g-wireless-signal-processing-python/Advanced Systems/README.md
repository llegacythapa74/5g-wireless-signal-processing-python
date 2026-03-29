# Advanced Systems

This folder is where things get more interesting. I built three simulations
that connect the theoretical concepts from lectures to actual working code.
Each one covers a core part of how modern 5G systems work under the hood.

---

## What is inside

### 1. `modulator_demodulator.py` — BPSK, QPSK and 16QAM Communication System

This was my attempt to build a complete communication chain from scratch —
transmitter, channel and receiver all in one place. I wanted to understand
not just what modulation is but how the bits actually become complex symbols,
travel through a noisy channel and get decoded back on the other side.

Supports three modulation schemes:
| Scheme   | Bits per Symbol | Minimum SNR needed |
|----------|-----------------|--------------------|
| BPSK     | 1               | Low (~6 dB)        |
| QPSK     | 2               | Medium (~10 dB)    |
| 16-QAM   | 4               | High (~15 dB)      |

Also includes AWGN and Rayleigh fading channel models.
The simulation sweeps SNR from 0 to 20 dB and compares simulated BER
against the theoretical formula — good way to verify the implementation is correct.

---

### 2. `antenna_array.py` — Phased Array Beamforming Simulator

I built this to understand how a 5G base station points its beam toward a user
without physically moving the antenna. The trick is giving each antenna element
a slightly different phase shift — this is called a steering vector.

The beam pattern method then sweeps all angles from -90 to +90 degrees and
shows where the beam is strong and where it cancels out. With 10 antennas
the peak magnitude at 0 degrees comes out exactly 10 — all elements perfectly
in phase. This is the mathematical core of mmWave beamforming in 5G NR.

---

### 3. `link_budget.py` — Free Space Link Budget Calculator

This one simulates how much signal survives after travelling through open space.
I wanted to understand the tradeoff between distance, frequency and SNR that
every RF engineer has to deal with when designing a wireless link.

Given a distance it calculates the received SNR. Given a target SNR it works
backwards and finds the maximum distance where communication is still possible.
Tested at 75 GHz mmWave — the numbers show exactly why mmWave has such
short range compared to sub-6 GHz.

| Method              | Input        | Output          |
|---------------------|--------------|-----------------|
| `calculate_snr()`   | Distance (m) | SNR (dB)        |
| `find_max_distance()` | Target SNR (dB) | Distance (km) |

---

## Concepts covered

- Modulation and demodulation (BPSK, QPSK, 16QAM)
- AWGN and Rayleigh fading channel models
- Bit Error Rate (BER) simulation vs theoretical
- Phased array steering vectors and beam patterns
- Free Space Path Loss (FSPL)
- SNR calculation and link budget analysis

---

## How to run

Each file is standalone, just run directly:
```bash
python modulator_demodulator.py
python antenna_array.py
python link_budget.py
```

No external libraries needed — only `math`, `cmath` and `random` from
Python standard library.

---

## Author
Pujan Thapa Magar

## Part of
[5g-wireless-signal-processing-python](https://github.com/llegacythapa74/5g-wireless-signal-processing-python)