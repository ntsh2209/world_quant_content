# MScFE 620 Derivative Pricing - Group Work Project #1 Solutions

## Step 1: Put-Call Parity & Binomial Tree

### 1. Does put-call parity apply for European options? Why or why not?
Yes, put-call parity applies to European options. Put-call parity is a fundamental relationship between the price of a European call option and a European put option with the same underlying asset, strike price, and expiration date. This relationship is derived from the principle of no-arbitrage. If we consider two portfolios: Portfolio A, consisting of a European call option and cash equal to the present value of the strike price ($K e^{-rT}$), and Portfolio B, consisting of a European put option and one share of the underlying stock ($S_0$), both portfolios will have the same value at expiration, which is $\max(S_T, K)$. Since they have the same payoff regardless of the stock price at maturity, they must have the same value today to prevent arbitrage opportunities.

### 2. Rewrite put-call parity to solve for the call price.
The standard put-call parity formula is $C + K e^{-rT} = P + S_0$. To solve for the call price ($C$), we rearrange the equation as follows:
$$C = P + S_0 - K e^{-rT}$$
This formula indicates that the price of a European call option is equivalent to the price of a European put option plus the current stock price, minus the present value of the strike price.

### 3. Rewrite put-call parity to solve for the put price.
Using the same standard put-call parity formula $C + K e^{-rT} = P + S_0$, we can solve for the put price ($P$) by rearranging the terms:
$$P = C + K e^{-rT} - S_0$$
This relationship shows that the price of a European put option is equal to the price of a European call option plus the present value of the strike price, minus the current stock price.

### 4. Does put-call parity apply for American options? Why or why not?
For American options, the standard put-call parity equality does not strictly hold because of the possibility of early exercise. Instead, it is expressed as a set of inequalities:
$$S_0 - K \leq C - P \leq S_0 - K e^{-rT}$$
The reason for this is that American options can be exercised at any time before expiration. For a non-dividend-paying stock, it is never optimal to exercise an American call early, so its value is the same as a European call. However, it can be optimal to exercise an American put early if the stock price is sufficiently low. This added flexibility makes the American put more valuable than its European counterpart, thus breaking the strict equality of the standard put-call parity.

### 5. Price an ATM European call and put using a binomial tree.
Using the parameters $S_0 = 100, K = 100, r = 5\%, \sigma = 20\%, T = 0.25$ years, and choosing $N = 100$ steps for a reliable estimate:
- **European Call Price:** $4.61
- **European Put Price:** $3.36

**Process Description:**
The binomial tree model discretizes the time to expiration into $N$ steps. At each step, the stock price can move up by a factor $u = e^{\sigma \sqrt{\Delta t}}$ or down by $d = 1/u$. The risk-neutral probability of an upward move is $p = \frac{e^{r \Delta t} - d}{u - d}$. We first build the stock price tree forward from $t=0$ to $T$. Then, we calculate the option's payoff at maturity ($t=T$) for each node. Finally, we work backward through the tree, calculating the option value at each preceding node as the discounted expected value under the risk-neutral measure. We chose $N=100$ steps because it provides a good balance between computational efficiency and convergence to the Black-Scholes price.

### 6. Compute the Greek Delta for the European call and European put at time 0.
- **European Call Delta:** 0.5693
- **European Put Delta:** -0.4307

**Comparison and Comment:**
The Delta of the call option is positive (0.5693), while the Delta of the put option is negative (-0.4307). Delta represents the sensitivity of the option price to a change in the underlying stock price. A call delta of 0.5693 means that for every $1 increase in the stock price, the call option price is expected to increase by approximately $0.57. Conversely, a put delta of -0.4307 means the put price will decrease by $0.43 for the same $1 increase in the stock. It is important to note that $\Delta_{call} - \Delta_{put} = 0.5693 - (-0.4307) = 1.00$, which is consistent with the theoretical relationship derived from put-call parity.

