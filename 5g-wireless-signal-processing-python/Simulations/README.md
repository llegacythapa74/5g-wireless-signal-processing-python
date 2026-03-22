# Monte Carlo BER Simulation — BPSK

This exercise helped me understand how Bit Error Rate is estimated
in practice using Monte Carlo simulation instead of just using the
theoretical formula.

The idea is to simulate 1000 BPSK transmissions, add real Gaussian
noise to each symbol, detect the received bits and count how many
were wrong.

## How it works

1. Generate 1000 random bits (0 or 1)
2. Map each bit to a BPSK symbol — bit 0 becomes +1, bit 1 becomes -1
3. Add Gaussian noise to each symbol based on the SNR
4. Detect the received bit — if received signal > 0 then bit=0, else bit=1
5. Compare transmitted and received bits, count the errors
6. BER = total errors / 1000

## What I learned

At SNR = 10 dB the BER is very low, which makes sense because
the noise power is much smaller than the signal power. Lowering
the SNR increases errors quickly — this is the whole point of
link budget design in 5G.

## Author
Pujan Thapa Magar