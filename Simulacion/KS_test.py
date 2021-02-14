from GLC import fast_glc
import numpy as np
from scipy.stats import ks_2samp

ks_sample = fast_glc(1, 16, 5, 1)
ks_sample = [d / 16 for d in ks_sample]
u = np.random.uniform(0, 1, 16)
ans = ks_2samp(ks_sample, u)
print(ks_sample)
print(f'ks_sample is \n {ks_sample}')
print(f'uniform is \n {u}')
print(f'ks test p-value = {ans[1]}')
print('reject null hypothesis' if ans[1] < 0.05 else 'null hypothesis')
