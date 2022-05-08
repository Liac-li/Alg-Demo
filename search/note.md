# Search

#### Beam Search

To search the optimal strategy from candidate states, we can apply *greedy search*, *exhaustive search* or generalized greedy search *beam search*(with beam width $k$)

- Greedy search choose the best 1 in each searching step
- Beam search: record the best $k$ choices in each searching step, but in greedy strategy

> not expand the search tree to $k^d$, only record the best $k$ items at each depth


#### Viterbi Algorithm

For inference in HMM model, the target is:

$$
    \max P(s_{1:t}|o_{1:t})
$$

apply Markov assumption:

$$
    \begin{aligned}
    P(s_{1:t} | o_{1:t}) &= \frac{P(o_{1:t}|s_{1:t})P(s_{1:t})}{P(o_{1:t})}\\
        &\propto \prod_{i} P(o_{i}|s_{i}) \prod_{i} P(s_i|s_{i-1})\\
        &= \prod_i^t P(o_i|s_i) P(s_i | s_{i-1}) \quad\text{Learned in HMM}
    \end{aligned}
$$

to search a optimal path from the start hidden state $s_i$ to $s_t$ is the target. With DP, if now we know the best path **with prob** of time step $t$ to hidden state $j$, donate the probability as viterbi path:
$$
    V_t(j) = \max P(s_{1:t-1};O_{1:t}; s_t = j|\lambda)
$$

consider the $V_{t+1}(j)$

$$
    \begin{aligned}
        V_{t+1}(j) &= \max P(s_{1:t}; o_{1:t+1}; s_{t+1} = j | \lambda)\\
            &= \max P(s_{t+1}=j , o_{t+1}| V_t(i), \lambda) P(V_t(i)) \quad \text{1 step Markov chain}\\
            &= \max_i V_t(i) P(s_{t+1} = j |s_{t} = i) \cdot P(o_{t+1}|s_{t+1})\\
            &= \max_i V_t(i)\cdot a_{ij} \cdot b_{j}(o_{t+1})
    \end{aligned}
$$

thus we get the recurrence relation of DP, the target is get $\argmax_{p = (i_1, i_2, ..., i_N)} V_{t}(i)$ 

use a time step with tags counting matrix, $X \in \mathbb{R}^{T\times N}$ representing the $V$, on each time step $t$ (row of $X$) is only related with last time step $t-1$. We can **update $X$ row by row**, which takes time $O(N^2 T)$ with recording path while updating