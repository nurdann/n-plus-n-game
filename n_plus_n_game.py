import numpy as np
import sys

# actions: 0 lose
# otherwise win by removing
# one piece from stack A (1)
# one from stack B (2)
# one from both stacks (3)

def nbym(dp):
    (n, m) = dp.shape
    for i in range(n):
        for j in range(m):
            if (i, j) == (0, 0):
                dp[i][j] = 0
            elif i > 0 and dp[i-1][j] == 0:
                dp[i][j] = 1
            elif j > 0 and dp[i][j-1] == 0:
                dp[i][j] = 2
            elif i > 0 and j > 0 and dp[i-1][j-1] == 0:
                dp[i][j] = 3


if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    dp = np.zeros((n+1, m+1), dtype=np.int8)
    nbym(dp)
    if dp[n][m] != 0:
        print("Alice wins")
    else:
        print("Bob wins")