### 7. Compute the sensitivity of previous put and call option prices to a 5% increase in volatility.
- **New Volatility:** 25%
- **New European Call Price:** $5.59
- **New European Put Price:** $4.34
- **Change in Call Price (Vega):** $0.98
- **Change in Put Price (Vega):** $0.98

**Comment on Impact:**
Both the call and put option prices increased by the same amount ($0.98) when the volatility increased from 20% to 25%. This is because Vega, the sensitivity to volatility, is always positive for both calls and puts. Higher volatility increases the probability of the option ending up deep in-the-money, which increases its current value. The identical change in both prices is also consistent with put-call parity, as the difference $C-P$ depends only on $S_0, K, r,$ and $T$, not on volatility.

### 8. Repeat Q5 for American style options.
- **American Call Price:** $4.61
- **American Put Price:** $3.47

**Comment:**
The American call price is identical to the European call price ($4.61) because, for a non-dividend-paying stock, early exercise of a call option is never optimal. However, the American put price ($3.47) is higher than the European put price ($3.36). This reflects the added value of the early exercise feature, which can be optimal for a put option when the stock price is very low and the interest earned on the strike price outweighs the potential for further stock price decreases.

### 9. Repeat Q6 for American style options.
- **American Call Delta:** 0.5693
- **American Put Delta:** -0.4498

**Comment:**
The American call delta remains the same as the European call delta because their prices are identical. However, the American put delta (-0.4498) is slightly more negative than the European put delta (-0.4307). This indicates that the American put is more sensitive to changes in the underlying stock price, particularly because the early exercise boundary makes the option behave more like the underlying stock as it moves deeper into the money.

### 10. Repeat Q7 for American style options.
- **New American Call Price (25% vol):** $5.59
- **New American Put Price (25% vol):** $4.45
- **Change in American Call Price:** $0.98
- **Change in American Put Price:** $0.98

**Comment:**
Similar to the European case, both American options increase in value with higher volatility. The increase for the American call is identical to the European call. The American put also increases by approximately the same amount as the European put, showing that volatility remains a significant driver of value for American-style options.

### 11. Show European call and put satisfy put-call parity.
Using the formula $C - P = S_0 - K e^{-rT}$:
- $C - P = 4.61 - 3.36 = 1.25$
- $S_0 - K e^{-rT} = 100 - 100 e^{-0.05 \times 0.25} = 1.24$
The difference is $0.01$, which is within the rounding limit of the nearest cent.

### 12. Show American call and put satisfy put-call parity.
Using the inequality $S_0 - K \leq C - P \leq S_0 - K e^{-rT}$:
- $S_0 - K = 100 - 100 = 0.00$
- $C - P = 4.61 - 3.47 = 1.14$
- $S_0 - K e^{-rT} = 1.24$
Since $0.00 \leq 1.14 \leq 1.24$, the inequality is satisfied.

### 13. Confirm European call <= American call.
- **European Call:** $4.61
- **American Call:** $4.61
The European call is equal to the American call. This is always the case for non-dividend-paying stocks because early exercise of a call option is never optimal.

### 14. Confirm European put <= American put.
- **European Put:** $3.36
- **American Put:** $3.47
The European put is less than the American put. This is because the American put has the added value of the early exercise feature, which can be optimal when the stock price is low.

---

## Step 2: Trinomial Tree

### 15. Price European Call using trinomial tree for 5 strikes.
Using the parameters $S_0 = 100, r = 5\%, \sigma = 20\%, T = 0.25$ years, and choosing $N = 100$ steps:

| Strike (K) | Moneyness (K/S0) | European Call Price |
| :--- | :--- | :--- |
| 90 | 90% | $11.67 |
| 95 | 95% | $7.71 |
| 100 | 100% | $4.61 |
| 105 | 105% | $2.48 |
| 110 | 110% | $1.19 |

**Comment on the trend:**
As the strike price increases, the call option price decreases. This is because a higher strike price makes it less likely for the option to end up in-the-money at expiration. For a call option, the payoff is $\max(S_T - K, 0)$, so a larger $K$ directly reduces the potential payoff for any given stock price $S_T$.

### 16. Repeat Q15 for European Put.

