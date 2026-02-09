import numpy as np

def american_option_price(S0, K, T, r, u, d, N, option_type='call'):
    dt = T / N
    # Risk-neutral probability p = (exp(r*dt) - d) / (u - d)
    # Note: In some contexts, r is given as a simple rate or continuous. 
    # The quiz says r=0, so exp(r*dt) = 1.
    p = (np.exp(r * dt) - d) / (u - d)
    disc = np.exp(-r * dt)
    
    # Asset prices at maturity
    S = np.zeros(N + 1)
    for j in range(N + 1):
        S[j] = S0 * (u**j) * (d**(N - j))
    
    # Option values at maturity
    if option_type == 'call':
        V = np.maximum(S - K, 0)
    else:
        V = np.maximum(K - S, 0)
    
    # Backward induction
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            S_curr = S0 * (u**j) * (d**(i - j))
            V_hold = disc * (p * V[j + 1] + (1 - p) * V[j])
            if option_type == 'call':
                V_exercise = np.maximum(S_curr - K, 0)
            else:
                V_exercise = np.maximum(K - S_curr, 0)
            V[j] = np.maximum(V_hold, V_exercise)
            
    return V[0]

def calculate_delta_at_node(S0, K, T, r, u, d, N, option_type, path):
    dt = T / N
    p = (np.exp(r * dt) - d) / (u - d)
    disc = np.exp(-r * dt)
    
    # Full tree for V and S
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
            V_hold = disc * (p * V_tree[i+1][j+1] + (1 - p) * V_tree[i+1][j])
            if option_type == 'call':
                V_exercise = np.maximum(S_tree[i][j] - K, 0)
            else:
                V_exercise = np.maximum(K - S_tree[i][j], 0)
            V_tree[i][j] = np.maximum(V_hold, V_exercise)
            
    # Determine node from path
    # Path 'dd' means down, then down.
    # Step 0: (0,0)
    # Step 1: 'd' -> (1,0)
    # Step 2: 'dd' -> (2,0)
    n = len(path)
    j = path.count('u')
    
    # Delta at node (n, j) is (V[n+1][j+1] - V[n+1][j]) / (S[n+1][j+1] - S[n+1][j])
    if n < N:
        delta = (V_tree[n+1][j+1] - V_tree[n+1][j]) / (S_tree[n+1][j+1] - S_tree[n+1][j])
        return delta
    else:
        # If at maturity, delta is usually 1 if S > K else 0 for call
        S_final = S_tree[n][j]
        if option_type == 'call':
            return 1.0 if S_final > K else 0.0
        else:
            return -1.0 if S_final < K else 0.0

print("--- Question 2 ---")
# u = 1.5, d = 1/u, T = 5 = N, r = 0, K = 31, S0 = 36. American Call.
q2 = american_option_price(36, 31, 5, 0, 1.5, 1/1.5, 5, 'call')
print(f"Q2 Result: {q2}")

print("\n--- Question 4 ---")
# u = 1.2, d = 1/u, T = 5 = N, r = 0, K = 45, S0 = 45. Delta_2^{dd}
q4 = calculate_delta_at_node(45, 45, 5, 0, 1.2, 1/1.2, 5, 'call', 'dd')
print(f"Q4 Result: {q4}")

print("\n--- Question 6 ---")
# u = 1.2, d = 1/u, T = 5 = N, r = 0, K = 105, S0 = 45. American Call.
q6 = american_option_price(45, 105, 5, 0, 1.2, 1/1.2, 5, 'call')
print(f"Q6 Result: {q6}")

print("\n--- Question 8 ---")
# u = 1.2, d = 1/u, T = 5 = N, r = 0, K = 45, S0 = 45. Delta_5^{ddddd}
q8 = calculate_delta_at_node(45, 45, 5, 0, 1.2, 1/1.2, 5, 'call', 'ddddd')
print(f"Q8 Result: {q8}")

print("\n--- Question 10 ---")
# u = 1.5, d = 1/u, T = 5 = N, r = 0, K = 31, S0 = 36. American Put.
q10 = american_option_price(36, 31, 5, 0, 1.5, 1/1.5, 5, 'put')
print(f"Q10 Result: {q10}")

print("\n--- Question 16 ---")
# u = 1.2, d = 1/u, T = 50 = N, r = 0, K = 45, S0 = 45. American Put.
q16 = american_option_price(45, 45, 50, 0, 1.2, 1/1.2, 50, 'put')
print(f"Q16 Result: {q16}")
