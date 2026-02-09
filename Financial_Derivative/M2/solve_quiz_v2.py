import numpy as np

def binomial_american_option(S0, K, T, r, u, d, N, option_type='call'):
    dt = T / N
    p = (np.exp(r * dt) - d) / (u - d)
    
    V_tree = [np.zeros(i + 1) for i in range(N + 1)]
    S_tree = [np.zeros(i + 1) for i in range(N + 1)]
    
    for i in range(N + 1):
        for j in range(i + 1):
            S_tree[i][j] = S0 * (u**j) * (d**(i - j))
            
    if option_type == 'call':
        V_tree[N] = np.maximum(S_tree[N] - K, 0)
    else:
        V_tree[N] = np.maximum(K - S_tree[N], 0)
        
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            V_hold = np.exp(-r * dt) * (p * V_tree[i+1][j+1] + (1 - p) * V_tree[i+1][j])
            if option_type == 'call':
                V_exercise = np.maximum(S_tree[i][j] - K, 0)
            else:
                V_exercise = np.maximum(K - S_tree[i][j], 0)
            V_tree[i][j] = np.maximum(V_hold, V_exercise)
            
    return V_tree[0][0], V_tree, S_tree

# Question 8: Delta_5^{ddddd}
# If N=5, Delta_5 would be at the nodes of step 5. 
# But Delta is usually (V_up - V_down) / (S_up - S_down).
# This requires values at step 6. 
# Let's assume N is larger or Delta_5 refers to the delta at step 4 that leads to step 5.
# Or maybe Delta_5^{ddddd} means the delta at the node reached by 5 'd's? 
# But that's a terminal node. Delta at terminal node is usually defined as the derivative of payoff.
# For a call, it's 1 if S > K, 0 if S < K.
# Let's check the values at step 5 for Question 8 parameters.
S0, K, T, r, u, d, N = 45, 45, 5, 0, 1.2, 1/1.2, 5
S_ddddd = S0 * (d**5)
print(f"Q8: S_ddddd = {S_ddddd}, K = {K}")
# S_ddddd = 45 * (1/1.2)^5 = 45 / 2.48832 = 18.08. This is < K.
# So Delta at maturity would be 0.

# Let's check Delta_4^{dddd}
def get_delta(V_tree, S_tree, n, j):
    return (V_tree[n+1][j+1] - V_tree[n+1][j]) / (S_tree[n+1][j+1] - S_tree[n+1][j])

price, V_tree, S_tree = binomial_american_option(45, 45, 5, 0, 1.2, 1/1.2, 5, 'call')
try:
    d4_dddd = get_delta(V_tree, S_tree, 4, 0)
    print(f"Q8: Delta_4^{{dddd}} = {d4_dddd}")
except:
    pass

# Question 16: American put price
# Wait, I got 7.62 but the options are 20.12, 32.14, 21.53, 23.28.
# Let me re-read the question. 
# Question 16: u = 1.2, d = 1/u, T = 50 = N, r = 0, K = 45, S0 = 45.
# Ah! T = 50, not 5.
price_q16, _, _ = binomial_american_option(45, 45, 50, 0, 1.2, 1/1.2, 50, 'put')
print(f"Q16 Price (T=50): {price_q16}")
