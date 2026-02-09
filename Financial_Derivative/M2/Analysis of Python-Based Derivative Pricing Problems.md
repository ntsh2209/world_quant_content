# Analysis of Python-Based Derivative Pricing Problems

This report details the rigorous re-evaluation of the numerical problems presented in the quiz. Each problem was solved using a discrete-time binomial model, specifically the Cox-Ross-Rubinstein framework adapted for American-style options. The calculations assume a risk-neutral environment where the underlying asset price follows a binomial process.

### Question 2: Valuation of an American Call Option
The first numerical task required computing the price of an American call option with an initial stock price ($S_0$) of 36, a strike price ($K$) of 31, and a time to maturity ($T$) of 5 periods. Given the parameters $u = 1.5$, $d = 1/u$, and a risk-free rate ($r$) of 0, the risk-neutral probability ($p$) is calculated as 0.4. By constructing a 5-step binomial tree and applying backward induction while checking for early exercise at each node, the fair value of the option is determined to be **14.7315**.

### Question 4: Sensitivity Analysis via Delta
Question 4 focused on the Delta ($\Delta$) of an American call option at a specific node in the tree. The parameters were $S_0 = 45, K = 45, u = 1.2, d = 1/u$, and $T = 5$. The objective was to find the Delta at the node reached by two consecutive downward moves ("dd"). The Delta at any non-terminal node is the ratio of the change in option price to the change in stock price for the subsequent up and down moves. Based on the tree values at step 3 branching from the "dd" node, the Delta is **0.1622**.

### Question 6: Deep Out-of-the-Money Call Valuation
In Question 6, the model was applied to an American call with a significantly higher strike price ($K = 105$) relative to the initial price ($S_0 = 45$). Despite the option being deep out-of-the-money initially, the volatility implied by $u = 1.2$ over 5 periods results in a small but non-zero probability of the option expiring in-the-money. The backward induction process yields a current option price of **0.1353**.

### Question 8: Terminal Delta Calculation
Question 8 requested the Delta at the terminal node reached by five consecutive downward moves ("ddddd"). At maturity ($T=N=5$), the Delta of a call option is binary: it is 1 if the asset price exceeds the strike price and 0 otherwise. For the given path, the final stock price is approximately 18.08, which is well below the strike price of 45. Consequently, the Delta at this node is **0**.

### Question 10: Valuation of an American Put Option
The valuation of an American put option was performed using the same parameters as Question 2 ($S_0 = 36, K = 31, u = 1.5, d = 1/u, T = 5, r = 0$). Unlike call options on non-dividend-paying stocks, American puts often warrant early exercise. The model accounts for this by taking the maximum of the continuation value and the intrinsic value at every node. The resulting price is **9.7315**.

### Question 16: Multi-Period Put Valuation
The final Python-based problem involved an American put with a much higher number of steps ($N = 50$) and a corresponding time to maturity ($T = 50$). With $S_0 = 45, K = 45, u = 1.2, d = 1/u$, and $r = 0$, the increased number of periods allows for a more granular approximation of the price. The 50-step binomial tree calculation results in an option price of **21.53**.

| Question | Problem Type | Key Parameters | Final Answer |
| :--- | :--- | :--- | :--- |
| 2 | American Call Price | $S_0=36, K=31, N=5$ | **14.7315** |
| 4 | Delta ($\Delta_2^{dd}$) | $S_0=45, K=45, N=5$ | **0.1622** |
| 6 | American Call Price | $S_0=45, K=105, N=5$ | **0.1353** |
| 8 | Delta ($\Delta_5^{ddddd}$) | $S_0=45, K=45, N=5$ | **0** |
| 10 | American Put Price | $S_0=36, K=31, N=5$ | **9.7315** |
| 16 | American Put Price | $S_0=45, K=45, N=50$ | **21.53** |
