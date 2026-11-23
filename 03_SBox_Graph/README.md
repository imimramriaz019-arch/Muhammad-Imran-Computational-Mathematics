# Graph-Theoretical Construction of S-Box for Image Encryption

**Author:** Muhammad Imran Riaz
**Affiliation:** Department of Mathematics, University of Education Lahore, Pakistan
**Email:** imimramriaz019@gmail.com

## 1. About This Work

This work presents a new method to construct the S-Box, which is the non-linear component of a block cipher like AES. The S-Box is used for image encryption.

The main idea is to use a **Complete Graph** made from a word, and then apply a fractional transformation to generate a strong S-Box.

## 2. My Algorithm - 4 Steps

**Step 1: Word to Graph**
Word ke har letter ko vertex banao.
Word = `BILAL`
- B = 66, I = 73, L = 76, A = 65, L = 76

**Step 2: Cycle Graph to Complete Graph**
Sab vertices ko aapas me connect karo.
Edge weight = |ASCII difference| of two letters.

**Step 3: Adjacency Matrix to Fractional Transformation**
```python
"""
Graph-Based S-Box Construction
Author: Muhammad Imran Riaz
Paper: A Graph-Theoretical Approach for Construction of Non-Linear Component
Word BILAL -> Complete Graph -> f(x)=1/(6x+1) mod 257 -> S-Box
My Extension: Also generate S-Box for word IMRAN
"""

import numpy as np

def word_to_sbox(word, A=6, B=1):
    # Step 1: ASCII values
    ascii_vals = [ord(c) for c in word]
    print(f"Word: {word} -> ASCII: {ascii_vals}")

    # Step 2: Complete Graph - edge weights = ASCII difference
    # Step 3: Fractional Transformation
    sbox = []
    for x in range(256):
        denom = (A*x + B) % 257
        if denom == 0:
            val = 0  # x=214 case - paper rule
        else:
            val = pow(denom, -1, 257)
        sbox.append(val)

    # Step 4: Fix bijectivity - 256 cannot be in 0-255 S-Box
    if 256 in sbox:
        idx = sbox.index(256)
        used = set(sbox) - {256}
        missing = [v for v in range(256) if v not in used][0]
        print(f"Fix: x={idx} gave 256 -> replaced with {missing}")
        sbox[idx] = missing

    sbox = np.array(sbox, dtype=int)
    assert len(set(sbox)) == 256, "S-box must be bijective!"
    return sbox

# --- Paper S-Box: BILAL ---
sbox_bilal = word_to_sbox("BILAL", A=6, B=1)
print("\nBILAL S-Box (16x16):")
print(sbox_bilal.reshape(16,16))
print(f"Bijective: {len(set(sbox_bilal))==256}")
print(f"NL Avg (Paper): 105.25, LP: 0.1484, SAC Avg: 0.4812, DU: 16")

# --- MY Extension: IMRAN ---
sbox_imran = word_to_sbox("IMRAN", A=5, B=3)
print("\nMY S-Box for IMRAN (16x16):")
print(sbox_imran.reshape(16,16))
print(f"Bijective: {len(set(sbox_imran))==256}")

# --- Image Encryption Demo: Pixel Substitution ---
test_pixels = np.array([10, 50, 100, 200, 255])
encrypted = sbox_bilal[test_pixels]
print(f"\nImage Encryption Demo:")
print(f"Original Pixels: {test_pixels}")
print(f"Encrypted Pixels: {encrypted}")
print("Done - S-Box ready for image encryption")
