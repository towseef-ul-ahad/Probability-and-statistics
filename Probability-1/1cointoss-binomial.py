'''
coin has prob p of falling heads take p=0.3 and n=1000 and simulate and show 
number of heads as fxn of n. repeat for p=0.03
'''
import random
import numpy as np
import matplotlib.pyplot as plt

n = 1000
x_values = np.arange(1, n+1)

def simulate(p):
    head_count = np.zeros(n)
    count = 0

    for i in range(n):
        choice = random.random()

        if choice < p:
            count += 1

        head_count[i] = count

    print(f"p = {p}: Final number of heads = {count}")
    print(f"Empirical probability = {count/n:.4f}")

    return head_count

# Simulations
heads_03 = simulate(0.3)
heads_003 = simulate(0.03)

# Plotting
plt.figure(figsize=(11, 6))

plt.plot(x_values, heads_03, label='p = 0.3')
plt.plot(x_values, heads_003, label='p = 0.03')

# Expected number of heads
plt.plot(x_values, 0.3*x_values, '--', label='Expected heads (p=0.3)')
plt.plot(x_values, 0.03*x_values, '--', label='Expected heads (p=0.03)')

plt.xlabel("Number of tosses (n)")
plt.ylabel("Cumulative number of heads")
plt.title("Number of Heads vs Number of Coin Tosses")

plt.legend()
plt.grid()
plt.show()