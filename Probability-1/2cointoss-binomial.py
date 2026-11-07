'''
comparing average number of tosses ie np in binomial with actual simulation
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
# Plotting
plt.figure(figsize=(11, 6))

plt.plot(x_values, heads_03, label='p = 0.3 or experimental')

# Expected number of heads
plt.plot(x_values, 0.3*x_values, '--', label='Expected heads or np (p=0.3)')

plt.xlabel("Number of tosses (n)")
plt.ylabel("Cumulative number of heads")
plt.title("Number of Heads vs Number of Coin Tosses")

plt.legend()
plt.grid()
plt.show()