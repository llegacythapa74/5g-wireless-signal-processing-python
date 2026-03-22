"""
Adaptive Modulation and Coding (AMC) Selector
Based on 5G NR MCS thresholds — selects the best modulation
and coding scheme for a given SNR value.

Author: Pujan Thapa Magar
"""

# SNR thresholds based on 5G NR MCS table
# Higher SNR → higher order modulation → more bits per symbol

def amc_selector(snr_values):
    for snr in snr_values:
        if snr >= 25:
            modulation = "256-QAM"
            code_rate = "3/4"
        elif snr >= 20:
            modulation = "64-QAM"
            code_rate = "2/3"
        elif snr >= 15:
            modulation = "16-QAM"
            code_rate = "1/2"
        elif snr >= 10:
            modulation = "QPSK"
            code_rate = "1/2"
        elif snr >= 5:
            modulation = "QPSK"
            code_rate = "1/3"
        else:
            modulation = "No transmission"
            code_rate = "N/A"

        print(f"SNR {snr:>2} dB → Modulation: {modulation:<10} | Code Rate: {code_rate}")


snr_db = [2, 7, 12, 17, 22, 27]
amc_selector(snr_db)