# My Paper - FAI Iteration
# Author: Muhammad Imran Riaz
# K(v) = 1 - v, fixed point = 0.5

def K(v):
    return 1 - v

def picard(v0):
    v = v0
    print("--- Picard ---")
    for i in range(10):
        v = K(v)
        print(f"Step {i+1}: {v}")
    return v

def fai(v0):
    v = v0
    print("\n--- My FAI ---")
    alpha = 0.5
    beta = 0.5
    for i in range(10):
        l = K((1 - alpha) * v + alpha * K(v))
        z = K((1 - beta) * l + beta * K(l))
        v = K(K(z))
        print(f"Step {i+1}: {v}")
        if abs(v - 0.5) < 0.000001:
            break
    return v

picard(0.2)
fai(0.2)