| Strike (K) | Moneyness (K/S0) | European Put Price |
| :--- | :--- | :--- |
| 90 | 90% | $0.55 |
| 95 | 95% | $1.53 |
| 100 | 100% | $3.36 |
| 105 | 105% | $6.17 |
| 110 | 110% | $9.83 |

**Comment on the trend:**
As the strike price increases, the put option price increases. This is because a higher strike price makes it more likely for the option to end up in-the-money at expiration. For a put option, the payoff is $\max(K - S_T, 0)$, so a larger $K$ directly increases the potential payoff for any given stock price $S_T$.

### 17. Repeat Q15 for American Call.

| Strike (K) | Moneyness (K/S0) | American Call Price |
| :--- | :--- | :--- |
| 90 | 90% | $11.67 |
| 95 | 95% | $7.71 |
| 100 | 100% | $4.61 |
| 105 | 105% | $2.48 |
| 110 | 110% | $1.19 |

**Comment:**
The American call prices are identical to the European call prices for all strikes. This confirms that for a non-dividend-paying stock, early exercise of an American call option is never optimal.

### 18. Repeat Q16 for American Put.

| Strike (K) | Moneyness (K/S0) | American Put Price |
| :--- | :--- | :--- |
| 90 | 90% | $0.56 |
| 95 | 95% | $1.57 |
| 100 | 100% | $3.47 |
| 105 | 105% | $6.42 |
| 110 | 110% | $10.33 |

**Comment:**
The American put prices are consistently higher than the European put prices. This difference represents the value of the early exercise feature. As the strike price increases (making the put more in-the-money), the value of early exercise also increases.

### 19-22. Graphs
*Graphs are provided as separate attachments.*
- **Graph #1:** European call and put prices versus stock prices.
- **Graph #2:** American call and put prices versus stock prices.
- **Graph #3:** European and American call prices versus strike.
- **Graph #4:** European and American put prices versus strike.

### 23. Check put-call parity for trinomial European options.
Using the formula $C - P = S_0 - K e^{-rT}$:

| Strike (K) | C - P | S0 - K * exp(-rT) | Difference |
| :--- | :--- | :--- | :--- |
| 90 | 11.67 - 0.55 = 11.12 | 100 - 90 * exp(-0.05 * 0.25) = 11.12 | 0.00 |
| 95 | 7.71 - 1.53 = 6.18 | 100 - 95 * exp(-0.05 * 0.25) = 6.18 | 0.00 |
| 100 | 4.61 - 3.36 = 1.25 | 100 - 100 * exp(-0.05 * 0.25) = 1.24 | 0.01 |
| 105 | 2.48 - 6.17 = -3.69 | 100 - 105 * exp(-0.05 * 0.25) = -3.69 | 0.00 |
| 110 | 1.19 - 9.83 = -8.64 | 100 - 110 * exp(-0.05 * 0.25) = -8.63 | 0.01 |

**Comment:**
The European call and put prices satisfy put-call parity within sensible rounding limits. The small differences (0.01) are due to rounding the option prices to the nearest cent.

### 24. Check put-call parity for trinomial American options.
Using the inequality $S_0 - K \leq C - P \leq S_0 - K e^{-rT}$:

| Strike (K) | S0 - K | C - P | S0 - K * exp(-rT) | Satisfied? |
| :--- | :--- | :--- | :--- | :--- |
| 90 | 10.00 | 11.67 - 0.56 = 11.11 | 11.12 | Yes |
| 95 | 5.00 | 7.71 - 1.57 = 6.14 | 6.18 | Yes |
| 100 | 0.00 | 4.61 - 3.47 = 1.14 | 1.24 | Yes |
| 105 | -5.00 | 2.48 - 6.42 = -3.94 | -3.69 | Yes |
| 110 | -10.00 | 1.19 - 10.33 = -9.14 | -8.63 | Yes |

