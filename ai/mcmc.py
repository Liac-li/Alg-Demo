import numpy as np
import numpy.linalg as npla
import random



"""
    Only For Gaussian
"""
def gibbs_sampler(initial_point, num_samples, Conditional_sampler): 
    assert Conditional_sampler is not None

    dims = initial_point.shape[0]
    samples = np.empty([num_samples+1, dims])
    samples[0] = initial_point
    
    for i in range(1, num_samples+1):
        target_idx = random.randint(0, dims-1)

        # Sample from P(x_i | x_{j != i})
        new_x = Conditional_sampler.sample(target_idx, samples[i-1])
        samples[i] = new_x 
    
    return samples

class ConditionalSampler:
    def __init__(self, mu, cov) -> None:
        assert mu.shape[0] == cov.shape[0]
        self.mu = mu
        self.cov = cov
        self.dim = mu.shape[0]
    
    
    def sample(self, tgt_idx, cur_x):
        #P(a | b) sim to N(mu_a + sigma_ab * sigma_bb_inv * (x_b - mu_b), 
        # sigma_aa - sigma_ab * sigma_bb_inv * sigma_ba)
        mu_a = self.mu[tgt_idx]
        mu_b = np.concatenate(self.mu[:tgt_idx], self.mu[tgt_idx+1:])
        x_b = cur_x[[True if i != tgt_idx else False for i in range(self.dim)]]
        
        sigma_aa = self.sigma[tgt_idx, tgt_idx]
        sigma_ab = self.sigma[tgt_idx, [True if i != tgt_idx else False for i in range(self.dim)]]
        bb_idx = np.ones_like(self.cov)
        bb_idx[tgt_idx, :] = 0
        bb_idx[:, tgt_idx] = 0
        sigma_bb = self.sigma[bb_idx]
        
        new_mu = mu_a + sigma_ab @ npla.inv(sigma_bb) @ (x_b - mu_b) 
        new_sigma = sigma_aa - sigma_ab @ npla.inv(sigma_bb) @ np.transpose(sigma_ab)
        
        new_x = np.random.randn(self.dim) * new_sigma + new_mu
        return new_x