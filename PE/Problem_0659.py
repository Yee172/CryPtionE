# Let P(k) be the largest prime that divides any two
# successive terms of the sequence n^{2} + k^{2}.
# Find the last 18 digits of \sum_{k = 1}^{10000000} P(k)
# ----------------------------------------------------
# Analysis: brute force
#           p | n^{2} + k^{2}
#           p | (n + 1)^{2} + k^{2}
#              => p | 2 n + 1
#              => p | (2 n + 1)^{2}
#              => p | 4 n^{2} + 4 n + 1
#           p | n^{2} + k^{2}
#              => p | 4 n^{2} + 4 k^{2}
#              => p | 4 n + 1 - 4 k^{2}
#           p | 2 n + 1
#              => p | 4 n + 2
#              => p | 1 + 4 k^{2}
#           We only have to find the sum of the largest prime factor of 1 + 4 k^{2}
#               1 + 4 k^{2} | 1 + 4 (k + m)^{2}
#           <=> 1 + 4 k^{2} | 1 + 4 k^{2} + 4 m (m + 2 k)
#           <=> 1 + 4 k^{2} | m (m + 2 k)
#           <=> 1 + 4 k^{2} | m or 1 + 4 k^{2} | m + 2 k (in the case of 1 + 4 k^{2} is a prime number)
#           <=> m = n (1 + 4 k^{2}) or m = n (1 + 4 k^{2}) - 2 k, \forall n \in \N
#              => 1 + 4 k^{2} | 1 + 4 (n (1 + 4 k^{2}) \pm k)^{2}, \forall n \in \N

2c53279a8eb4e818b627433c99c1228514f698cf53263b5431d73df8113f4acec104286152e90661bca0e3077c90df03296c96ad6e3a78dc78e0fc4d224c6594806157d7c94f831ce86fab5a9064e85f52be6229b9515197e546fed2af0c22196ab97ca0584312acc7e53e00a26d62650d9270605c8471f4772f644a791da5a8c7854af7520c5ff69031abca0add8cc63980e0b36ab3cdbf70fc8be1e5ec4af028b80d804cd9ffe59b047c374b8c5d39747bed0098c5c3224126800c432c3c2c96a72f982b4245e497edcf0af76e015aa4cee33feb5477171115ce63bc627e2fa30c24442d24c88ea50c120139c431310bc2327d7f4d7642b2f2b8a7052395707c2d2d7cc52069a44568bfa2ba817ded1166f4ae1d71b25e4832c9db4d2cdbdd0661792b1c28ea7f0388d68fb83e1aa7ecf1f769138ed5123526cf14b5a601411326c0b00e189a787690c47b2473bcbb589ba822e7822b1bf010e15e267f93a9bcb599022bcb46be29f2b49c67c74cc90e7fa80fbefd82f99a99f0333895b913174fcdb9adbb5fc21ed60426c96ee304bccbbc05393985b5e397a61a7cda8d08a060ccedd017f84822a6dc832a7626ef5a1c7969c64dafcdcff87320c3985a6a2b56a200f326dcb9abe88a883309381f4feec08997ca5c285603f8b8dc1fa57d5ff10ac779136d3cde2703d0de6c2a4a5889c57e6313467e663e20cbde2b07381e1f31107c2d2d7c42f5899cb55e9eddbec8b0c9bcee4c204840db9fc631a7311bd52632f57439451fc1ae1d3716d96d6e43b69cdd4c818bdd06f004f285056dc9facd79d581bf62fd31f7826a55ac204aa0590acd9c15d2b69c8dad64a36124dfc0b397f1afc76ad52a77094a2a0d57566bbaacfbaad8fad6b5f719c0c3dabeee5d7789619365cb9b9ad7ec993dd569745cf7ca9a63d32202aa6cda6ce5994392dba88347b220069b333794588d0980d214bb814d4e480f56468a11a823cd139a2a391da3a43fccd1221c9d4823426a44457bfbc5b267e5392ee664885c196bd70d9758efd7862d6a338e62305101660a42b2a65361d68bf8e14b5ba0cda3dd05fe254b68e1127e
