# 5G Wireless Signal Processing — Python

I built this project to bridge the gap between my wireless engineering
theory and practical Python implementation. Coming from an internship
at Qualcomm Frankfurt where I worked on 5G modem testing and protocol
stack validation, I wanted to make sure my simulation and coding skills
matched my hardware experience.

Every file in this repo is built around a real wireless engineering
concept — not generic programming exercises.

## What this covers

### Fundamentals
Basic 5G calculations — unit conversions, wavelength, frequency.
The building blocks before jumping into system level simulation.

### Link and Channel
Shannon capacity, free space path loss at mmWave frequencies and
3GPP TDL channel models. Understanding theoretical limits before
designing real systems.

### Signal Processing
FFT, spectral analysis and filtering — the core tools for any
wireless engineer working with real signals.

### Simulations
Monte Carlo BER simulation for BPSK and channel simulation.
Moving from theoretical formulas to statistical results through
repeated random experiments.

### Adaptive Systems
AMC selector based on 5G NR MCS thresholds and OFDM system
implementation. The kind of algorithms that run inside every
modern base station and UE.

### Numpy and Math
Linear algebra for MIMO, matrix operations for beamforming.
The mathematical foundation behind massive MIMO in 5G NR.

### Data and Plots
Matplotlib visualizations for signal analysis and measurement data.
Because in wireless engineering, if you cannot plot it clearly
you cannot explain it.

### Python for Engineers
This is where I practiced core Python concepts — but always using
wireless problems instead of generic examples.

**Functions** — Shannon capacity, dBm conversion, power combining.
Writing reusable functions for calculations I kept repeating made
me realise how much cleaner simulation code can be.

**OOP** — antenna classes, signal encapsulation with property
validation, channel inheritance with AWGN and Rayleigh fading models.
Writing a Channel base class with child classes made inheritance
click for me in a way that generic examples never did.

**Data structures** — list comprehension, sets, dictionaries applied
to subcarrier allocation, TDL channel models and measurement datasets.
No boring generic examples — every exercise has an RF context.

## Why I built this

During my Qualcomm internship I realized that wireless engineers
who can both understand RF concepts deeply and implement them in
code are rare. Most engineers are strong on one side but weak on
the other. I wanted to be strong on both.

This project is my attempt to get there.

## Tech Stack
- Python 3
- NumPy, SciPy, Matplotlib
- Based on 3GPP 5G NR standards

## Status
Ongoing — actively adding new modules while completing my MSc
in Wireless Engineering at Hochschule Darmstadt.

## Author
Pujan Thapa Magar
MSc Wireless Engineering — Hochschule Darmstadt
Qualcomm Frankfurt — 5G Modem Testing Intern