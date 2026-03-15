import numpy as np
import matplotlib.pyplot as plt

def binomial_tree(S0, K, r, sigma, T, N, option_type='call', style='European'):
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)
    V = np.zeros((N + 1, N + 1))
    S = np.zeros((N + 1, N + 1))
    for i in range(N + 1):
        for j in range(i + 1):
            S[j, i] = S0 * (u ** (i - j)) * (d ** j)
    if option_type == 'call':
        V[:, N] = np.maximum(S[:, N] - K, 0)
    else:
        V[:, N] = np.maximum(K - S[:, N], 0)
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            continuation_value = np.exp(-r * dt) * (p * V[j, i + 1] + (1 - p) * V[j + 1, i + 1])
            if style == 'American':
                exercise_value = np.maximum(S[j, i] - K, 0) if option_type == 'call' else np.maximum(K - S[j, i], 0)
                V[j, i] = np.maximum(exercise_value, continuation_value)
            else:
                V[j, i] = continuation_value
    return V[0, 0]

# Parameters
S0_range = np.linspace(80, 120, 20)
K_range = np.linspace(80, 120, 20)
r = 0.05
sigma = 0.20
T = 0.25
N = 50

# Graph 1: European Call/Put vs Stock Price
c_euro_s = [binomial_tree(s, 100, r, sigma, T, N, 'call', 'European') for s in S0_range]
p_euro_s = [binomial_tree(s, 100, r, sigma, T, N, 'put', 'European') for s in S0_range]

plt.figure(figsize=(10, 6))
plt.plot(S0_range, c_euro_s, label='European Call')
plt.plot(S0_range, p_euro_s, label='European Put')
plt.xlabel('Stock Price (S0)')
plt.ylabel('Option Price')
plt.title('European Option Prices vs Stock Price')
plt.legend()
plt.grid(True)
plt.savefig('/home/ubuntu/graph1.png')
plt.close()

# Graph 2: American Call/Put vs Stock Price
c_amer_s = [binomial_tree(s, 100, r, sigma, T, N, 'call', 'American') for s in S0_range]
p_amer_s = [binomial_tree(s, 100, r, sigma, T, N, 'put', 'American') for s in S0_range]

plt.figure(figsize=(10, 6))
plt.plot(S0_range, c_amer_s, label='American Call')
plt.plot(S0_range, p_amer_s, label='American Put')
plt.xlabel('Stock Price (S0)')
plt.ylabel('Option Price')
plt.title('American Option Prices vs Stock Price')
plt.legend()
plt.grid(True)
plt.savefig('/home/ubuntu/graph2.png')
plt.close()

# Graph 3: European and American Call vs Strike
c_euro_k = [binomial_tree(100, k, r, sigma, T, N, 'call', 'European') for k in K_range]
c_amer_k = [binomial_tree(100, k, r, sigma, T, N, 'call', 'American') for k in K_range]

plt.figure(figsize=(10, 6))
plt.plot(K_range, c_euro_k, label='European Call')
plt.plot(K_range, c_amer_k, '--', label='American Call')
plt.xlabel('Strike Price (K)')
plt.ylabel('Option Price')
plt.title('Call Option Prices vs Strike Price')
plt.legend()
plt.grid(True)
plt.savefig('/home/ubuntu/graph3.png')
plt.close()

# Graph 4: European and American Put vs Strike
p_euro_k = [binomial_tree(100, k, r, sigma, T, N, 'put', 'European') for k in K_range]
p_amer_k = [binomial_tree(100, k, r, sigma, T, N, 'put', 'American') for k in K_range]

plt.figure(figsize=(10, 6))
plt.plot(K_range, p_euro_k, label='European Put')
plt.plot(K_range, p_amer_k, '--', label='American Put')
plt.xlabel('Strike Price (K)')
plt.ylabel('Option Price')
plt.title('Put Option Prices vs Strike Price')
plt.legend()
plt.grid(True)
plt.savefig('/home/ubuntu/graph4.png')
plt.close()
