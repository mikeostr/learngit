import time
import numpy as np
import ssgetpy
from scipy.io import mmread
matrix = ssgetpy.search(6)[0]
file_path = matrix.download(extract=True)[0] + "/" + matrix.name + ".mtx"
mtx = mmread(file_path)
a = mtx.toarray()


def naiv(a):
    start = time.time()
    len_a = int(a.size ** 0.5 + 0.2)
    n_sim, p_sim = 0, 0
    for i in range(len_a):

        for j in range(i + 1, len_a):
            if a[i][j] == a[j][i]:
                p_sim += 1
                n_sim += 1
            elif a[i][j] != 0 and a[j][i] != 0:
                p_sim += 1
        # print(i, p_sim, n_sim)
    print('len=', len_a, 'p_sim', p_sim, 'n_sim', n_sim)
    p_sim = 2 * (p_sim + len_a) / (len_a ** 2 + len_a)
    n_sim = 2 * (n_sim + len_a) / (len_a ** 2 + len_a)
    end = time.time()
    return p_sim, n_sim, end - start


def numpe_alg(a):
    stat = time.time()
    a_trans = a.transpose()
    a_abs = np.absolute(a)
    n_sym = 1 - np.count_nonzero(a - a_trans) / a.size
    p_sym = (a.size - np.count_nonzero(a_abs + a_trans) + np.count_nonzero(np.multiply(a, a_trans))) / a.size
    end = time.time()
    return p_sym, n_sym, end - stat


print(*naiv(a))
print(*numpe_alg(a))

