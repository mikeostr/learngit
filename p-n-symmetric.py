import time
import numpy as np
import ssgetpy
from scipy.io import mmread
id = 1554
matrix = ssgetpy.search(id)[0]
file_path = matrix.download(extract=True)[0] + "/" + matrix.name + ".mtx"
mtx = mmread(file_path)
a = mtx.toarray()
print(id, a.shape)


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
    # print('len=', len_a, 'p_sim', p_sim, 'n_sim', n_sim)
    p_sim = 2 * (p_sim + len_a) / (len_a ** 2 + len_a)
    n_sim = 2 * (n_sim + len_a) / (len_a ** 2 + len_a)
    end = time.time()
    return p_sim, n_sim, end - start


def numpe_alg(a):
    len_a = a.size
    start = time.time()
    a_trans = a.transpose()
    n_sym = 1 - np.count_nonzero(a - a_trans) / len_a
    no_zero = np.count_nonzero(np.multiply(a, a_trans))
    a_abs = np.absolute(a)
    a_trans_abs = np.absolute(a_trans)
    zero = a.size - np.count_nonzero(a_abs + a_trans_abs)
    p_sym = (zero + no_zero) / len_a
    end = time.time()
    return p_sym, n_sym, end - start


print(*naiv(a))
print(*numpe_alg(a))

