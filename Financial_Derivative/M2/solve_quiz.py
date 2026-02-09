import numpy as np

def binomial_american_option(S0, K, T, r, u, d, N, option_type='call'):
    dt = T / N
    p = (np.exp(r * dt) - d) / (u - d)
    
    # Initialize asset prices at maturity
    S = np.zeros(N + 1)
    for j in range(N + 1):
        S[j] = S0 * (u**j) * (d**(N - j))
    
    # Initialize option values at maturity
    if option_type == 'call':
        V = np.maximum(S - K, 0)
    else:
        V = np.maximum(K - S, 0)
    
    # Backward induction
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            S_curr = S0 * (u**j) * (d**(i - j))
            V_hold = np.exp(-r * dt) * (p * V[j + 1] + (1 - p) * V[j])
            if option_type == 'call':
                V_exercise = np.maximum(S_curr - K, 0)
            else:
                V_exercise = np.maximum(K - S_curr, 0)
            V[j] = np.maximum(V_hold, V_exercise)
            
    return V[0]

def calculate_delta(S0, K, T, r, u, d, N, option_type='call', path=''):
    # This is a bit more complex as we need the delta at a specific node
    # Delta_n = (V_up - V_down) / (S_up - S_down)
    # For Question 4: Delta_2^{dd}
    # For Question 8: Delta_5^{ddddd}
    
    dt = T / N
    p = (np.exp(r * dt) - d) / (u - d)
    
    # We need the full tree of option values
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
            
    # Delta at node (n, j) is (V[n+1][j+1] - V[n+1][j]) / (S[n+1][j+1] - S[n+1][j])
    # Path 'dd' means we go down twice. 
    # S0 -> S0*d (node 1,0) -> S0*d*d (node 2,0)
    # Delta_2^{dd} is the delta at node (2,0)
    
    def get_node_from_path(path):
        n = len(path)
        j = path.count('u')
        return n, j

    n, j = get_node_from_path(path)
    delta = (V_tree[n+1][j+1] - V_tree[n+1][j]) / (S_tree[n+1][j+1] - S_tree[n+1][j])
    return delta

# Question 2
q2_price = binomial_american_option(36, 31, 5, 0, 1.5, 1/1.5, 5, 'call')
print(f"Q2 Price: {q2_price}")

# Question 4
q4_delta = calculate_delta(45, 45, 5, 0, 1.2, 1/1.2, 5, 'call', 'dd')
print(f"Q4 Delta: {q4_delta}")

# Question 6
q6_price = binomial_american_option(45, 105, 5, 0, 1.2, 1/1.2, 5, 'call')
print(f"Q6 Price: {q6_price}")

# Question 8
# Delta_5^{ddddd} is at the very end? 
# Wait, Delta_n is usually defined at step n. 
# Delta_5 at step 5 would require values at step 6. But T=5=N.
# Usually Delta_n is the hedge ratio to be held from time n to n+1.
# So Delta_5 would be at the last step.
# Let's check if the question implies Delta at the node reached by ddddd.
try:
    q8_delta = calculate_delta(45, 45, 5, 0, 1.2, 1/1.2, 5, 'call', 'ddddd')
    print(f"Q8 Delta: {q8_delta}")
except IndexError:
    print("Q8: Cannot calculate Delta at step 5 with N=5")

# Question 10
q10_price = binomial_american_option(36, 31, 5, 0, 1.5, 1/1.5, 5, 'put')
print(f"Q10 Price: {q10_price}")

# Question 16
q16_price = binomial_american_option(45, 45, 5, 0, 1.2, 1/1.2, 5, 'put')
print(f"Q16 Price: {q16_price}")