**Comment:**
The American call and put prices satisfy the put-call parity inequalities. In all cases, $C - P$ is between the lower bound ($S_0 - K$) and the upper bound ($S_0 - K e^{-rT}$). This confirms that the American put is more valuable than the European put, which pulls the $C - P$ value lower than the European parity value.

---

## Step 3: Real-World Questions

### 25. Dynamic Delta Hedging
**Parameters:** $S_0 = 180, r = 2\%, \sigma = 25\%, T = 0.5$ years, $K = 182, N = 3$ steps.
- $\Delta t = 0.5 / 3 = 0.1667$
- $u = e^{0.25 \sqrt{0.1667}} = 1.1075$
- $d = 1/u = 0.9030$
- $p = \frac{e^{0.02 \times 0.1667} - 0.9030}{1.1075 - 0.9030} = 0.4908$

#### a. Price a European Put option using a 3-step binomial tree.
The stock price tree and option value tree are as follows:

**Stock Price Tree:**
- $t=0: 180.00$
- $t=1: 199.34, 162.54$
- $t=2: 220.76, 180.00, 146.77$
- $t=3: 244.48, 199.34, 162.54, 132.52$

**Option Value Tree (European Put):**
- $t=3: 0.00, 0.00, 19.46, 49.48$
- $t=2: 0.00, 9.88, 34.63$
- $t=1: 5.01, 22.41$
- $t=0: 13.82$

**European Put Price:** $13.82

#### b. Describe the Delta hedging process for one path.
**Path chosen:** $S_0 \to S_d \to S_{du} \to S_{dud}$ (Down, Up, Down)
- $t=0: S_0 = 180.00, \Delta_0 = -0.4726$
- $t=1: S_d = 162.54, \Delta_1 = -0.7447$
- $t=2: S_{du} = 180.00, \Delta_2 = -0.5288$
- $t=3: S_{dud} = 162.54, \text{Payoff} = 19.46$

**Hedging Process (Seller of Put):**
As the seller of the put option, we are short the put. To hedge this position, we must maintain a portfolio that is delta-neutral. Since the put has a negative delta, being short the put means we have a positive delta exposure. To offset this, we must sell (short) $\Delta$ units of the underlying stock.

**Cash Account Table (Path: D-U-D):**

| Step | Stock Price | Delta ($\Delta$) | Shares to Buy/Sell | Cash Flow (Stock) | Interest | Cash Balance |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | 180.00 | -0.4726 | Sell 0.4726 | +85.07 | 0.00 | +85.07 |
| 1 | 162.54 | -0.7447 | Sell 0.2721 | +44.23 | +0.28 | +129.58 |
| 2 | 180.00 | -0.5288 | Buy 0.2159 | -38.86 | +0.43 | +91.15 |
| 3 | 162.54 | -1.0000 | Buy 0.4712 | -76.59 | +0.30 | +14.86 |

*Note: At $t=3$, the option is exercised for $19.46. The final cash balance of $14.86 plus the interest earned is used to offset the payoff.*

### 26. American Put Hedging (25 steps)
- **American Put Price (25 steps):** $13.04
- **Delta at $t=0$:** -0.4735

**Comment on the Delta hedging process:**
The delta hedging process for an American put is similar to the European case, but with one key difference: the delta must account for the possibility of early exercise. In the binomial tree, the delta at each node is calculated using the option values that already incorporate the early exercise decision. As the stock price falls and approaches the early exercise boundary, the delta of the American put will approach -1 more quickly than the European put. This means the hedger must sell more of the underlying stock sooner to remain delta-neutral.

### 27. Asian ATM Put
- **Asian ATM Put Price (15 steps):** $6.79

**Comment and Comparison:**
The Asian ATM put price ($6.79) is significantly lower than the American put price ($13.04). This is because the payoff of an Asian option depends on the average price of the underlying asset over the life of the option, rather than the price at a single point in time (maturity or exercise). Averaging reduces the volatility of the payoff, as extreme price movements are smoothed out. Since option value is positively correlated with volatility, the reduced volatility of the average price leads to a lower option premium. Additionally, the Asian option is path-dependent, making it more complex to hedge than a standard American or European option.
