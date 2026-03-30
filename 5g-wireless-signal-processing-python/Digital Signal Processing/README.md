# Digital Signal Processing

Signal generation and bitwise operations used in wireless communications.

## What this covers
- Complex AWGN generation with proper variance scaling  
- Power validation — checking that our noise actually hits the target energy
- AND, OR, XOR operations on binary sequences
- Hamming distance — measuring bit errors between two sequences

## Why it matters
We spent time getting the sqrt(0.5) scaling right because accurate noise power is the baseline for every SNR calculation we run. If the variance is off, our whole link budget drifts.

Hamming distance is how we measure channel errors in practice. The more bits that flip, the worse the channel quality.

## Files
- `awgn_generator.py` — complex Gaussian noise with power validation
- `Bitwise_and_Hamming.py` — bitwise ops and Hamming distance